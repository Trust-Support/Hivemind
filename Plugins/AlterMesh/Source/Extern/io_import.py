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
import datetime
from mathutils import Matrix, Vector
from utils import get_geometry_nodes_obj, get_geometry_type
from library import AlterMesh, AlterMeshHandle, Reader
import numpy as np

def update_geometry_node_params(geometry_nodes_obj, new_params: dict):    
    bpy.context.view_layer.objects.active =geometry_nodes_obj

    # todo multiple GN modifiers
    GN = next(modifier for modifier in bpy.context.object.modifiers if modifier.type == 'NODES')

    for params in new_params['Params']:
        if params['Type'] == 'VECTOR':
            vect = params['Value'][0]
            GN[params['Id']][:] = [vect['X'], vect['Y'], vect['Z']]
        elif params['Type'] == 'INT':
            GN[params['Id']] = int(params['Value'])
        elif params['Type'] == 'VALUE':
            GN[params['Id']] = float(params['Value'])
        elif params['Type'] == 'BOOLEAN':
            GN[params['Id']] = bool(params['Value'])
        elif params['Type'] == 'MESH':
            GN[params['Id']] = params['Object']
        elif params['Type'] == 'COLLECTION':
            GN[params['Id']] = params['Collection']            
        elif params['Type'] == 'STRING':
            GN[params['Id']] = str(params['Value'])
        elif params['Type'] == 'IMAGE' or params['Type'] == 'TEXTURE':
            GN[params['Id']] = params['Tex']
        elif params['Type'] == 'RGBA':
            vect = params['Value'][0]
            GN[params['Id']][:] = [vect['R'], vect['G'], vect['B'], vect['A']]
    
    for obj in bpy.data.objects:
        if obj.data and obj.type == "MESH":
            obj.data.update()
        if obj.data and obj.type == "CURVE":
            #workaround for missing update
            obj.data.resolution_u = obj.data.resolution_u
            
def import_texture(Id, x, y):
    print(str(x) + ' ' + str(y), flush=True)
    image = bpy.data.images.new(Id + "_Image", width=x, height=y)
    #pixels = np.zeros(x*y*4, dtype = np.float16)
    #pixels = Reader(np.float16).as_list()
    #pixels = [p / 256 for p in pixels]
    #image.pixels = pixels
    return image

def import_all():
    if AlterMesh.ReadLock(AlterMeshHandle):
        json_str = Reader(np.float16).as_string()
        params_dict = []
        try:
            params_dict = json.loads(json_str)
        except json.decoder.JSONDecodeError:
            if json_str != "":
                print('couldnt parse json: ' + json_str)
        else:
            geometry_nodes_obj = bpy.data.objects.get(params_dict['Object'])
            if geometry_nodes_obj == None:
                geometry_nodes_obj = get_geometry_nodes_obj()

            start = datetime.datetime.now()
            print('Importing')
            for param, i in zip(params_dict['Params'], range(0, len(params_dict['Params']))):
                if param['Type'] == 'IMAGE' or param['Type'] == 'TEXTURE':
                    print('importing texture', flush=True)
                    tex = import_texture(param['Id'], param['X'], param['Y'])
                    params_dict['Params'][i]['Tex'] = tex

                if param['Type'] == 'MESH':
                    obj = get_geometry_type(param['Class']).import_obj(param['Id'])
                    params_dict['Params'][i]['Object'] = obj

                if param['Type'] == 'COLLECTION':
                    
                    #todo reuse
                    #create new collection for this param
                    collection = bpy.data.collections.new(param["Id"] + "_Collection")
                    bpy.context.scene.collection.children.link(collection)

                    #import all objs for that param
                    for class_name, j in zip(param['Classes'], range(0, param['Num'])):
                        obj = get_geometry_type(class_name).import_obj(param['Id'] + '_' + str(j))
                        collection.objects.link(obj)
                    params_dict['Params'][i]['Collection'] = collection

            update_geometry_node_params(geometry_nodes_obj, params_dict)

            if (bpy.context.scene.frame_current != params_dict["Frame"]):
                bpy.context.scene.frame_set(params_dict["Frame"] % bpy.context.scene.frame_end)

            end = datetime.datetime.now()
            print('Imported in ' + str((end-start).seconds + (end-start).microseconds/1000000) + 's')

        AlterMesh.ReadUnlock(AlterMeshHandle)
        return params_dict
