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
from mathutils import Matrix
from library import Reader
import numpy as np

def import_obj(object_name):
    matrix = Reader(np.float32).as_array(4).tolist()
    
    obj = bpy.data.objects.new( "NewEmpty", None )
    bpy.context.scene.collection.objects.link(obj)
    obj.matrix_world = Matrix((matrix[0],matrix[1],matrix[2],matrix[3]))
    obj.matrix_world = obj.matrix_world * bpy.context.scene.unit_settings.scale_length
    obj.scale[0] = obj.scale[0] * -1
    return obj
    
def used_for_object(obj):
    False

def get_defaults(obj):
    pass