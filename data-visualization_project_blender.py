import bpy
import csv

# selecting and deleting previous objects to clean up the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


bar_spacing = 1.5
bar_width = 2

# importing the csv file
with open(r"C:\Users\Have Fun\Documents\coding\python\Bar_Graph_Resource_Files\sample.csv") as f:
    readout = list(csv.reader(f))
    print(readout)

for a in readout:
    placement = readout.index(a)
    bpy.ops.mesh.primitive_plane_add(size=1)
    new_bar = bpy.context.object
    
    for vert in new_bar.data.vertices:
        # co[1] stands for the y location of the vertices [y, y, z]
        vert.co[1] += 0.5
        # placing the planes on their position
        vert.co[0] += placement*bar_spacing + 0.5
     
       
    new_bar.scale = (bar_width, float(a[1]), 1)
    
    # creating and aligning text desciption with the names from the csv file
    bpy.ops.object.text_add()
    bpy.context.object.data.align_y = 'CENTER'
    bpy.context.object.data.align_x = 'RIGHT'
    bpy.ops.transform.rotate(value=-1.5708)
    bpy.ops.transform.translate(value=(placement*bar_spacing*2.1, -0.5, 0))
    bpy.context.object.data.body = a[0]

