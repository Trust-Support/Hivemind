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
from library import Reader
from mathutils import Vector
from enum import Enum

class SplineType(Enum):
    LINEAR = 0,
    CURVE = 1,
    CONSTANT = 2

def import_obj(object_name):
    resolution = Reader(np.int32).as_value()
    cyclic = Reader(np.bool8).as_value()
     
    locations = Reader(np.float32).as_array(3)
    locations = locations / bpy.context.scene.unit_settings.scale_length
    locations = locations.tolist()

    scales = Reader(np.float32).as_list(3)
    tilts = Reader(np.float32).as_list()
    
    right_tangents = Reader(np.float32).as_array(3)
    right_tangents = right_tangents / bpy.context.scene.unit_settings.scale_length
    right_tangents = right_tangents.tolist()
    
    left_tangents = Reader(np.float32).as_array(3)
    left_tangents = left_tangents / bpy.context.scene.unit_settings.scale_length
    locatleft_tangentsions = left_tangents.tolist()

    point_types = Reader(np.int32).as_list()

    name = 'Curve_' + object_name
    curve_data = bpy.data.curves.get(name)
    
    if curve_data == None:
        curve_data = bpy.data.curves.new('Curve_' + object_name, type='CURVE')

    curve_data.dimensions = '3D'
    curve_data.resolution_u = resolution
    curve_data.splines.clear()
    
    spline = curve_data.splines.new('BEZIER')
    spline.bezier_points.add(len(locations)-1)
    spline.use_cyclic_u = cyclic
    
    for i, coord in enumerate(locations):
        spline.bezier_points[i].co = coord
        spline.bezier_points[i].tilt = tilts[i] / 180 * 3.14 * -1
        
        inverted = [tangent * -1 for tangent in left_tangents[i]]        
        spline.bezier_points[i].handle_left = Vector((inverted)) + spline.bezier_points[i].co
        spline.bezier_points[i].handle_right = Vector((right_tangents[i])) + spline.bezier_points[i].co        

        spline.bezier_points[i].radius = scales[i][1]

        if point_types[i] == SplineType.LINEAR:
            print(i, flush=True)
            spline.bezier_points[i].handle_right_type = 'VECTOR'
            spline.bezier_points[(i+1) % len(spline.bezier_points)].handle_left_type = 'VECTOR'
            
        if point_types[i] == SplineType.CONSTANT:
            print(i, flush=True)
            spline.bezier_points[(i+1) % len(spline.bezier_points)].handle_left_type = 'VECTOR'

    obj = bpy.data.objects.get(name)
    if obj == None:
        obj = bpy.data.objects.new(name, curve_data)
    
    if bpy.context.scene.collection.objects.get(obj.name) == None:
        bpy.context.scene.collection.objects.link(obj)

    return obj

from library import AlterMesh, AlterMeshHandle, Writer
import numpy as np

def used_for_object(obj):
    return obj.type == 'CURVE' and len(obj.data.splines) > 0

def get_defaults(obj):    
    if obj.data.splines[0].type == 'NURBS':
        locations = np.empty(len(obj.data.splines[0].points)*4, dtype=np.float32)  
        obj.data.splines[0].points.foreach_get('co', locations)

        #ignore weight, its gonna be imported as bezier anyway
        locations = locations.reshape(locations.size//4,4)
        locations = np.delete(locations, 3, 1)
        locations = np.ravel(locations)

    if obj.data.splines[0].type == 'BEZIER':
        locations = np.empty(len(obj.data.splines[0].bezier_points)*3, dtype=np.float32)  
        obj.data.splines[0].bezier_points.foreach_get('co', locations)        

    Writer().from_array(locations)
