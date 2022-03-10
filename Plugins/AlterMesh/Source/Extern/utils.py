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

def get_geometry_nodes_obj():
    for obj in bpy.data.objects:
            for modifier in obj.modifiers:
                if modifier.type == 'NODES':
                    return obj

                    
def make_obj_for_param(ParamType, Id):
    name = ParamType + '_' + Id
    mesh = bpy.data.meshes.get(name)
    obj = bpy.data.objects.get(name)

    if mesh == None:
        mesh = bpy.data.meshes.new(name)
        obj = bpy.data.objects.new(name, mesh)

    mesh.clear_geometry()

    if bpy.context.scene.collection.objects.get(obj.name) == None:
        bpy.context.scene.collection.objects.link(obj)
    
    return obj, mesh


import importlib
importlib.import_module('GeometryTypes')
from os import walk, path

from importlib import util

def get_geometry_types():
    geometry_types_path = path.abspath( path.dirname(path.realpath(__file__)) + '\\GeometryTypes')
    geometry_types = []
    for (dirname, folders, filenames) in walk(geometry_types_path):
        for filename in filenames:
            file, ext = path.splitext(filename)
            module = 'GeometryTypes.' + file
            if (ext == '.py' and util.find_spec(module)):
                geometry_types += [importlib.import_module(module)]
    return geometry_types
                
def get_geometry_type(class_name):
    for geometry_type in get_geometry_types():
        if (geometry_type.__name__ == 'GeometryTypes.' + class_name):
            return geometry_type
