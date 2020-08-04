#!/usr/bin/python
# -*- coding: utf-8 -*-
import bpy
import os
from bpy import context
from math import radians

file_loc = \
'/Users/nhipham/Desktop/obj files/colored_cylinder/pulling_downward'
target_loc = \
'/Users/nhipham/Desktop/obj files/colored_cylinder/rendered_images/cylinder_pulling_downward/'

file_list = sorted(os.listdir(file_loc))
obj_list = [item for item in file_list if item.endswith('.obj')]
cnt = 0

for i in range(len(obj_list)):
    
    o = obj_list[i]
    # import the obj

    path = os.path.join(file_loc, o)
    bpy.ops.import_scene.obj(filepath=path)
    obj = bpy.context.window.scene.objects[0]
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    #obj.scale = (5.0, 5.0, 5.0)

    # add light
    light_data = bpy.data.lights.new(name='light_2.80', type='SUN')
    light_data.energy = 30
    light_object = bpy.data.objects.new(name='Sun', object_data=light_data)
    bpy.context.collection.objects.link(light_object)

    # create the camera

    cam = bpy.data.cameras.new('Camera')
    cam_obj = bpy.data.objects.new('Camera', cam)
    cam_obj.location = (0.0, 0.0, 2.0)
    cam_obj.rotation_euler = (0.0, 0.0, 0.0)
    scn = bpy.context.scene
    scn.collection.objects.link(cam_obj)
    bpy.context.view_layer.objects.active = cam_obj
    cam_obj.select_set(True)
    scn.camera = context.object
    cam_obj.scale = (0.5, 0.5, 0.5)

    # export rendered images
    #for angle in range(0, 360, 120):
    cam_obj.rotation_euler[1] = radians(0)
    bpy.context.scene.render.filepath = target_loc + '/image-' + str(cnt) + '-' + str(0)
    bpy.ops.render.render(write_still=True)

    # delete all objs

    while len(bpy.context.scene.objects) > 0:
        del_obj = bpy.context.scene.objects[0]
        bpy.context.view_layer.objects.active = del_obj
        del_obj.select_set(True)
        bpy.ops.object.delete()
    cnt += 1