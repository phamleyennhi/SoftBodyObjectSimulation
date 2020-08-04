# Please adjust the working and twisting axis before using the script

import bpy
import os
import math


target_loc = '/Users/nhipham/Desktop/obj files/colored_cylinder/bending'
 
# set obj to origin and export
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
cylinder = bpy.data.objects[0]
cylinder.location = [0,0,0]
cylinder.select_set(True)

# add modifier - bending
modifier = cylinder.modifiers.new(name='cylinder', type='SIMPLE_DEFORM')
modifier.origin = bpy.data.objects['Empty'] 
modifier.deform_method = 'TWIST'
modifier.deform_axis = 'X'
modifier.angle = 0

for i in range(101):
    modifier.angle = math.radians(i);
    target_file = os.path.join(target_loc, 'cylinder'+ str(i) + '.obj')
    bpy.ops.export_scene.obj(filepath=target_file)
    
modifier.angle = 0;