import bpy
from bpy.props import IntProperty, FloatProperty, StringProperty

def mirror(axis):
    mods = 0
    mod_nro = 0
    active_mod = ""

    mirror_mods = 0
    mirror_nro = 0
    active_mirror = ""
    
    for mod in bpy.context.active_object.modifiers:
        if mod.type == "MIRROR":
            mirror_mods += 1
        else:
            print("no")

    if mirror_mods == 0:
        bpy.ops.object.modifier_add(type='MIRROR')
        for mod in bpy.context.active_object.modifiers:
            mods += 1
        print(mods)
        for mod in bpy.context.active_object.modifiers:
            mod_nro += 1
            if mod_nro == mods:
                active_mod = mod.name
                
                #World Space Mirror
                if bpy.context.scene.tool_settings.transform_pivot_point == "CURSOR":
                    active = bpy.context.active_object
                    bpy.ops.object.empty_add(type='ARROWS', location=(bpy.context.scene.cursor.location))

                    pivot_object = bpy.context.object
                    bpy.context.object.name = "MIRROR_PIVOT" + str(bpy.context.scene.cursor.location)

                    bpy.ops.object.select_all(action='TOGGLE')

                    bpy.context.view_layer.objects.active = active
                    bpy.data.objects[active.name].select_set(True)
                    
                    bpy.context.object.modifiers[active_mod].mirror_object = pivot_object
                    
                else:
                    bpy.context.object.modifiers[active_mod].use_clip = True
                
                if axis == "x":
                    bpy.context.object.modifiers[active_mod].use_axis[0] = True
                    bpy.context.object.modifiers[active_mod].use_axis[1] = False
                    bpy.context.object.modifiers[active_mod].use_axis[2] = False
                elif axis == "y":
                    bpy.context.object.modifiers[active_mod].use_axis[0] = False
                    bpy.context.object.modifiers[active_mod].use_axis[1] = True
                    bpy.context.object.modifiers[active_mod].use_axis[2] = False
                elif axis == "z":
                    bpy.context.object.modifiers[active_mod].use_axis[0] = False
                    bpy.context.object.modifiers[active_mod].use_axis[1] = False
                    bpy.context.object.modifiers[active_mod].use_axis[2] = True
    else:
        for mod in bpy.context.active_object.modifiers:
            if mod.type == "MIRROR":
                mirror_nro += 1
                if mirror_nro == 1:
                    active_mirror = mod.name
        if axis == "x":
            if bpy.context.object.modifiers[active_mirror].use_axis[0] == True:
                bpy.context.object.modifiers[active_mirror].use_axis[0] = False
            else:
                bpy.context.object.modifiers[active_mirror].use_axis[0] = True
        elif axis == "y":
            if bpy.context.object.modifiers[active_mirror].use_axis[1] == True:
                bpy.context.object.modifiers[active_mirror].use_axis[1] = False
            else:
                bpy.context.object.modifiers[active_mirror].use_axis[1] = True
        elif axis == "z":
            if bpy.context.object.modifiers[active_mirror].use_axis[2] == True:
                bpy.context.object.modifiers[active_mirror].use_axis[2] = False
            else:
                bpy.context.object.modifiers[active_mirror].use_axis[2] = True

def mirror_metaball(axis):
    
    active = bpy.context.active_object

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

    bpy.context.view_layer.objects.active = active
    bpy.data.objects[active.name].select_set(True)

    bpy.ops.object.parent_set(type='OBJECT')

    bpy.ops.object.select_all(action='TOGGLE')

    bpy.context.view_layer.objects.active = active
    bpy.data.objects[active.name].select_set(True)

class MWS_OT_MirrorX(bpy.types.Operator):
    bl_idname = "object.mirror_x"
    bl_label = "Mws Mirror X"
    bl_description = ""
    bl_options = {"REGISTER"}

    def execute(self, context):
        try:
            if bpy.context.active_object.type == "META":
                mirror_metaball("x")
            else:
                mirror("x")
        except:
            print("Unable to complete Mirror operation")
            self.report({'WARNING'}, "Unable to complete action...")
        return {"FINISHED"}

class MWS_OT_MirrorY(bpy.types.Operator):
    bl_idname = "object.mirror_y"
    bl_label = "Mws Mirror Y"
    bl_description = ""
    bl_options = {"REGISTER"}

    def execute(self, context):
        try:
            if bpy.context.active_object.type == "META":
                mirror_metaball("y")
            else:
                mirror("y")
        except:
            print("Unable to complete Mirror operation")
            self.report({'WARNING'}, "Unable to complete action...")
        return {"FINISHED"}

class MWS_OT_MirrorZ(bpy.types.Operator):
    bl_idname = "object.mirror_z"
    bl_label = "Mws Mirror Z"
    bl_description = ""
    bl_options = {"REGISTER"}

    def execute(self, context):
        try:
            if bpy.context.active_object.type == "META":
                mirror_metaball("z")
            else:
                mirror("z")
        except:
            print("Unable to complete Mirror operation")
            self.report({'WARNING'}, "Unable to complete action...")
        return {"FINISHED"}

bevels = []

class MWS_OT_BevelModal(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "object.mws_bevel_modal"
    bl_label = "Edit Bevel"

    first_mouse_x = IntProperty()
    first_value = FloatProperty()
    first_seg = IntProperty()
    first_limit = StringProperty()

    def modal(self, context, event):
        
        global bevels
        
        if event.type == 'MOUSEMOVE':
            delta = self.first_mouse_x - event.mouse_x
            bpy.context.object.modifiers[bevels[0]].width = self.first_value + delta * -0.002
        
        elif event.type == 'WHEELUPMOUSE':
            bpy.context.object.modifiers[bevels[0]].segments += 1
        
        elif event.type == 'WHEELDOWNMOUSE':
            bpy.context.object.modifiers[bevels[0]].segments -= 1
        
        elif event.type == 'MIDDLEMOUSE':
            bpy.ops.object.modifier_move_down(modifier = bevels[0])
        
        elif event.type == 'W':
            bpy.context.object.modifiers[bevels[0]].limit_method = "WEIGHT"
        
        elif event.type == 'A':
            bpy.context.object.modifiers[bevels[0]].limit_method = "ANGLE"
        
        elif event.type == 'LEFTMOUSE':
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.context.object.modifiers[bevels[0]].width = self.first_value
            bpy.context.object.modifiers[bevels[0]].segments = self.first_seg
            bpy.context.object.modifiers[bevels[0]].limit_method = self.first_limit
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        
        global bevels
        bevels = []

        for mod in bpy.context.object.modifiers:
            if mod.type == "BEVEL":
                bevels.append(mod.name)
        
        if len(bevels) == 0:
            bpy.ops.object.modifier_add(type='BEVEL')
            for mod in bpy.context.object.modifiers:
                if mod.type == "BEVEL":
                    bevels.append(mod.name)
            bpy.context.object.modifiers[bevels[0]].limit_method = 'ANGLE'
            bpy.context.object.modifiers[bevels[0]].use_clamp_overlap = False

        
        print(bevels)
        
        if context.object:
            self.first_mouse_x = event.mouse_x
            self.first_value = bpy.context.object.modifiers[bevels[0]].width
            self.first_seg = bpy.context.object.modifiers[bevels[0]].segments
            self.first_limit = bpy.context.object.modifiers[bevels[0]].limit_method

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}


#Registering

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_OT_MirrorX)
    bpy.utils.register_class(MWS_OT_MirrorY)
    bpy.utils.register_class(MWS_OT_MirrorZ)
    bpy.utils.register_class(MWS_OT_BevelModal)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_OT_MirrorX)
    bpy.utils.unregister_class(MWS_OT_MirrorY)
    bpy.utils.unregister_class(MWS_OT_MirrorZ)
    bpy.utils.unregister_class(MWS_OT_BevelModal)

register()