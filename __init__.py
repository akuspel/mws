'''
Copyright (C) 2018 AKU KETTUNEN
AKU.KETTUNEN@GMAIL.com

Created by AKU KETTUNEN

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "MWS",
    "author": "Aku Kettunen",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "3D View, SHIFT ALT Q",
    "description": "-model with speed-",
    "warning": "",
    "wiki_url": "",
    "category": "Mesh",
    }


import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty, FloatProperty
import webbrowser
from . utils.addons import addon_exists
import rna_keymap_ui
from . keymap import register_keymaps
import os, string, socket

class MWS_PT_Preferences(AddonPreferences):
    bl_idname = __name__

    quickEditors = BoolProperty(
            name="Enable Quick Operators (under construction)",
            default=False,
            )
    number = FloatProperty(
            name="Example Number",
            default=1,
            min=0,
            max=3
            )
    helpBoolean = BoolProperty(
            name="Help",
            default=False,
            )
    
    def draw(self, context):
        if addon_exists("penfinity_bevel"):
            bevlr_icon = "FILE_TICK"
        else:
            bevlr_icon = "ERROR"
        
        if addon_exists("mesh_looptools"):
            loopt_icon = "FILE_TICK"
        else:
            loopt_icon = "ERROR"
        
        if addon_exists("space_view3d_modifier_tools"):
            modt_icon = "FILE_TICK"
        else:
            modt_icon = "ERROR"
        
        layout = self.layout
        layout.label(text="Useful Addons")
        box = layout.split().column()
        row = box.row(align=True)
        row.operator("pref.bevelr", text="Bevelr", icon=bevlr_icon)
        row.operator("pref.looptools", text="Loop Tools", icon=loopt_icon)
        row.operator("pref.modtools", text="Modifier Tools", icon=modt_icon)
        layout.prop(self, "quickEditors")
        layout.prop(self, "helpBoolean")
        if self.helpBoolean == True:
            layout.label(text="Keymap:")
            layout.label(text="Mesh Editor Pie - Shift Alt Q")
            if self.quickEditors == True:
                layout.label(text="Quick Delete - X")
                layout.label(text="Quick Merge - Alt M")



# load and reload submodules
##################################

import importlib
from . import developer_utils
importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())



# register
##################################

import traceback

classes = ( MWS_PT_Preferences )

def register():
    from bpy.utils import register_class
    bpy.utils.register_class(MWS_PT_Preferences)

def unregister():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(MWS_PT_Preferences)

if __name__ == "__main__":
    register()


"""def register():
    try: bpy.utils.register_class(__name__)
    except: traceback.print_exc()
    register_keymaps()

    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))

def unregister():
    try: bpy.utils.unregister_class(__name__)
    except: traceback.print_exc()

    print("Unregistered {}".format(bl_info["name"]))"""
