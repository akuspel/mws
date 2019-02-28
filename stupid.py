import bpy

class MWS_OT_CallTools(bpy.types.Operator) :
    bl_idname = "mws.call_tools"
    bl_label = "Call Tools Pie"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.wm.call_menu_pie(name="mws_tool_pie")
        return {"FINISHED"}


#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_CallTools)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_CallTools)

register()