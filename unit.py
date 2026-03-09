unit = float(input("Enter total unit consumed: "))

if unit <= 50:
    amt = unit * 0.50

elif unit <= 150:
    amt = 25 + (unit - 50) * 0.75

elif unit <= 250:
    amt = 100 + (unit - 150) * 1.20

else:
    amt = 220 + (unit - 250) * 1.50

sur_charge = amt * 0.20
total_bill = amt + sur_charge

print("Electricity Bill = ₹", total_bill)