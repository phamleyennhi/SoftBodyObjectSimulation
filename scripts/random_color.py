# subdivide the surface in Blender
# create the materials you want to randomly assign to the faces of the objects

import bpy
import bmesh 
import random

obj = bpy.context.active_object
bm = bmesh.from_edit_mesh(obj.data) 

for f in bm.faces:
    f.material_index = random.randint(0,4)
bmesh.update_edit_mesh(obj.data)