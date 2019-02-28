import bpy
from bpy.props import FloatProperty

class MWS_OT_Sharpen(bpy.types.Operator) :
    bl_idname = "mesh.mws_sharp"
    bl_label = "Sharpen Sharp Edges"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.edges_select_sharp(sharpness=0.785398)
            bpy.ops.mesh.mark_sharp()
            bpy.ops.transform.edge_bevelweight(value=1)
        return {"FINISHED"}

class MWS_OT_DissolveLoops(bpy.types.Operator) :
    bl_idname = "mesh.mws_dissolve_loops"
    bl_label = "Dissolve loops"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_mode(use_verts=True)
        return {"FINISHED"}

class MWS_OT_MarkSharp(bpy.types.Operator) :
    bl_idname = "mesh.mws_mark_sharp"
    bl_label = "Mark Sharp"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        bpy.ops.mesh.mark_sharp()
        bpy.ops.transform.edge_bevelweight(value=1)
        return {"FINISHED"}


#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_Sharpen)
    bpy.utils.register_class(MWS_OT_DissolveLoops)
    bpy.utils.register_class(MWS_OT_MarkSharp)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_Sharpen)
    bpy.utils.unregister_class(MWS_OT_DissolveLoops)
    bpy.utils.unregister_class(MWS_OT_MarkSharp)

register()