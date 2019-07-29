import bpy
from bpy.types import Menu
from . utils.addons import addon_exists


class MWS_PIE_mwspie(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Mesh Editor Pie"
    bl_idname = "mwse_pie"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        
        
        if len(bpy.context.selected_objects) == 0 and bpy.context.active_object == None:
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
        
        elif bpy.context.object.mode == "EDIT":
            #LEFT
            box = pie.split().column()
            row = box.split(align=True)
            row.operator("ed.undo_history", text="History", icon="LOOP_BACK")
            row = box.row(align=True)
            row.operator("screen.redo_last", text="       F6")
            
            #RIGHT        
            box = pie.split().column()
            row = box.split(align=True)
            try:
                row.operator("penfinity.smart_bevel", text="P Bevel", icon='MOD_BEVEL')
            except:
                print("Penfinity Bevel not enabled")
            if tuple(bpy.context.scene.tool_settings.mesh_select_mode)[1] == True:
                row = box.row(align=True)
                row.operator("mesh.mws_dissolve_loops", text="Dissolve Loops", icon='SNAP_EDGE')
            row = box.row(align=True)
            row.operator("mesh.mws_mark_sharp", text="Mark Sharp")
            row.operator("mesh.mws_sharp", text="Sharp")
            row = box.row(align=True)
            row.operator("mesh.selor", text="O - sel", icon='KEYTYPE_BREAKDOWN_VEC')
            row.operator("mesh.orge", text="O- Geo", icon='KEYTYPE_BREAKDOWN_VEC')
            row = box.row(align=True)
            
            
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
            row.operator("mesh.vertd_clear", text="Clear Vertex Data")
            row = box.row(align=True)
            row.operator("mesh.qdec", text="   ", icon='MOD_DECIM')
            row.operator("mesh.tringon", text="Ngon", icon='MOD_TRIANGULATE')
            
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
            row.operator("mesh.bdiffbevel", text="Difference", icon="MOD_BOOLEAN")
            row = box.row(align=True)
            row.operator("mesh.bunbevel", text="Union", icon="MOD_BOOLEAN")
            
            #BOTTOM-LEFT
            pie.operator("mws.call_tools", text="More")
            
            #BOTTOM-RIGHT
            box = pie.split().column()
            row = box.split(align=True)
            row = box.row(align=True)
            row.operator("object.modifier_add", text="Add Modifier", icon='MODIFIER')
            row = box.row(align=True)
            try:
                row.operator("object.delete_all_modifiers", text="Delete All", icon='X')
            except:
                print("Modifier Tool not enabled")
            
        elif bpy.context.object.mode == "OBJECT":
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
            row.operator("object.mws_bevel_modal", text="Edit Bevel", icon="MOD_BEVEL")
            
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
            row.operator("mesh.vertd_clear", text="Clear Vertex Data")
            row = box.row(align=True)
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
            box = pie.split().column()
            row = box.split(align=True)
            row.operator("object.mws_boolean_dif", text="Diff", icon='MOD_BOOLEAN')
            row = box.row(align=True)
            row.operator("object.mws_boolean_union", text="Union", icon='MOD_BOOLEAN')
            row = box.row(align=True)
            row.operator("object.mws_boolean_int", text="Int", icon='MOD_BOOLEAN')
            
            #BOTTOM-LEFT
            pie.separator()
            
            #BOTTOM-RIGHT
            box = pie.split().column()
            row = box.split(align=True)
            row = box.row(align=True)
            row.operator("object.modifier_add", text="Add Modifier", icon='MODIFIER')
            row = box.row(align=True)
            try:
                row.operator("object.apply_all_modifiers", text="Apply All", icon='IMPORT')
                row.operator("object.delete_all_modifiers", text="Delete All", icon='X')
            except:
                print("Modifier Tool not enabled")


class MWS_PIE_toolpie(Menu):
    bl_label = "Tool Pie"
    bl_idname = "mws_tool_pie"

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
        row.operator("mesh.select_mirror", text="Select Mirror", icon='UV_SYNC_SELECT')
        
        #BOTTOM
        if addon_exists("mesh_looptools"):
            box = pie.split().column()
            row = box.split(align=True)
            row.label(text="Loop Tools:")
            row= box.row(align=True)
            row.operator("mesh.looptools_circle", text="Circle", icon='MESH_CIRCLE')
            row.operator("mesh.looptools_flatten", text="Flatten", icon='MESH_PLANE')
            row= box.row(align=True)
            row.menu("wm.search_menu", text="Search", icon="VIEWZOOM")
        else:
            print("unable to load addon looptools")
            pie.separator()
        
        #TOP
        pie.operator("mesh.distance_fill", text="Cursor Fill")
        
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
        row.operator("mesh.fill_grid", text="Grid Fill", icon='MESH_GRID')
        row.operator("mesh.bridge_edge_loops", text="Bridge", icon='SPHERECURVE')


def register():
    bpy.utils.register_class(MWS_PIE_mwspie)
    bpy.utils.register_class(MWS_PIE_toolpie)


def unregister():
    bpy.utils.unregister_class(MWS_PIE_mwspie)
    bpy.utils.unregister_class(MWS_PIE_toolpie)



register()