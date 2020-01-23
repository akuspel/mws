from mathutils import Vector
import math

import bpy
from bpy import context

def distance(a, b):
    
    #calculate distance in each axis
    x = abs(a.x - b.x)
    y = abs(a.y - b.y)
    z = abs(a.z - b.z)
    
    #calculate 3D distance
    d = math.sqrt(x**2 + y**2 + z**2)
    
    return(d)

def dist_fill():
    cursor = Vector(bpy.context.scene.cursor.location)
    object = bpy.context.object.location
    
    cursor.x -= object.x
    cursor.y -= object.y
    cursor.z -= object.z
    
    a = None
    a_l = 10.0
    b = None
    b_l = 10.0
    c = None
    c_l = 10.0
    d = None
    d_l = 10.0
    
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
    for v in bpy.context.object.data.vertices:
        dist = distance(v.co, cursor)
        if dist < a_l:
            a = v
            a_l = dist
    
    for v in bpy.context.object.data.vertices:
        dist = distance(v.co, cursor)
        if dist < b_l:
            if v != a:
                b = v
                b_l = dist
    
    for v in bpy.context.object.data.vertices:
        dist = distance(v.co, cursor)
        if dist < c_l:
            if v != a and v != b:
                c = v
                c_l = dist
    
    for v in bpy.context.object.data.vertices:
        dist = distance(v.co, cursor)
        if dist < d_l:
            if v != a and v != b and v != c:
                d = v
                d_l = dist
    
    a.select = True
    b.select = True
    c.select = True
    d.select = True
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.edge_face_add()
    

class BLT_OT_distance_fill(bpy.types.Operator):
    bl_idname = "mesh.distance_fill"
    bl_label = "Fill by Distance"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if bpy.context.object.mode == "EDIT":
            
            dist_fill()
            
        return {'FINISHED'}

#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(BLT_OT_distance_fill)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(BLT_OT_distance_fill)

register()
