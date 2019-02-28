import bpy

class MWS_OT_QuickDelete(bpy.types.Operator) :
    bl_idname = "mesh.quickdelete"
    bl_label = "Quick Delete"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            if bpy.context.tool_settings.mesh_select_mode[0] == True and bpy.context.tool_settings.mesh_select_mode[1] == False and bpy.context.tool_settings.mesh_select_mode[2] == False:
                bpy.ops.mesh.delete(type='VERT')
            if bpy.context.tool_settings.mesh_select_mode[0] == False and bpy.context.tool_settings.mesh_select_mode[1] == True and bpy.context.tool_settings.mesh_select_mode[2] == False:
                bpy.ops.mesh.delete(type='EDGE')
            if bpy.context.tool_settings.mesh_select_mode[0] == False and bpy.context.tool_settings.mesh_select_mode[1] == False and bpy.context.tool_settings.mesh_select_mode[2] == True:
                bpy.ops.mesh.delete(type='FACE')
        return {"FINISHED"}


#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_QuickDelete)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_QuickDelete)

register()