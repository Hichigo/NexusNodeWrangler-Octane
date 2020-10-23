import unittest
from unittest import TestCase
from ..add_textures.add_octane_textures_op import *

class NWAddOctaneTexturesTest(TestCase):

    def setUp(self):
        self.add_octane_textures = NWAddOctaneTextures()

    def split_texture_name_test(self):
        print("sadas")
        texture_name_splited = self.add_octane_textures.split_texture_name("asd_asd-asd.ds")
        self.assertEqual(texture_name_splited, "asd asd asd ds")

if __name__ == "__main__":
    unittest.main()