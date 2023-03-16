import bpy, bmesh
from mathutils import *
D = bpy.data
C = bpy.context

class MWS_OT_CallToolPie(bpy.types.Operator):

    bl_idname = "mws.call_tools"
    bl_label = "Call Tool Pie"
    bl_options = {"REGISTER"}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="MWS_MT_toolpie")

        return {"FINISHED"}

class MWS_OT_CallMergePie(bpy.types.Operator):

    bl_idname = "mws.call_merge"
    bl_label = "Call Merge Pie"
    bl_options = {"REGISTER"}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="MWS_MT_mergepie")

        return {"FINISHED"}