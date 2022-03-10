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
from multiprocessing import Semaphore, shared_memory
import time
import datetime

import os
import sys

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

from utils import get_geometry_nodes_obj
from io_import import import_all
from io_export import export
from library import AlterMesh, AlterMeshHandle

def run():    
    update_rate = 0.005
    idle_time = 0

    # make object visible
    for layer_collection in bpy.context.view_layer.layer_collection.children:
        layer_collection.exclude = False

    while idle_time < 60:
        # read params back from unreal
        import_params = import_all()
        idle_time = idle_time + update_rate
        if import_params is not None and 'NeedsUpdate' in import_params:
            del import_params['NeedsUpdate']

            obj = bpy.data.objects.get(import_params['Object'])
            if obj == None:
                obj = get_geometry_nodes_obj()

            if obj.hide_get():
                obj.hide_set(False, view_layer=bpy.context.view_layer)

            start = datetime.datetime.now()
            export(obj)
            end = datetime.datetime.now()
            print('Exported in ' + str((end-start).seconds + (end-start).microseconds/1000000) + 's', flush=True)
            idle_time = 0

        if bpy.app.background:
            time.sleep(update_rate)
        else:
            break

    if bpy.app.background:
        AlterMesh.Free(AlterMeshHandle)
    else:
        return update_rate