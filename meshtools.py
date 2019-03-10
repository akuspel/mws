import bpy

class MWS_OT_TriNgon(bpy.types.Operator) : 
    bl_idname = "mesh.tringon"  
    bl_label = "Ngon to Tri"  
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_face_by_sides(number=4, type='GREATER')
            bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
            bpy.ops.mesh.tris_convert_to_quads()
            bpy.ops.mesh.select_all(action="DESELECT")
        return {"FINISHED"}

class MWS_OT_QuickDecimate(bpy.types.Operator) : 
    bl_idname = "mesh.qdec"  
    bl_label = "Quick Decimate"  
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.decimate(ratio=0.1)
            bpy.ops.mesh.select_all(action='DESELECT')
        return {"FINISHED"}

class MWS_OT_ClearVertData(bpy.types.Operator) : 
    bl_idname = "mesh.vertd_clear"  
    bl_label = "Clear Vertex Data"  
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context) :
        try:
            for group in bpy.context.active_object.vertex_groups:
                bpy.context.active_object.vertex_groups.remove(group)
            for color in bpy.context.active_object.data.vertex_colors:    
                bpy.context.active_object.data.vertex_colors.remove(color)
            for uv in bpy.context.active_object.data.uv_textures:
                 bpy.ops.mesh.uv_texture_remove()
            #active_uv = bpy.context.active_object.data.uv_textures.active.name
            #bpy.ops.mesh.uv_texture_remove(active_uv)
        except:
            try:
                for group in bpy.context.active_object.vertex_groups:
                    bpy.context.active_object.vertex_groups.remove(group)
                for color in bpy.context.active_object.data.vertex_colors:    
                    bpy.context.active_object.data.vertex_colors.remove(color)
                for uv in bpy.context.active_object.data.uv_textures:
                     bpy.ops.mesh.uv_texture_remove()
            except:
                self.report({'WARNING'}, "Unable to complete action...")
        return {"FINISHED"}

class MWS_OT_ClearScene(bpy.types.Operator) :
    bl_idname = "scene.mws_clear"
    bl_label = "Clear Scene"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        bpy.ops.object.select_all(action='DESELECT')
        for object in bpy.data.objects:
            object.select_set(True)
            bpy.ops.object.delete(use_global=False)
        return {"FINISHED"}


#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_TriNgon)
    bpy.utils.register_class(MWS_OT_QuickDecimate)
    bpy.utils.register_class(MWS_OT_ClearVertData)
    bpy.utils.register_class(MWS_OT_ClearScene)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_TriNgon)
    bpy.utils.unregister_class(MWS_OT_QuickDecimate)
    bpy.utils.unregister_class(MWS_OT_ClearVertData)
    bpy.utils.unregister_class(MWS_OT_ClearScene)

register()