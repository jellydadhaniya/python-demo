side1=int(input("Enter three slide1 of triangle:"))
side2=int(input("Enter three slide2 of triangle:"))
side3=int(input("Enter three slide3 of triangle:"))

if (side1 == side2 and side2 == side3):
    print("Equilateral triangle.")
    
elif (side1==side2 or side1==side3 or side2==side3):
    print("Isosceles triangle.")
    
else :
    print("Scalene triangle.")