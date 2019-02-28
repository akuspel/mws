import bpy

class MWS_OT_bdiffSharp(bpy.types.Operator) : 
    bl_idname = "mesh.bdiffbevel"  
    bl_label = "Difference Bevel"
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.mesh.select_mode(type="VERT")
            bpy.ops.mesh.intersect_boolean(operation='DIFFERENCE', use_swap=False)
            bpy.ops.mesh.mark_sharp()
            bpy.ops.transform.edge_bevelweight(value=1)
        return {"FINISHED"}

class MWS_OT_bunSharp(bpy.types.Operator) : 
    bl_idname = "mesh.bunbevel"  
    bl_label = "Union Bevel"
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.mesh.select_mode(type="VERT")
            bpy.ops.mesh.intersect_boolean(operation='UNION', use_swap=False)
            bpy.ops.mesh.mark_sharp()
            bpy.ops.transform.edge_bevelweight(value=1)
        return {"FINISHED"}

#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_bdiffSharp)
    bpy.utils.register_class(MWS_OT_bunSharp)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_bdiffSharp)
    bpy.utils.unregister_class(MWS_OT_bunSharp)

register()