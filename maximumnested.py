a = 90
b = 40
c = 50
d = 20

if a > b :
    if a > c:
        if a > d:
            maximum = a
        else: 
            maximum = d
    else:
        if c > d:
            maximum = c
        else:
            maximum = d

else:
    if b > c:
        if b > d:
            maximum = b
        else: 
            maximum = d
    else:
        if c > d:
            maximum = c
        else:
            maximum = d                                       

print("The maximum number is", maximum)           





