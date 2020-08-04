import bpy
import os

file_loc = '/Users/nhipham/Desktop/obj files/Sphere/raw_collision'
target_loc = '/Users/nhipham/Desktop/obj files/Sphere/modified_collision'

file_list = sorted(os.listdir(file_loc))
obj_list = [item for item in file_list if item.endswith('.obj')]

for obj in obj_list:
    # import the obj
    path = os.path.join(file_loc, obj)
    bpy.ops.import_scene.obj(filepath = path)
    
    # set obj to origin and export
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    bpy.data.objects[0].location = [0,0,0]
    target_file = os.path.join(target_loc, obj)
    bpy.ops.export_scene.obj(filepath=target_file)
    
    # delete the obj
    del_obj = bpy.context.scene.objects[0]  
    bpy.context.view_layer.objects.active = del_obj 
    del_obj.select_set(True) 
    bpy.ops.object.delete()

