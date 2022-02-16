from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestVizHomerseklet(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.signum(0)
        elvart = "semleges"
        self.assertEqual(elvart, aktualis, "Nulla  esetén rosszul határozta meg az értékelése!")
    def test_feladat02(self):
        aktualis = feladatok.signum(1)
        elvart = "pozitív"
        self.assertEqual(elvart, aktualis, "Egy esetén rosszul határozta meg az értékelése!")
    def test_feladat03(self):
        aktualis = feladatok.signum(-1)
        elvart = "negatív"
        self.assertEqual(elvart, aktualis, "-1  esetén rosszul határozta meg az értékelése!")
    def test_feladat04(self):
        aktualis = feladatok.signum(-100)
        elvart = "negatív"
        self.assertEqual(elvart, aktualis, "-100  esetén rosszul határozta meg az értékelése!")
    def test_feladat05(self):
        aktualis = feladatok.signum(100)
        elvart = "pozitív"
        self.assertEqual(elvart, aktualis, "-00  esetén rosszul határozta meg az értékelése!")


