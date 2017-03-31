"""
Type- Basic
A simple python script that adds a mesh object (Toros) in active scene and modify it forming a crown.
Instad of extrusion, Toros is scaled to form a crown.
"""

import bpy

#Function to remove the current selected object (Default Cube) and add Toros. 
def start():
    bpy.ops.object.delete()
    bpy.ops.mesh.primitive_torus_add()
    return bpy.context.selected_objects[0]

#Function to flatten the top surface of Torros
def flatten(ob):
    for i in range(3,576,12):
        ob.data.vertices[i].co.z-=0.03

#Function to scale the toros's vertices to make vertical strands forming a crown. 
def stands(ob):
    for i in range(2,576,36):
        for j in range(4):
            if(j<2):
                ob.data.vertices[i+j].co.z+=0.5
            else:
                ob.data.vertices[i+10+j].co.z+=0.5

obj = start()
flatten(obj)
stands(obj)