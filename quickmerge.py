import bpy

class MWS_OT_QuickMerge(bpy.types.Operator) :
    bl_idname = "mesh.quickmerge"
    bl_label = "Quick Merge"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.mesh.merge(type='CENTER')
        return {"FINISHED"}

#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_QuickMerge)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_QuickMerge)

register()