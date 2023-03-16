import bpy

def booleanMod(operation, context):
    mods = 0
    mod_nro = 0
    active_mod = ""

    for object in context.selected_objects:
        if object != context.active_object:
            try:
                object.display_type = "WIRE"
                bpy.ops.object.modifier_add(type="BOOLEAN")
                for mod in bpy.context.active_object.modifiers:
                    mods += 1
                
                for mod in context.active_object.modifiers:
                    mod_nro += 1
                    if mod_nro == mods:
                        active_mod = mod.name
                        context.object.modifiers[active_mod].object = bpy.data.objects[object.name]
                        if operation == "Dif":
                            context.object.modifiers[active_mod].operation = "DIFFERENCE"
                        elif operation == "Union":
                            context.object.modifiers[active_mod].operation = "UNION"
                        elif operation == "Int":
                            context.object.modifiers[active_mod].operation = "INTERSECT"
            except:
                print("Unable to complete operation...")
                self.report({'WARNING'}, "Unable to complete operation...")

class MWS_OT_BooleanUnion(bpy.types.Operator):
    bl_idname = "object.mws_boolean_union"
    bl_label = "Boolean Union"
    bl_description = "Boolean Union"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        booleanMod("Union", context)
        return {"FINISHED"}

class MWS_OT_BooleanDif(bpy.types.Operator):
    bl_idname = "object.mws_boolean_dif"
    bl_label = "Boolean Difference"
    bl_description = "Boolean Difference"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        booleanMod("Dif", context)
        return {"FINISHED"}

class MWS_OT_BooleanInt(bpy.types.Operator):
    bl_idname = "object.mws_boolean_int"
    bl_label = "Boolean Intersect"
    bl_description = "Boolean Intersect"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        booleanMod("Int", context)
        return {"FINISHED"}