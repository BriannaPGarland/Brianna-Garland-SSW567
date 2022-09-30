"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    #Testing all possibilities of above range input 
    def testInputAAbove(self):
        self.assertEqual(classifyTriangle(250,60, 100),'InvalidInput', 'Any value above 200 is an invalid input ') 
    def testInputBAbove(self):
        self.assertEqual(classifyTriangle(60,260, 100),'InvalidInput', 'Any value above 200 is an invalid input ') 
    def testInputCAbove(self):
        self.assertEqual(classifyTriangle(60,10, 300),'InvalidInput', 'Any value above 200 is an invalid input ') 
    
    #Testing all possibilities of below range input 
    def testInputABelow(self):
        self.assertEqual(classifyTriangle(-250,60, 100),'InvalidInput', 'Any value above 200 is an invalid input ') 
    def testInputBBelow(self):
        self.assertEqual(classifyTriangle(60,-260, 100),'InvalidInput', 'Any value above 200 is an invalid input ') 
    def testInputCBelow(self):
        self.assertEqual(classifyTriangle(60,10, -300),'InvalidInput', 'Any value above 200 is an invalid input ') 

    #Testing none integer responses for side lengths: 
    def testInputDecimal(self):
        self.assertEqual(classifyTriangle(41.56,60, 50),'InvalidInput', 'Any value for side length should be an integer ') 
    def testInputString(self):
        self.assertEqual(classifyTriangle('ten',60, 50),'InvalidInput', 'Any value for side length should be an integer ') 
    def testInputChar(self):
        self.assertEqual(classifyTriangle('b',60, 50),'InvalidInput', 'Any value for side length should be an integer ') 
    
    #This fails because a*2 not a **2  or a*a   --> Attempting to test Right triangle logic 
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    #This fails because a*2 not a **2  or a*a  --> Attempting to test Right triangle logic 
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    #this fails: returns not a triangle instead "   --> Attempting to test equilateral triangle logic fails and returns not a triangle    
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    #Test the not a triangle fuction (2,2,3)  fails and returns not a triangle
    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be isoceles')

    #test a == c   a!=b Scalene failure should be isocoles w/ how code is written but returns scalene 
    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(3,4,3),'Isoceles','3,4,3 should be isoceles')

    #test a == b   a!=c  equalateral failure should be isocoles w/ how code is written but returns equalateral 
    def testIsocelesTrianglesc(self): 
        self.assertEqual(classifyTriangle(3,3,4),'Isoceles','3,3,4 should be isoceles')

    #Test for a scalene Triangle 
    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 should be Scalene')

    #Test for not a triangle values 
    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(2,2,5),'NotATriangle','2,2,5 should be not a triagle ')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
