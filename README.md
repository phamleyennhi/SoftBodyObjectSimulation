# Soft Body Object Simulation using Blender

This is a documentation of generating soft body objects with simple deformations in Blender. The data collection includes soft sphere, soft cube, and soft cylinder with deformations such as bending, twisting, and inflation/deflation.

## Files
* `scripts/`: includes bending.py - generating bending deformations at different angles, twisting.py - generating twisting deformations at different angles, set_origin.py - moving the object back to origin in a simulation and export the .obj file, image_rendering.py - rendering the internal image of a sequence of objects in a simulation, and random_color - assigning predefined color materials randomly to the subdivided faces of the object.
* `colored objects/` : .obj files of randomly colored objects, including a colored soft sphere, colored soft cube, and colored soft cylinder.
* `colored_sphere/`: .obj files from collision, inflation, and deflation simulations, and internal images of these objects.
* `colored_cube/`: .obj files from collision, pulling downward by gravity, stretching, and twisting simulations, and internal images of these objects.
* `colored_cylinder/`: .obj files from pulling downward by gravity, bending and twisting simulations, and internal images of these objects.
* `backup/`: previously unsuccessful tries of the simulations.

## Run scripts

This section explains how to use each script in the scripts folder.
### random_color.py
This script helps with the process of randomly assigning colors to the subdivided faces of an object's surface.
1. Open Blender, create the object (sphere, cube, cylinder, etc), and adjust the soft body parameters
2. Subdivide the surface of the object in Edit mode
3. Create the colors/materials you want to randomly assign to the faces of the objects
4. Go to Scripting -> Text editor, copy and paste the random_color.py script to the text editor. Make any necessary changes such as the number of colors you want to randomly assign.
5. Run the script. After having the randomly colored objects, you can import it into Blender and create any simulation you want.

### set_origin.py
This script helps with setting the location of the object in an .obj file back to the origin.
1. Open Blender, go to Scripting -> Text editor, copy and paste the set_origin.py script to the text editor
2. Change the file_loc and target_loc properly
3. Run the script

### bending.py, twisting.py
These scripts help with generating a sequence of .obj files in bending/twisting deformation at different angles.
1. Open Blender, import the soft body object into the scene, and adjust the parameters
2. Go to Scripting -> Text editor, copy and paste the script to the text editor
3. Create an empty axis in the scene to serve as the bending/twisting modifier origin (modifier.origin)
4. Change the target_loc path, and the deform_axis.
5. Run the script

### image_rendering.py
This script helps with generating the sequence of internal images of an obj simulation
1. Open Blender, go to Scripting -> Text editor, copy and paste the script to the text editor
2. Adjust the lighting and camera scale/parameters in the script
3. Run the script
