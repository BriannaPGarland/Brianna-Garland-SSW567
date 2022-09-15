#Brianna Garland 

#“Write a function classify_triangle() that takes three  parameters: a, b, and c. The three parameters represent the 
#lengths of the sides of a triangle. The function returns a string that specifies whether the triangle is scalene, isosceles,
#or equilateral, and whether it is a right triangle as well.”

#Hint:  Write a function called classify_triangle(a, b, c) where a, b, and c are the lengths of the sides of the triangles.   
#You may either allow the user to enter values that you pass to classify_triangle() or your "main" routine can just invoke
#classify_triangle() with values.   This approach allows you to easily invoke classify_triangle() from your test framework.

def classify_triangle(a,b,c):
    #return a string that specifies if the triangle is scalene isosceles or equilateral and whether it is a right triangle 
    result = ""
    if(a ==b and a == c): #if all sides equal --> Equalateral
        result += "This Triangle is an Equilateral Triangle"
    elif(a!=b and a!=c and b!=c): # if no sides are equal--> scalene
        result += "This is a Scalene Triangle" 
    else: #
        result += "This is an Isosceles Triangle "


    if (a*a + b*b == c*c)or(b*b + c*c == a*a)or (a*a +c*c == b*b):
        if(result == ""):
            result += ("This is a Right Triangle")
        else:
            result += (". This is also a Right Triangle")
    return(result)
first = input("\nHello, Welcome to the triangle Identifier please enter your first side length \n")
sec = input("Please enter your second side length \n")
third = input("Please enter your final side length \n")
print("-----------------------------------------\n")
first = float(first)
sec = float(sec)
third =float(third)

def test_classify_triangle():
    a = first
    b = sec
    c = third
    if (a*a + b*b == c*c)or(b*b + c*c == a*a)or (a*a +c*c == b*b):
            if(a==b and a ==c):
                assert classify_triangle(a,b,c) == "This Triangle is an Equilateral Triangle. This is also a Right Triangle"
            elif(a!=b and a!=c and b!=c):
                assert classify_triangle(a,b,c) == "This is a Scalene Triangle. This is also a Right Triangle"
            elif(a==b or b==c or c ==a):
                assert classify_triangle(a,b,c) =="This is an Isosceles Triangle. This is also a Right Triangle"
            else: 
                assert classify_triangle(a,b,c) =="This is a Right Triangle"
    else:
        if(a==b and a ==c):
            assert classify_triangle(a,b,c) == "This Triangle is an Equilateral Triangle"
        elif(a!=b and a!=c and b!=c):
            assert classify_triangle(a,b,c) == "This is a Scalene Triangle"
        else:
            assert classify_triangle(a,b,c) =="This is an Isosceles Triangle "
 

print(classify_triangle(first,sec,third))






