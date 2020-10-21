import bpy
from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import (
    BoolProperty,
    StringProperty
)

class NWOctaneTexturesTags(PropertyGroup):
    transmission: StringProperty(
        name='Transmission',
        default='translucency',
        description='add description')
    albedo_color: StringProperty(
        name='Albedo color',
        default='diffuse diff albedo base col color',
        description='Naming Components for Albedo Color maps')
    ambient_occlusion: StringProperty(
        name='Ambient occlusion',
        default='ao occlusion',
        description='add description')
    metallic: StringProperty(
        name='Metallic',
        default='metallic metalness metal mtl',
        description='Naming Components for metallness maps')
    specular: StringProperty(
        name='Specular',
        default='specularity specular spec spc',
        description='Naming Components for Specular maps')
    roughness: StringProperty(
        name='Roughness',
        default='roughness rough rgh',
        description='Naming Components for roughness maps')
    gloss: StringProperty(
        name='Gloss',
        default='gloss glossy glossiness',
        description='Naming Components for glossy maps')
    opacity: StringProperty(
        name='Opacity',
        default='opacity',
        description='added description')
    bump: StringProperty(
        name='Bump',
        default='bump bmp heightmap height h',
        description='Naming Components for bump maps')
    normal: StringProperty(
        name='Normal',
        default='normal nor nrm nrml norm',
        description='Naming Components for Normal maps')
    displacement: StringProperty(
        name='Displacement',
        default='displacement displace disp dsp',
        description='Naming Components for displacement maps')

class NWOctanePreferences(AddonPreferences):
    bl_idname = __package__

    separators: StringProperty(
        name='Separators',
        default='-,--,_,__,.,#',
        description='Separators for split texture name, via ","')

    show_octane_lists: BoolProperty(
        name='Show Octane textures naming tags',
        default=False,
        description='Expand this box into a list of all naming tags for octane textures setup'
    )
    ocatane_textures_tags: bpy.props.PointerProperty(type=NWOctaneTexturesTags)

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.prop(self, 'separators')

        box = layout.box()
        col = box.column(align=True)
        col.prop(self, 'show_octane_lists', text='Edit tags for auto texture detection in Octane "Main node" setup', toggle=True)
        if self.show_octane_lists:
            tags = self.ocatane_textures_tags

            col.prop(tags, 'transmission')
            col.prop(tags, 'albedo_color')
            col.prop(tags, 'ambient_occlusion')
            col.prop(tags, 'metallic')
            col.prop(tags, 'specular')
            col.prop(tags, 'roughness')
            col.prop(tags, 'gloss')
            col.prop(tags, 'opacity')
            col.prop(tags, 'bump')
            col.prop(tags, 'normal')
            col.prop(tags, 'displacement')
