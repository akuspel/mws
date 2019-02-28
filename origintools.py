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
                ob = bpy.context.object
                ob.update_from_editmode()

                me = ob.data
                verts_sel = [v.co for v in me.vertices if v.select]

                pivot = sum(verts_sel, Vector()) / len(verts_sel)

                print("Local:", pivot)
                print("Global:", ob.matrix_world * pivot)

                curx = bpy.context.scene.cursor_location.x
                cury = bpy.context.scene.cursor_location.y
                curz = bpy.context.scene.cursor_location.z

                bpy.context.scene.cursor_location = ob.matrix_world * pivot
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='TOGGLE')

                bpy.context.scene.cursor_location = (curx, cury, curz)
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
        bpy.context.scene.cursor_location.x = 0
        return {"FINISHED"}

class MWS_OT_ResetCursorY(bpy.types.Operator) : 
    bl_idname = "cursor.y"  
    bl_label = "Reset Cursor Y"  
    bl_options = {"REGISTER"} 

    def execute(self, context) :
        bpy.context.scene.cursor_location.y = 0
        return {"FINISHED"}

class MWS_OT_ResetCursorZ(bpy.types.Operator) : 
    bl_idname = "cursor.z"  
    bl_label = "Reset Cursor Z"  
    bl_options = {"REGISTER"} 

    def execute(self, context) :
        bpy.context.scene.cursor_location.z = 0
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