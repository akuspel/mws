import bpy
import bmesh
from mathutils import Vector

class MWS_OT_OriginToSelected(bpy.types.Operator) : 
    bl_idname = "mesh.selor"
    bl_label = "Origin to Selected"
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            obj = bpy.context.active_object
            if bpy.context.mode == 'EDIT_MESH':
                bm = bmesh.from_edit_mesh(obj.data)
                verts = [ v.index for v in bm.verts if v.select ]
            else:
                verts = [ v.index for v in obj.data.vertices if v.select ]

            if len(verts) > 0:
                curx = bpy.context.scene.cursor.location[0]
                cury = bpy.context.scene.cursor.location[1]
                curz = bpy.context.scene.cursor.location[2]

                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='TOGGLE')

                bpy.context.scene.cursor.location = (curx, cury, curz)
            else:
                self.report({'WARNING'}, "Nothing selected")
        return {"FINISHED"}

class MWS_OT_OriginToGeometry(bpy.types.Operator) : 
    bl_idname = "mesh.orge"  
    bl_label = "Origin to Geometry"  
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context) :
        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='DESELECT')
        return {"FINISHED"}

class MWS_OT_ResetCursorX(bpy.types.Operator) : 
    bl_idname = "cursor.x"  
    bl_label = "Reset Cursor X"  
    bl_options = {"REGISTER"} 

    def execute(self, context) :
        bpy.context.scene.cursor.location[0] = 0
        return {"FINISHED"}

class MWS_OT_ResetCursorY(bpy.types.Operator) : 
    bl_idname = "cursor.y"  
    bl_label = "Reset Cursor Y"  
    bl_options = {"REGISTER"} 

    def execute(self, context) :
        bpy.context.scene.cursor.location[1] = 0
        return {"FINISHED"}

class MWS_OT_ResetCursorZ(bpy.types.Operator) : 
    bl_idname = "cursor.z"  
    bl_label = "Reset Cursor Z"  
    bl_options = {"REGISTER"} 

    def execute(self, context) :
        bpy.context.scene.cursor.location[2] = 0
        return {"FINISHED"}


#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_OriginToSelected)
    bpy.utils.register_class(MWS_OT_OriginToGeometry)
    bpy.utils.register_class(MWS_OT_ResetCursorX)
    bpy.utils.register_class(MWS_OT_ResetCursorY)
    bpy.utils.register_class(MWS_OT_ResetCursorZ)


def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_OriginToSelected)
    bpy.utils.unregister_class(MWS_OT_OriginToGeometry)
    bpy.utils.unregister_class(MWS_OT_ResetCursorX)
    bpy.utils.unregister_class(MWS_OT_ResetCursorY)
    bpy.utils.unregister_class(MWS_OT_ResetCursorZ)


register()