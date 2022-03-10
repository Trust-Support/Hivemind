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
from utils import make_obj_for_param
import numpy as np

def import_obj(object_name):
    obj, mesh = make_obj_for_param('Landscape', object_name)
    
    indices = Reader(np.int32).as_array()
    # flip winding
    indices = np.flip(indices, 1)
    indices = [indices[x:x+3] for x in range(0, len(indices), 3)]

    locations = Reader(np.float32).as_array(3)
    locations = locations / bpy.context.scene.unit_settings.scale_length
    locations = locations.tolist()

    normals = Reader(np.float32).as_list(3)
    
    mesh.from_pydata(locations, normals, indices)
    return obj
    
def used_for_object(obj):
    False

def get_defaults(obj):
    pass