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
import sys
import os

dir = os.path.dirname(__file__)
if not dir in sys.path:
    sys.path.append(dir )
    sys.path.append(dir + '\\GeometryTypes\\')

import sys
guids = sys.argv[sys.argv.index("--") + 1:]

from bpy.app.handlers import persistent

if __name__ == '__main__':
    from library import setup_dll
    setup_dll(guids[0], guids[1])   

    from AlterMesh import run
    if not bpy.app.background:
        bpy.app.timers.register(run)
    else:
        run()
