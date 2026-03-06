m1=int(input("Enter marks of subject1:"))
m2=int(input("Enter marks of subject2:"))
m3=int(input("Enter marks of subject3:"))
m4=int(input("Enter marks of subject4:"))
m5=int(input("Enter marks of subject5:"))
m6=int(input("Enter marks of subject6:"))

total=m1+m2+m3+m4+m5+m6
parcentage=total/6

if parcentage >=90: 
   print("Grade A")
elif parcentage >=80:
   print("Grade B")
elif parcentage >=70:
   print("Grade C") 
elif parcentage >=60:
   print("Grade D") 
elif parcentage >=40:
   print("Grade E")   
else :
    print("Grade F")