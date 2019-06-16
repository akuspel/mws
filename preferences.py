import bpy
import webbrowser
from . utils.addons import addon_exists


class MWS_OT_BevelrWeb(bpy.types.Operator) :
    bl_idname = "pref.bevelr"
    bl_label = "Get Bevelr Addon"

    def execute(self, context) :
        webbrowser.open("https://gumroad.com/l/bevelr")
        return {"FINISHED"}

class MWS_OT_LoopTools_en(bpy.types.Operator) :
    bl_idname = "pref.looptools"
    bl_label = "Enable Loop Tools"

    def execute(self, context) :
        bpy.ops.preferences.addon_enable(module = "mesh_looptools")
        self.report({'INFO'}, "Enabled addon Loop Tools")
        return {"FINISHED"}

class MWS_OT_ModTools_en(bpy.types.Operator) :
    bl_idname = "pref.modtools"
    bl_label = "Enable Modifier Tools"

    def execute(self, context) :
        bpy.ops.preferences.addon_enable(module = "space_view3d_modifier_tools")
        self.report({'INFO'}, "Enabled addon Modifier Tools")
        return {"FINISHED"}


#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_BevelrWeb)
    bpy.utils.register_class(MWS_OT_LoopTools_en)
    bpy.utils.register_class(MWS_OT_ModTools_en)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_BevelrWeb)
    bpy.utils.unregister_class(MWS_OT_LoopTools_en)
    bpy.utils.unregister_class(MWS_OT_ModTools_en)


register()