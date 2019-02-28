import bpy

def booleanMod(operation):
    mods = 0
    mod_nro = 0
    active_mod = ""

    for object in bpy.context.selected_objects:
        if object == bpy.context.active_object:
            print("active")
        else:
            try:
                object.display_type = "WIRE"
                bpy.ops.object.modifier_add(type="BOOLEAN")
                for mod in bpy.context.active_object.modifiers:
                    mods += 1
                print(mods)
                for mod in bpy.context.active_object.modifiers:
                    mod_nro += 1
                    if mod_nro == mods:
                        active_mod = mod.name
                        bpy.context.object.modifiers[active_mod].object = bpy.data.objects[object.name]
                        if operation == "Dif":
                            bpy.context.object.modifiers[active_mod].operation = "DIFFERENCE"
                        elif operation == "Union":
                            bpy.context.object.modifiers[active_mod].operation = "UNION"
                        elif operation == "Int":
                            bpy.context.object.modifiers[active_mod].operation = "INTERSECT"
            except:
                print("Unable to complete operation...")
                self.report({'WARNING'}, "Unable to complete operation...")

class MWS_OT_BooleanUnion(bpy.types.Operator) :
    bl_idname = "object.mws_boolean_union"
    bl_label = "Boolean Union"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        booleanMod("Union")
        return {"FINISHED"}

class MWS_OT_BooleanDif(bpy.types.Operator) :
    bl_idname = "object.mws_boolean_dif"
    bl_label = "Boolean Difference"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        booleanMod("Dif")
        return {"FINISHED"}

class MWS_OT_BooleanInt(bpy.types.Operator) :
    bl_idname = "object.mws_boolean_int"
    bl_label = "Boolean Intersect"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context) :
        booleanMod("Int")
        return {"FINISHED"}

#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_BooleanUnion)
    bpy.utils.register_class(MWS_OT_BooleanDif)
    bpy.utils.register_class(MWS_OT_BooleanInt)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_BooleanUnion)
    bpy.utils.unregister_class(MWS_OT_BooleanDif)
    bpy.utils.unregister_class(MWS_OT_BooleanInt)

register()