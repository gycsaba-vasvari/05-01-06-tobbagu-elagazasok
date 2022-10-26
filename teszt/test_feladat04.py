from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKoorinatarendszer(TestCase):
    def test_feladat00(self):
        x=0
        y=0
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "origo"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladat11(self):
        x=1
        y=1
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "1. negyed"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladatneg11(self):
        x=-1
        y=1
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "2. negyed"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladatneg1neg1(self):
        x=-1
        y=-1
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "3. negyed"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladat1neg1(self):
        x=11
        y=-1
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "4. negyed"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladat5nulla(self):
        x=5
        y=0
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "x tengely"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladatneg5nulla(self):
        x=-5
        y=0
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "x tengely"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladatnulla5(self):
        x=0
        y=5
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "y tengely"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")
    def test_feladatnullaneg5(self):
        x=0
        y=-5
        aktualis = feladatok.koordinatarendszer(x,y)
        elvart = "y tengely"
        self.assertEqual(elvart, aktualis, str(x)+","+str(y)+" pont helyét rosszul határozta meg")

