import unittest
from chain import *

class BuildingTest(unittest.TestCase):
    def test_construct_building(self):
        building = Building()
        self.assertTrue(building.construct('construct_building'))

    def test_wrong_item(self):
        building = Building()
        self.assertFalse(building.construct('wrong_item'))

class RoofingTest(unittest.TestCase):
    def test_add_roof(self):
        roofing = Roofing()
        self.assertTrue(roofing.construct('add_roof'))

    def test_wrong_item(self):
        roofing = Roofing()
        self.assertFalse(roofing.construct('wrong_item'))

class InteriorDesignTest(unittest.TestCase):
    def test_design_interior(self):
        interior_design = InteriorDesign()
        self.assertTrue(interior_design.construct('design_interior'))

    def test_wrong_item(self):
        interior_design = InteriorDesign()
        self.assertFalse(interior_design.construct('wrong_item'))

class FinalTouchTest(unittest.TestCase):
    def test_add_final_touch(self):
        final_touch = FinalTouch()
        self.assertTrue(final_touch.construct('add_final_touch'))

    def test_wrong_item(self):
        final_touch = FinalTouch()
        self.assertFalse(final_touch.construct('wrong_item'))

if __name__ == '__main__':
    unittest.main()
