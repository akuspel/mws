import bpy
from bpy.props import BoolProperty
from mathutils import *
D = bpy.data
C = bpy.context

# functions
def mirror(axis, self, context):

    mods = 0
    mod_nro = 0
    active_mod = ""

    mirror_mods = 0
    mirror_nro = 0
    active_mirror = ""
    mirror_pivot = ""
    
    for mod in context.active_object.modifiers:
        if mod.type == "MIRROR":
            mirror_mods += 1    

    if mirror_mods == 0:

        bpy.ops.object.modifier_add(type="MIRROR")
        
        for mod in context.active_object.modifiers:
            mods += 1
       
        for mod in context.active_object.modifiers:
            mod_nro += 1
            if mod_nro == mods:
                active_mod = mod.name
                
                if len(context.selected_objects) > 1:
                    for i in context.selected_objects:
                        if "MIRROR_PIVOT" in i.name:
                            mirror_pivot = i

                if mirror_pivot:
                    context.object.modifiers[active_mod].mirror_object = mirror_pivot
                
                else:
                    # World Space Mirror
                    if context.scene.tool_settings.transform_pivot_point == "CURSOR":
                        
                        if self.move_origin == False:
                            
                            active = context.active_object
                            bpy.ops.object.empty_add(type="ARROWS", location=(context.scene.cursor.location))

                            pivot_object = context.object
                            context.object.name = "MIRROR_PIVOT" + str(context.scene.cursor.location)

                            bpy.ops.object.select_all(action="TOGGLE")

                            context.view_layer.objects.active = active
                            bpy.data.objects[active.name].select_set(True)
                            
                            context.object.modifiers[active_mod].mirror_object = pivot_object
                        
                        else:
                            
                            active = context.active_object

                            bpy.ops.object.select_all(action="TOGGLE")

                            context.view_layer.objects.active = active
                            bpy.data.objects[active.name].select_set(True)

                            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
                        

                if self.use_clip == True:                           
                   context.object.modifiers[active_mod].use_clip = True
                
                if axis == "x":
                    context.object.modifiers[active_mod].use_axis[0] = True
                    context.object.modifiers[active_mod].use_axis[1] = False
                    context.object.modifiers[active_mod].use_axis[2] = False
                elif axis == "y":
                    context.object.modifiers[active_mod].use_axis[0] = False
                    context.object.modifiers[active_mod].use_axis[1] = True
                    context.object.modifiers[active_mod].use_axis[2] = False
                elif axis == "z":
                    context.object.modifiers[active_mod].use_axis[0] = False
                    context.object.modifiers[active_mod].use_axis[1] = False
                    context.object.modifiers[active_mod].use_axis[2] = True
    
    else:
        for mod in context.active_object.modifiers:
            if mod.type == "MIRROR":
                mirror_nro += 1
                if mirror_nro == 1:
                    active_mirror = mod.name
        
        if axis == "x":
            if context.object.modifiers[active_mirror].use_axis[0] == True:
                context.object.modifiers[active_mirror].use_axis[0] = False
            else:
                context.object.modifiers[active_mirror].use_axis[0] = True
        elif axis == "y":
            if context.object.modifiers[active_mirror].use_axis[1] == True:
                context.object.modifiers[active_mirror].use_axis[1] = False
            else:
                context.object.modifiers[active_mirror].use_axis[1] = True
        elif axis == "z":
            if context.object.modifiers[active_mirror].use_axis[2] == True:
                context.object.modifiers[active_mirror].use_axis[2] = False
            else:
                context.object.modifiers[active_mirror].use_axis[2] = True

def mirror_metaball(axis, context):
    
    active = context.active_object

    for ob in bpy.data.objects:
        if ob != active:
            bpy.data.objects[ob.name].select_set(False)

    bpy.ops.object.duplicate_move_linked()
    if axis == "x":
        bpy.ops.transform.resize(value=(-1, 1, 1))
    elif axis == "y":
        bpy.ops.transform.resize(value=(1, -1, 1))
    elif axis == "z":
        bpy.ops.transform.resize(value=(1, 1, -1))

    context.view_layer.objects.active = active
    bpy.data.objects[active.name].select_set(True)

    bpy.ops.object.parent_set(type="OBJECT")

    bpy.ops.object.select_all(action="TOGGLE")

    context.view_layer.objects.active = active
    bpy.data.objects[active.name].select_set(True)

# classes
class MWS_OT_MirrorX(bpy.types.Operator):

    bl_idname = "object.mirror_x"
    bl_label = "Mws Mirror X"
    bl_description = "Mirror X"
    bl_options = {"REGISTER", "UNDO"}

    move_origin: BoolProperty(
        name = "Move Origin",
        default = True,
        description = "move origin to cursor"
    )
    use_clip: BoolProperty(
        name = "Use Clip",
        default = True,
        description = "use mirror clipping"
    )

    def execute(self, context):
        
        if context.active_object.type == "META":
            mirror_metaball("x", context)
        else:
            mirror("x", self, context)
        
        return {"FINISHED"}

class MWS_OT_MirrorY(bpy.types.Operator):

    bl_idname = "object.mirror_y"
    bl_label = "Mws Mirror Y"
    bl_description = "Mirror Y"
    bl_options = {"REGISTER", "UNDO"}

    move_origin: BoolProperty(
        name = "Move Origin",
        default = True,
        description = "move origin to cursor"
    )
    use_clip: BoolProperty(
        name = "Use Clip",
        default = True,
        description = "use mirror clipping"
    )

    def execute(self, context):
        
        if context.active_object.type == "META":
            mirror_metaball("y", context)
        else:
            mirror("y", self, context)
        
        return {"FINISHED"}

class MWS_OT_MirrorZ(bpy.types.Operator):

    bl_idname = "object.mirror_z"
    bl_label = "Mws Mirror Z"
    bl_description = "Mirror Z"
    bl_options = {"REGISTER", "UNDO"}

    move_origin: BoolProperty(
        name = "Move Origin",
        default = True,
        description = "move origin to cursor"
    )
    use_clip: BoolProperty(
        name = "Use Clip",
        default = True,
        description = "use mirror clipping"
    )

    def execute(self, context):
        
        if context.active_object.type == "META":
            mirror_metaball("z", context)
        else:
            mirror("z", self, context)
        
        return {"FINISHED"}