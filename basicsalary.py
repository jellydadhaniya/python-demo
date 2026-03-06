bs = int(input("Enter basic salary: "))

if bs <= 10000:
    hra = bs * 0.20
    da = bs * 0.80

elif bs <= 20000:
    hra = bs * 0.25
    da = bs * 0.90

else:
    hra = bs * 0.30
    da = bs * 0.95

gs = bs + hra + da

print("Gross Salary =", gs)
    
    