import bpy, bmesh
from bpy.props import BoolProperty
from mathutils import *
D = bpy.data
C = bpy.context

class MWS_OT_Tringon(bpy.types.Operator): 

    bl_idname = "mesh.ngon_to_tri"
    bl_label = "Ngon to Tri"
    bl_description = "Convert nGons to Tris"
    bl_options = {"REGISTER", "UNDO"}

    to_quads: BoolProperty(
        name = "To Quads",
        default = True,
        description = "convert to quads where possible"
    )

    def execute(self, context):

        if context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_face_by_sides(number=4, type="GREATER")
            bpy.ops.mesh.quads_convert_to_tris(quad_method="BEAUTY", ngon_method="BEAUTY")
            
            if self.to_quads == True:
                bpy.ops.mesh.tris_convert_to_quads()
            
            bpy.ops.mesh.select_all(action="DESELECT")

        return {"FINISHED"}

class MWS_OT_DissoveLoops(bpy.types.Operator): 

    bl_idname = "mesh.dissolve_loops"  
    bl_label = "Dissolve Loops"
    bl_description = "Dissolve Edge Loops"
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context):

        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type="EDGE")
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_mode(use_verts=True)

        return {"FINISHED"}

class MWS_OT_OriginToSelected(bpy.types.Operator):

    bl_idname = "mesh.origin_to_selected"
    bl_label = "Origin to Selected"
    bl_description = "Set Origin to Selection"
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context):

        if context.active_object.mode == "EDIT":

            obj = context.active_object

            if context.active_object.mode == "EDIT":
                bm = bmesh.from_edit_mesh(obj.data)
                verts = [ v.index for v in bm.verts if v.select ]
            
            else:
                verts = [ v.index for v in obj.data.vertices if v.select ]

            if len(verts) > 0:

                curx = context.scene.cursor.location[0]
                cury = context.scene.cursor.location[1]
                curz = context.scene.cursor.location[2]

                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action="TOGGLE")

                context.scene.cursor.location = (curx, cury, curz)
            
            else:
                self.report({"WARNING"}, "Nothing selected")
        
        return {"FINISHED"}

class MWS_OT_OriginToGeometry(bpy.types.Operator): 
    bl_idname = "mesh.origin_to_geometry"  
    bl_label = "Origin to Geometry"
    bl_description = "Set Origin to Geometry"
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context):
        
        if context.active_object.mode == "EDIT":
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY")
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action="DESELECT")
        
        return {"FINISHED"}