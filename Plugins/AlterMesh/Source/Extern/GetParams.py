import json
import bpy
import os
import sys

dir = os.path.dirname(__file__)
if not dir in sys.path:
    sys.path.append(dir )

def get_geometry_nodes_params(obj):
    '''Get exposed geometry nodes params, defaults from OBJECT instead of node group, so user gets exactly whats in the blend file'''
    params = []
    for modifier in obj.modifiers:
        if modifier.type == 'NODES':
            for input in modifier.node_group.inputs:                
                
                # Ignored
                if input.type == 'MATERIAL' or input.type == 'GEOMETRY':
                    continue

                new_param = {}
                new_param['Id'] = input.identifier
                new_param['Name'] = input.name
                new_param['Type'] = input.type

                if input.type == 'INT' or input.type == 'VALUE' or input.type == 'VECTOR':
                    new_param['MinValue'] = input.min_value
                    new_param['MaxValue'] = input.max_value

                if input.type == "VECTOR":
                    new_param['DefaultValue'] = [modifier[input.identifier][0], modifier[input.identifier][1], modifier[input.identifier][2]]                    
                elif input.type == "RGBA":
                    new_param['DefaultValue'] = [modifier[input.identifier][0], modifier[input.identifier][1], modifier[input.identifier][2], modifier[input.identifier][3]]
                
                
                if input.type == 'INT' or input.type == 'VALUE' or input.type == 'BOOLEAN' or input.type == 'STRING':
                    new_param['DefaultValue'] = modifier[input.identifier]

                params += [new_param]
    return params

def get_materials():
    names = []
    for material in bpy.data.materials[:]:
        names += [material.name]
    return names


geometry_nodes_objs = []
for obj in bpy.data.objects:
        for modifier in obj.modifiers:
            if modifier.type == 'NODES':
                geometry_nodes_objs += [obj]


if len(geometry_nodes_objs) < 1:
    print("No geometry nodes object found", file=sys.stderr)

import ctypes

from library import setup_dll
guids = sys.argv[sys.argv.index("--") + 1:]
setup_dll(guids[0], guids[1])

from library import AlterMesh, AlterMeshHandle, Writer
from utils import get_geometry_types
import numpy as np

while True:
    if AlterMesh.WriteLock(AlterMeshHandle):
        Writer(np.int32).from_value(len(geometry_nodes_objs))

        for obj in geometry_nodes_objs:    
            Writer().from_buffer(bytes(obj.name, "UTF-16-LE"))

            export_params = {'Params': get_geometry_nodes_params(obj), 'Materials' : get_materials()}
            Writer().from_buffer(bytes(json.dumps(export_params), "UTF-16-LE"))

            geometry_types = get_geometry_types()
            for modifier in obj.modifiers:
                if modifier.type == 'NODES':
                    for input in modifier.node_group.inputs:
                        has_default = False
                        if input.type == "OBJECT":
                            default_geometry_type = None

                            # Find which class we should use for defaults
                            for geometry_type in geometry_types:
                                if modifier[input.identifier] is not None and geometry_type.used_for_object(modifier[input.identifier]):
                                    default_geometry_type = geometry_type
                                    break
                                
                            geometry_type_name_bytes = bytes(default_geometry_type.__name__, "UTF-16-LE") if default_geometry_type is not None else b''
                            Writer().from_buffer(geometry_type_name_bytes)

                            # Let it write defaults
                            if default_geometry_type is not None:
                                default_geometry_type.get_defaults(modifier[input.identifier])

        AlterMesh.WriteUnlock(AlterMeshHandle)
        break

import time
time.sleep(1)
AlterMesh.Free(AlterMeshHandle)