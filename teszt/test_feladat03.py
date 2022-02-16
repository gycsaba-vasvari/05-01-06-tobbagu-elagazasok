from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestErtekeles(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.ertekeles(1)
        elvart = "elégtelen"
        self.assertEqual(elvart, aktualis, "Egyes esetén rosszul határozta meg az értékelést")
    def test_feladat02(self):
        aktualis = feladatok.ertekeles(2)
        elvart = "elégséges"
        self.assertEqual(elvart, aktualis, "Kettes esetén rosszul határozta meg az értékelést")
    def test_feladat03(self):
        aktualis = feladatok.ertekeles(3)
        elvart = "közepes"
        self.assertEqual(elvart, aktualis, "Hármas esetén rosszul határozta meg az értékelést")
    def test_feladat04(self):
        aktualis = feladatok.ertekeles(4)
        elvart = "jó"
        self.assertEqual(elvart, aktualis, "Jó esetén rosszul határozta meg az értékelést")
    def test_feladat05(self):
        aktualis = feladatok.ertekeles(5)
        elvart = "jeles"
        self.assertEqual(elvart, aktualis, "Jeles esetén rosszul határozta meg az értékelést")
    def test_feladat00(self):
        aktualis = feladatok.ertekeles(0)
        elvart = "értelmezhetetlen"
        self.assertEqual(elvart, aktualis, "Értelmezhetetlen jegy esetén rosszul határozta meg az értékelést")
    def test_feladat06(self):
        aktualis = feladatok.ertekeles(6)
        elvart = "értelmezhetetlen"
        self.assertEqual(elvart, aktualis, "Értelmezhetetlen jegy esetén rosszul határozta meg az értékelést")