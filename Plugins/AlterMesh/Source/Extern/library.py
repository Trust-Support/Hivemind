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

import ctypes
import os
import numpy as np

AlterMesh = None
AlterMeshHandle = None

def setup_dll(guid1, guid2):
    dll_path = os.path.abspath( os.path.dirname(os.path.realpath(__file__)) + '\\AlterMesh.dll')
    
    global AlterMesh
    global AlterMeshHandle

    AlterMesh = ctypes.cdll.LoadLibrary(dll_path)
    AlterMesh.Init.argtypes = (ctypes.c_wchar_p,ctypes.c_wchar_p)
    AlterMesh.Init.restype = ctypes.c_void_p

    AlterMeshHandle = AlterMesh.Init(guid1, guid2)

    AlterMesh.Read.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t))
    AlterMesh.Read.restype = ctypes.c_bool

    AlterMesh.Write.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)
    AlterMesh.Write.restype = None

    AlterMesh.ReadLock.argtypes = (ctypes.c_void_p,)
    AlterMesh.ReadLock.restype = ctypes.c_bool

    AlterMesh.WriteLock.argtypes = (ctypes.c_void_p,)
    AlterMesh.WriteLock.restype = ctypes.c_bool

    AlterMesh.ReadUnlock.argtypes = (ctypes.c_void_p,)
    AlterMesh.ReadUnlock.restype = None

    AlterMesh.WriteUnlock.argtypes = (ctypes.c_void_p,)
    AlterMesh.WriteUnlock.restype = None

    AlterMesh.Free.argtypes = (ctypes.c_void_p,)
    AlterMesh.Free.restype = None

class Reader:
    buffer = 0
    length = 0
    dtype = None
    
    def __init__(self, dtype) -> None:
        length = ctypes.c_ulonglong(0)
        address = ctypes.c_void_p()

        if AlterMesh.Read(AlterMeshHandle, ctypes.byref(address), length):    
            ArrayType = ctypes.c_char * length.value
            bytes = ctypes.cast(address, ctypes.POINTER(ArrayType)).contents[:length.value]
        else:
            bytes = b''

        self.buffer = bytes
        self.length = length.value
        self.dtype = dtype
    
    def as_array(self, num_components=1):
        array = np.frombuffer(self.buffer, np.dtype(self.dtype))
        if num_components > 1:
            array = array.reshape(array.size//num_components, num_components)
        return array

    def as_list(self, num_components=1):
        return self.as_array(num_components).tolist()

    def as_value(self):
        return self.as_array().item()

    def as_string(self):
        string = str(self.buffer, encoding = 'ascii')
        string = string.replace('\x00', '')
        return string

class Writer():
    dtype = None

    def __init__(self, dtype=np.byte) -> None:
        self.dtype = dtype

    def from_array(self, array):
        AlterMesh.Write(AlterMeshHandle, array.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)), array.nbytes)

    def from_value(self, value):
        array = np.asarray(value, self.dtype)
        AlterMesh.Write(AlterMeshHandle, array.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)), array.nbytes)
        
    def from_buffer(self, value):
        array = np.frombuffer(value, self.dtype)
        AlterMesh.Write(AlterMeshHandle, array.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)), array.nbytes)