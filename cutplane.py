import bpy

import bpy
from bpy.props import FloatProperty

class MWS_OT_CutPlane(bpy.types.Operator) :
    bl_idname = "object.cutplane"
    bl_label = "Cut Plane"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        if bpy.context.object.mode == "OBJECT":
            obj_a = bpy.context.active_object.name
            obj_a_ = bpy.context.active_object
            bpy.ops.mesh.primitive_plane_add(size = 100)
            obj_b = bpy.context.active_object.name
            obj_b_ = bpy.context.active_object
            bpy.data.objects[obj_a].select_set(True)
            bpy.context.view_layer.objects.active = obj_a_
            bpy.ops.object.mws_boolean_dif()

            mod_nro = 0
            mods = len(bpy.context.active_object.modifiers)
            mod_name = ""

            for mod in bpy.context.active_object.modifiers:
                mod_nro += 1
                if mod_nro == mods:
                    mod_name = mod.name

            bpy.ops.object.select_all(action='TOGGLE')
            bpy.context.view_layer.objects.active = obj_b_
            bpy.data.objects[obj_b].select_set(True)
            bpy.ops.transform.rotate("INVOKE_DEFAULT")
        return {"FINISHED"}