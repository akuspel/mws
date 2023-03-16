import bpy
from bpy.props import BoolProperty
from mathutils import *
D = bpy.data
C = bpy.context

# functions
def reset_cursor(self, context, axis):

    # reset based on origin
    if self.selection == False:
        context.scene.cursor.location[axis] = 0
    
    # reset based on selection
    else:

        curx = context.scene.cursor.location[0]
        cury = context.scene.cursor.location[1]
        curz = context.scene.cursor.location[2]
        pos_1 = [curx, cury, curz]

        # snap to selection
        bpy.ops.view3d.snap_cursor_to_selected()
        pos_2 = context.scene.cursor.location[axis]

        # set cursor location
        context.scene.cursor.location = pos_1
        context.scene.cursor.location[axis] = pos_2


# classes
class MWS_OT_reset_cursor_x(bpy.types.Operator):

    bl_idname = "cursor.x"  
    bl_label = "Reset Cursor X"  
    bl_description = "Reset Cursor along X axis"
    bl_options = {"REGISTER", "UNDO"} 
    
    selection: BoolProperty(
        name = "To Selection",
        default = False,
        description = "cursor to selection"
    )

    def execute(self, context):
        
        reset_cursor(self, context, 0)

        return {"FINISHED"}

class MWS_OT_reset_cursor_y(bpy.types.Operator): 

    bl_idname = "cursor.y"  
    bl_label = "Reset Cursor Y"  
    bl_description = "Reset Cursor along Y axis"
    bl_options = {"REGISTER", "UNDO"} 

    selection: BoolProperty(
        name = "To Selection",
        default = False,
        description = "cursor to selection"
    )

    def execute(self, context):
        
        reset_cursor(self, context, 1)

        return {"FINISHED"}

class MWS_OT_reset_cursor_z(bpy.types.Operator):

    bl_idname = "cursor.z"  
    bl_label = "Reset Cursor Z"
    bl_description = "Reset Cursor along Z axis"
    bl_options = {"REGISTER", "UNDO"} 

    selection: BoolProperty(
        name = "To Selection",
        default = False,
        description = "cursor to selection"
    )

    def execute(self, context):
        
        reset_cursor(self, context, 2)

        return {"FINISHED"}