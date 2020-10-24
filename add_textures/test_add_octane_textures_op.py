import unittest
from unittest import TestCase
# from .add_octane_textures_op import *

class NWAddOctaneTexturesTest(TestCase):

    def setUp(self):
        pass
        # self.add_octane_textures = NWAddOctaneTextures()

    def test_split_texture_name(self):
        # texture_name_splited = self.add_octane_textures.split_texture_name("asd_asd-asd.ds")
        self.assertEqual("asd asd_asd-ds", "asd asd asd ds")

if __name__ == "__main__":
    unittest.main()
