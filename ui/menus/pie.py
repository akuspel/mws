import bpy
from bpy.types import Menu
from ... utils.addons import addon_exists
from mathutils import *
D = bpy.data
C = bpy.context

class MWS_MT_PIE_MwsPie(Menu):

    # label is displayed at the center of the pie menu.
    bl_label = "Mesh Editor Pie"
    bl_idname = "MWS_MT_pie" 
    bl_description = "Mesh Editor Pie Menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        
        
        if len(context.selected_objects) == 0 and context.active_object == None:
            #LEFT
            box = pie.split().column()
            row = box.split(align=True)
            row.operator("ed.undo_history", text="History", icon="LOOP_BACK")
            row = box.row(align=True)
            row.operator("screen.redo_last", text="       F6")
            
            #RIGHT
            pie.separator()
            
            #BOTTOM
            box = pie.split().column()
            row = box.row(align=True)
            row.operator("mesh.primitive_cube_add", text="", icon="MESH_CUBE")
            row.operator("mesh.primitive_plane_add", text="", icon="MESH_PLANE")
            row.operator("mesh.primitive_cylinder_add", text="", icon="MESH_CYLINDER")
            row.operator("mesh.primitive_uv_sphere_add", text="", icon="MESH_UVSPHERE")
            
            #TOP
            box = pie.split().column()
            row = box.split(align=True)
            row.operator("scene.mws_clear", text="Clear Scene")
            
            #TOP-LEFT
            box = pie.split().column()
            row = box.row()
            row.label(text="Reset cursor")
            row = box.row(align=True)
            row.operator("cursor.x", text="X")
            #row = box.row(align=True)
            row.operator("cursor.y", text="Y")
            #row = box.row(align=True)
            row.operator("cursor.z", text="Z")
            
            #TOP-RIGHT
            pie.separator()
            
            #BOTTOM-LEFT   
            pie.separator()
            
            #BOTTOM-RIGHT
        
        if context.active_object.mode == "EDIT":
            #LEFT
            box = pie.split().column()
            row = box.split(align=True)
            row.operator("ed.undo_history", text="History", icon="LOOP_BACK")
            row = box.row(align=True)
            row.operator("screen.redo_last", text="       F6")
            
            #RIGHT        
            box = pie.split().column()
            row = box.row(align=True)
            row.operator("mesh.mark_sharp", text="", icon="CHECKMARK")
            row.operator("mesh.clear_sharp", text="", icon="X")
            row.operator("object.auto_smooth_sharpen", text="Auto Mark", icon="AUTO")
            if tuple(context.scene.tool_settings.mesh_select_mode)[1] == True:
                row = box.row(align=True)
                row.operator("mesh.dissolve_loops", text="Dissolve Loops", icon="SNAP_EDGE")
            row = box.row(align=True)
            row.operator("mesh.origin_to_selected", text="O - Sel", icon="KEYTYPE_BREAKDOWN_VEC")
            row.operator("mesh.origin_to_geometry", text="O - Geo", icon="KEYTYPE_BREAKDOWN_VEC")
            row = box.row(align=True)
            
            
            #BOTTOM
            pie.operator("mws.call_tools", text="More")
            
            #TOP
            box = pie.split().column()
            row = box.split(align=True)
            row.operator("mesh.ngon_to_tri", text="Ngon", icon="MOD_TRIANGULATE")
            
            #TOP-LEFT
            box = pie.split().column()
            row = box.row()
            row.label(text="Reset cursor")
            row = box.row(align=True)
            row.operator("cursor.x", text="X")
            #row = box.row(align=True)
            row.operator("cursor.y", text="Y")
            #row = box.row(align=True)
            row.operator("cursor.z", text="Z")
            
            #TOP-RIGHT
            box = pie.split().column()
            row = box.row()
            row.operator("mesh.intersect_boolean", text="Boolean", icon="MOD_BOOLEAN")
            
            #BOTTOM-LEFT
            box = pie.split().column()
            row = box.row(align=True)
            row.operator("mesh.primitive_cube_add", text="", icon="MESH_CUBE")
            row.operator("mesh.primitive_plane_add", text="", icon="MESH_PLANE")
            row.operator("mesh.primitive_cylinder_add", text="", icon="MESH_CYLINDER")
            row.operator("mesh.primitive_uv_sphere_add", text="", icon="MESH_UVSPHERE")
            
            #BOTTOM-RIGHT
            box = pie.split().column()
            row = box.split(align=True)
            row = box.row(align=True)
            row.operator("object.modifier_add", text="Add Modifier", icon="MODIFIER")
            
        elif context.active_object.mode == "OBJECT":
            #LEFT
            box = pie.split().column()
            row = box.split(align=True)
            row.operator("ed.undo_history", text="History", icon="LOOP_BACK")
            row = box.row(align=True)
            row.operator("screen.redo_last", text="       F6")
            
            #RIGHT
            box = pie.split().column()
            row = box.row(align=True)
            row.operator("object.mirror_x", text="X", icon="MOD_MIRROR")
            row.operator("object.mirror_y", text="Y", icon="MOD_MIRROR")
            row.operator("object.mirror_z", text="Z", icon="MOD_MIRROR")
            row = box.row(align=True)
            row.operator("object.auto_smooth_sharpen", text="Auto Mark Sharp")
            row.operator("object.shade_smooth_sharp", text="Shade Smooth")
            
            #BOTTOM
            pie.separator()
            
            #TOP
            pie.separator()
            
            #TOP-LEFT
            box = pie.split().column()
            row = box.row()
            row.label(text="Reset cursor")
            row = box.row(align=True)
            row.operator("cursor.x", text="X")
            #row = box.row(align=True)
            row.operator("cursor.y", text="Y")
            #row = box.row(align=True)
            row.operator("cursor.z", text="Z")
            
            #TOP-RIGHT
            box = pie.split().column()
            row = box.row(align=True)
            row.operator("object.mws_boolean_dif", text="Diff", icon="MOD_BOOLEAN")
            row.operator("object.mws_boolean_union", text="Union", icon="MOD_BOOLEAN")
            row.operator("object.mws_boolean_int", text="Int", icon="MOD_BOOLEAN")
            
            #BOTTOM-LEFT
            box = pie.split().column()
            row = box.row(align=True)
            row.operator("mesh.primitive_cube_add", text="", icon="MESH_CUBE")
            row.operator("mesh.primitive_plane_add", text="", icon="MESH_PLANE")
            row.operator("mesh.primitive_cylinder_add", text="", icon="MESH_CYLINDER")
            row.operator("mesh.primitive_uv_sphere_add", text="", icon="MESH_UVSPHERE")
            
            #BOTTOM-RIGHT
            box = pie.split().column()
            row = box.split(align=True)
            row = box.row(align=True)
            row.operator("object.modifier_add", text="Add Modifier", icon="MODIFIER")
            row = box.row(align=True)
            row.operator("object.convert", text="Convert To", icon="IMPORT")


class MWS_MT_PIE_ToolPie(Menu):

    bl_label = "Tool Pie"
    bl_idname = "MWS_MT_toolpie"
    bl_description = "MWS Tool Pie Menu"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        
        #LEFT
        box = pie.split().column()
        row = box.split(align=True)
        row.operator("mesh.knife_project", text="Project", icon="LINE_DATA")
        row.operator("mesh.intersect", text="Cut")
        
        
        #RIGHT
        box = pie.split().column()
        row = box.split(align=True)
        row.operator("mesh.symmetrize", text="Symmetrize")
        row.operator("mesh.select_mirror", text="Select Mirror", icon="UV_SYNC_SELECT")
        
        #BOTTOM
        if addon_exists("mesh_looptools"):
            box = pie.split().column()
            row = box.split(align=True)
            row.label(text="Loop Tools:")
            row= box.row(align=True)
            row.operator("mesh.looptools_circle", text="Circle", icon="MESH_CIRCLE")
            row.operator("mesh.looptools_flatten", text="Flatten", icon="MESH_PLANE")
        else:
            pie.separator()
        
        #TOP
        pie.operator("mws.call_merge", text="Merge")
        
        #TOP-LEFT
        pie.separator()
        
        #TOP-RIGHT
        pie.separator()
        
        #BOTTOM-LEFT
        box = pie.split().column()
        row = box.split(align=True)
        row.operator("mesh.offset_edge_loops_slide", text="Split Slide", icon="EDGESEL")
        
        #BOTTOM-RIGHT
        box = pie.split().column()
        row = box.split(align=True)
        row.operator("mesh.fill_grid", text="Grid Fill", icon="MESH_GRID")
        row.operator("mesh.bridge_edge_loops", text="Bridge", icon="SPHERECURVE")

class MWS_MT_PIE_edit_mesh_merge(Menu):
    
    # label is displayed at the center of the pie menu.
    bl_label = "Merge"
    bl_idname = "MWS_MT_mergepie"
    bl_description = "Merge Pie Menu"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        
        # main merge options
        pie.operator_enum("mesh.merge", "type")
        
        # merge by distance
        pie.operator("mesh.remove_doubles")