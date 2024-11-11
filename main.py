import bpy

bl_info = {
    "name": "NameSync",
    "author": "Nanosize",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > UI > NameSync",
    "description": "Sync object names with their mesh data names",
    "category": "Object",
}

class OBJECT_OT_sync_names(bpy.types.Operator):
    bl_idname = "object.sync_names"
    bl_label = "Sync Object Names with Mesh Data"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        for obj in scene.objects:
            if obj.type == 'MESH' and scene.apply_mesh:
                obj.data.name = obj.name
            elif obj.type == 'CAMERA' and scene.apply_camera:
                obj.data.name = obj.name
            elif obj.type == 'LIGHT' and scene.apply_light:
                obj.data.name = obj.name
            elif obj.type == 'CURVE' and scene.apply_curve:
                obj.data.name = obj.name
            elif obj.type == 'SURFACE' and scene.apply_surface:
                obj.data.name = obj.name
            elif obj.type == 'LATTICE' and scene.apply_lattice:
                obj.data.name = obj.name
        return {'FINISHED'}

class OBJECT_PT_sync_panel(bpy.types.Panel):
    bl_label = "Sync Panel"
    bl_idname = "OBJECT_PT_sync_panel_v2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NameSync"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "apply_mesh", text="Mesh", icon='MESH_DATA')
        layout.prop(scene, "apply_camera", text="Camera", icon='CAMERA_DATA')
        layout.prop(scene, "apply_light", text="Light", icon='LIGHT_DATA')
        layout.prop(scene, "apply_curve", text="Curve", icon='CURVE_DATA')
        layout.prop(scene, "apply_surface", text="Surface", icon='SURFACE_DATA')
        layout.prop(scene, "apply_lattice", text="Lattice", icon='LATTICE_DATA')
        layout.separator()
        layout.operator(OBJECT_OT_sync_names.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_sync_names)
    bpy.utils.register_class(OBJECT_PT_sync_panel)

    bpy.types.Scene.apply_mesh = bpy.props.BoolProperty(name="Mesh", default=True)
    bpy.types.Scene.apply_camera = bpy.props.BoolProperty(name="Camera", default=False)
    bpy.types.Scene.apply_light = bpy.props.BoolProperty(name="Light", default=False)
    bpy.types.Scene.apply_curve = bpy.props.BoolProperty(name="Curve", default=False)
    bpy.types.Scene.apply_surface = bpy.props.BoolProperty(name="Surface", default=False)
    bpy.types.Scene.apply_lattice = bpy.props.BoolProperty(name="Lattice", default=False)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_sync_names)
    bpy.utils.unregister_class(OBJECT_PT_sync_panel)

    del bpy.types.Scene.apply_mesh
    del bpy.types.Scene.apply_camera
    del bpy.types.Scene.apply_light
    del bpy.types.Scene.apply_curve
    del bpy.types.Scene.apply_surface
    del bpy.types.Scene.apply_lattice

if __name__ == "__main__":
    register()
