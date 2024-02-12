import unittest
import transdict



class TestTransDict(unittest.TestCase):
    def setUp(self):
        labels = ['color','number','shape','element']
        relations = [('red',0,'circle','fire'),
                     ('brown',1,'square','earth'),
                     ('blue',2,'rectangle','water'),
                     ('green',3,'oval','forest'),
                     ('white',4,'quatrefoil','snow'),
                     ('black',5,'trapezoid', 'swamp')]
        self.data = transdict.TransDict(labels, relations)
	
    def test_addErrorDup(self):
        with self.assertRaises(Exception):
            self.data.add(('rainbow', 1, 'crescent', 'mountain'))
	
    def test_colorOfFire(self):
        self.assertEqual(self.data.colorOf('fire'), 'red')

    def test_numberOfFire(self):
        self.assertEqual(self.data.numberOf('fire'), 0)

    def test_shapeOfFire(self):
        self.assertEqual(self.data.shapeOf('fire'), 'circle')

    def test_elementOfFire(self):
        self.assertEqual(self.data.elementOf('fire'), 'fire')

    def test_fire_red(self):
        self.assertEqual(self.data['fire'], 'red')

    def test_circle_fire(self):
        self.assertEqual(self.data['circle'], 'fire')

    def test_0_circle(self):
        self.assertEqual(self.data[0], 'circle')

    def test_red_0(self):
        self.assertEqual(self.data['red'], 0)

if __name__ == '__main__':
    unittest.main()
