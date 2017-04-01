"""
Details-

start()- function to delete any pre-existing object and add the mesh plane.
extrude()- function to extrude the plane in z-axis to 2.0 units.
pyramid(obj)- function to take the mesh-plane as argument, set it in object mode and scale the
              vertices such that they coincide and required pyramid is formed.
main()- driver function to centralize all definrd-functions and run/call them.
"""

import bpy      #To import all blender functions

def start():    #Function to add plane and return it's object
    bpy.ops.object.delete() #delete any object present in scene
    bpy.ops.mesh.primitive_plane_add()  #add a mesh plane to scene
    return bpy.context.selected_objects[0]  #return the mesh plane

def extrude():
    bpy.ops.object.mode_set(mode='EDIT')    #to set the object in EDIT mode
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 2), "constraint_axis":(False, False, True)})

def pyramid(obj):
    bpy.ops.object.mode_set(mode='OBJECT')
    obj.data.vertices[4].co.x+= 1.0
    obj.data.vertices[5].co.x-= 1.0
    obj.data.vertices[6].co.x+= 1.0
    obj.data.vertices[7].co.x-= 1.0
    obj.data.vertices[4].co.y+= 1.0
    obj.data.vertices[5].co.y+= 1.0
    obj.data.vertices[6].co.y-= 1.0
    obj.data.vertices[7].co.y-= 1.0


def main():
    ob = start()
    extrude()
    pyramid(ob)

main()