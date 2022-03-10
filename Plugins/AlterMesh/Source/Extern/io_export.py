# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import json
import ctypes
import numpy as np
import bpy_types
from array import array
from mathutils import Matrix, Vector
from utils import get_geometry_nodes_obj
from library import AlterMesh, AlterMeshHandle, Writer

def get_geometry_nodes_params():
    '''Get exposed geometry nodes params'''
    params = []

    for group in bpy.data.node_groups:
        if group.type == 'GEOMETRY':
            for input in group.inputs:
                if input.type == 'MATERIAL':
                    continue
                new_param = {}
                new_param['Id'] = input.identifier
                new_param['Name'] = input.name
                new_param['Type'] = input.type
                if input.type != 'GEOMETRY':
                    if input.type == "VECTOR":
                        new_param['DefaultValue'] = [input.default_value[0], input.default_value[1], input.default_value[2]]
                    else:
                        new_param['DefaultValue'] = input.default_value
                params += [new_param]
    return params

def get_materials(mesh):
    names = []
    for material in mesh.materials[:]:
        if material is not None:
            names += [material.name_full]
        else:
            names += ['Default']
    return names

def get_mesh_data(mesh):
    mesh.calc_loop_triangles()
    mesh.calc_normals_split()

    locations = np.empty(len(mesh.vertices)*3, dtype=np.float32)  
    mesh.vertices.foreach_get('co', locations)
    
    normals = np.empty(len(mesh.loop_triangles)*3*3, dtype=np.float32)
    mesh.loop_triangles.foreach_get('split_normals', normals)

    indices = np.empty(len(mesh.loop_triangles)*3, dtype=np.int32)
    mesh.loop_triangles.foreach_get('vertices', indices)

    triangle_loops = np.empty(len(mesh.loop_triangles)*3, dtype=np.int32)
    mesh.loop_triangles.foreach_get('loops', triangle_loops)

    loops = np.empty(len(mesh.loops), dtype=np.int32)
    mesh.loops.foreach_get('vertex_index', loops)

    # todo better way to import UVs and colors from attributes when available
    has_vertex_indexed_colors = False

    if len(mesh.vertex_colors) > 0:
        colors = np.empty(len(mesh.vertex_colors[0].data)*4, dtype=np.float32)
        mesh.vertex_colors[0].data.foreach_get('color', colors)
    elif mesh.attributes.get('Col') and len(mesh.attributes.get('Col').data) > 0:
        attribute_colors = mesh.attributes.get('Col')
        colors = np.empty(len(attribute_colors.data)*4, dtype=np.float32)
        attribute_colors.data.foreach_get('color', colors)
        has_vertex_indexed_colors = attribute_colors.domain == 'POINT'
    else:
        colors = np.zeros(len(mesh.loops)*4, dtype=np.float32)

    has_vector3_uvs = False
    has_vertex_indexed_uvs = False

    if mesh.attributes.get('UVMap') and len(mesh.attributes.get('UVMap').data) > 0:
        attribute_uvmap = mesh.attributes.get('UVMap')     
        uv_size = len(attribute_uvmap.data[0].vector)
        has_vector3_uvs = uv_size == 3
        has_vertex_indexed_uvs = attribute_uvmap.domain == 'POINT'
        uvs = np.empty(len(attribute_uvmap.data)*uv_size, dtype=np.float32)
        attribute_uvmap.data.foreach_get('vector', uvs)
    elif mesh.attributes.get('uv_map') and len(mesh.attributes.get('uv_map').data) > 0:
        attribute_uvmap = mesh.attributes.get('uv_map')
        uv_size = len(attribute_uvmap.data[0].vector)
        has_vector3_uvs = uv_size == 3
        has_vertex_indexed_uvs = attribute_uvmap.domain == 'POINT'
        uvs = np.empty(len(attribute_uvmap.data)*uv_size, dtype=np.float32)
        attribute_uvmap.data.foreach_get('vector', uvs)        
    elif len(mesh.uv_layers) > 0:
        uvs = np.empty(len(mesh.loops)*2, dtype=np.float32)    
        if len(mesh.uv_layers) > 0 :
            mesh.uv_layers[0].data.foreach_get('uv', uvs)
    else:
        uvs = np.zeros(len(mesh.loops)*2, dtype=np.float32)
    
    # make float3 uvs into float2
    if has_vector3_uvs:
        uvs = uvs.reshape((int(len(uvs)/3),3))
        uvs = np.delete(uvs, 2, 1)
        uvs = np.ravel(uvs)

    materials = np.empty(len(mesh.loop_triangles), dtype=np.int32)
    mesh.loop_triangles.foreach_get('material_index', materials)

    material_names = {'Materials' : get_materials(mesh)}
    material_names = json.dumps(material_names)

    mesh_hash = np.asarray(hash(mesh), np.int64)
    material_names = np.frombuffer(bytes(material_names, "UTF-16-LE"), np.byte)
    vertex_indexed_uvs = np.asarray(has_vertex_indexed_uvs, np.bool8)
    vertex_indexed_colors = np.asarray(has_vertex_indexed_colors, np.bool8)    

    return locations, normals, indices, triangle_loops, loops, colors, uvs, materials, material_names, mesh_hash, vertex_indexed_colors, vertex_indexed_uvs

def get_original_input(geometry_nodes_obj, original_mesh):
    # todo multiple GN modifiers
    GN = next(modifier for modifier in geometry_nodes_obj.modifiers if modifier.type == 'NODES')

    # find original input object
    instance_of = ''
    for input in GN.items():
        if (type(input[1]) == bpy_types.Object and input[1].data is not None and input[1].data == original_mesh):
            instance_of = input[0]
            break
        
    return instance_of

def get_instance_data(geometry_nodes_obj, mesh, original_mesh, matrix_local, matrix_world):
    original_input = np.frombuffer(bytes(get_original_input(geometry_nodes_obj, original_mesh), "UTF-16-LE"), np.byte)
    matrix_local = np.array(matrix_local, np.float32)
    matrix_world = np.array(matrix_world, np.float32)
    mesh_hash = np.asarray(hash(mesh), np.int64)

    return original_input, matrix_local, matrix_world, mesh_hash

def export(geometry_nodes_obj):
    if AlterMesh.WriteLock(AlterMeshHandle):
        print('Exporting')

        depsgraph = bpy.context.evaluated_depsgraph_get()        
        evaluated_geometry_nodes_data = geometry_nodes_obj.evaluated_get(depsgraph).data

        mesh_hashes = []
        mesh_datablocks = []
        instance_datablocks = []
        instance_original_datablocks = []
        instance_local_matrices = []
        instance_world_matrices = []
        
        # Get number of meshes and instances
        if geometry_nodes_obj.type == 'MESH':
            mesh_hashes = [hash(geometry_nodes_obj)]
            mesh_datablocks = [evaluated_geometry_nodes_data]
            instance_datablocks = [evaluated_geometry_nodes_data]
            instance_original_datablocks = [None]
            instance_local_matrices = [Matrix() * bpy.context.scene.unit_settings.scale_length]
            instance_world_matrices = [geometry_nodes_obj.matrix_world.copy() * bpy.context.scene.unit_settings.scale_length]

        for instance in depsgraph.object_instances:
            if instance.instance_object and instance.parent and instance.parent.original == geometry_nodes_obj:
                if instance.object.type == 'MESH':
                    # No need to export instances that aren't realized
                    if hash(instance.object.data) not in mesh_hashes:
                        mesh_hashes += [hash(instance.object.data)]
                        mesh_datablocks += [instance.object.data]
                    if hash(instance.object.data) in mesh_hashes:
                        instance_datablocks += [instance.object.data]
                        instance_original_datablocks += [instance.object.original.data]
                        local_matrix = instance.parent.matrix_world.inverted() @ instance.matrix_world                        
                        instance_local_matrices += [local_matrix * bpy.context.scene.unit_settings.scale_length]
                        instance_world_matrices += [instance.matrix_world.copy() * bpy.context.scene.unit_settings.scale_length]
                        
        Writer(np.int32).from_value(len(mesh_datablocks))
        Writer(np.int32).from_value(len(instance_datablocks))
        
        # Export meshes
        for mesh in mesh_datablocks:
            for array in get_mesh_data(mesh):
                Writer().from_array(array)

        # Export Instances
        for mesh, original_mesh, matrix_local, matrix_world in zip(instance_datablocks, instance_original_datablocks, instance_local_matrices, instance_world_matrices):
            for array in get_instance_data(geometry_nodes_obj, mesh, original_mesh, matrix_local, matrix_world):
                Writer().from_array(array)

        AlterMesh.WriteUnlock(AlterMeshHandle)
