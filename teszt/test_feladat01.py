from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestVizHomerseklet(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.viz_allapot(0)
        elvart = "jég"
        self.assertEqual(elvart, aktualis, "Nulla fok esetén rosszul határozta meg a víz állapotot!")
    def test_feladat02(self):
        aktualis = feladatok.viz_allapot(101)
        elvart = "pára"
        self.assertEqual(elvart, aktualis, "101 fok esetén rosszul határozta meg a víz állapotot!")
    def test_feladat03(self):
        aktualis = feladatok.viz_allapot(1)
        elvart = "víz"
        self.assertEqual(elvart, aktualis, "1 fok esetén rosszul határozta meg a víz állapotot!")
    def test_feladat04(self):
        aktualis = feladatok.viz_allapot(99)
        elvart = "víz"
        self.assertEqual(elvart, aktualis, "99 fok esetén rosszul határozta meg a víz állapotot!")
    def test_feladat05(self):
        aktualis = feladatok.viz_allapot(-10)
        elvart = "jég"
        self.assertEqual(elvart, aktualis, "-10 fok esetén rosszul határozta meg a víz állapotot!")

