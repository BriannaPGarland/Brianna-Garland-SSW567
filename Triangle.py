# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""

def classify_triangle(sde_a,sde_b,sde_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    #  # pylint: disable=line-too-long
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if (not(isinstance(sde_a,int) and isinstance(sde_b,int) and isinstance(sde_c,int))) or (sde_a not in range(0,200)or (sde_b not in range(0,200)) or (sde_c not in range(0,200))):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle

    #Solution: add a not or  a<= b+c
    if (sde_a >= (sde_b + sde_c)) or (sde_b >= (sde_a + sde_c)) or (sde_c >=(sde_a+sde_b)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if sde_a == sde_b and sde_b == sde_c:  #a==b and b==c
        return 'Equilateral'

    if((sde_a**2)+(sde_b**2))==(sde_c**2)or((sde_c**2)+(sde_b**2))==(sde_a**2)or((sde_a**2)+(sde_c**2))==(sde_b**2):
        return 'Right'
    if (sde_a != sde_b) and  (sde_b != sde_c) and (sde_a != sde_c): # c!=a
        return 'Scalene'
    return 'Isoceles'
