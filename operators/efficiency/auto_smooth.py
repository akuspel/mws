import bpy
from mathutils import *
D = bpy.data
C = bpy.context


class MWS_OT_AutoSmoothSharpen(bpy.types.Operator):

    bl_idname = "object.auto_smooth_sharpen"
    bl_label = "Auto Smooth Sharpen"
    bl_description = "Mark Auto Smooth Edges as Sharp"
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context):

        """ Selects sharp edges based on auto smooth angle,
        and marks them as sharp. """

        # loop through selected objects
        for object in context.selected_objects:
            
            # set active object
            context.view_layer.objects.active = object

            if object.type == "MESH":
                if object.data.use_auto_smooth == True:

                    # toggle editmode
                    if context.active_object.mode == "EDIT":
                        bpy.ops.object.editmode_toggle()
                    
                    # get auto smooth angle
                    angle = context.active_object.data.auto_smooth_angle

                    # select only active
                    bpy.ops.object.select_all(action = "DESELECT")
                    context.selected_objects.append(context.active_object)

                    # toggle editmode
                    bpy.ops.object.editmode_toggle()

                    # deselect all verts
                    bpy.ops.mesh.select_all(action = "DESELECT")

                    # select by angle
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type="EDGE")
                    bpy.ops.mesh.edges_select_sharp(sharpness = angle)

                    # mark sharp
                    bpy.ops.mesh.mark_sharp()

                    # toggle out of edit mode
                    bpy.ops.object.editmode_toggle()

        return {"FINISHED"}

class MWS_OT_ShadeSmoothSharp(bpy.types.Operator):

    bl_idname = "object.shade_smooth_sharp"
    bl_label = "Shade Smooth with Auto Smooth"
    bl_description = "Shade Smooth without changing Auto Smooth status"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        if len(context.selected_objects) > 0:

            # save list of selected objects into a variable
            selected = context.selected_objects

            # loop through objects
            for obj in selected:

                # select each object individually
                context.selected_objects.clear()
                context.selected_objects.append(obj)

                # get auto smooth angle
                angle = obj.data.auto_smooth_angle

                # shade smooth
                bpy.ops.object.shade_smooth(use_auto_smooth=True, auto_smooth_angle=angle)
            
            # select everything again
            for obj in selected:
                obj.select_set(True)
        
        return {"FINISHED"}

class MWS_OT_ClearSharp(bpy.types.Operator):

    bl_idname = "mesh.clear_sharp"
    bl_label = "Clear Sharp"
    bl_description = "Clear Sharp Edges"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        bpy.ops.mesh.mark_sharp(clear=True)
        
        return {"FINISHED"}