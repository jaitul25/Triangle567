@JaitulBharodiya

import unittest

from HW02a_JBharodiya import classify_triangle

class TestTriangles(unittest.TestCase):

    def testEquilateralTriangle1(self): 
        self.assertEqual(classify_triangle(5,5,5),'Equilateral Triangle')

    def testEquilateralTriangle2(self): 
        self.assertEqual(classify_triangle(7,7,7),'Equilateral Triangle')

    def testIsocelesTriangle3(self): 
        self.assertEqual(classify_triangle(7,7,3),'Isosceles Triangle')
    
    def testIsocelesTriangle4(self):     
        self.assertEqual(classify_triangle(5,7,7),'Isosceles Triangle')

    def testRightTriangle5(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right Angled Triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classify_triangle(7,8,9),'Scalene Triangle')

if __name__ == '__main__':
    unittest.main(exit=False,verbosity=2)

