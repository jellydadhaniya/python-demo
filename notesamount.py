amount = int(input("Enter amount: "))

note2000 = amount // 2000
amount = amount % 2000

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

print("2000 notes =", note2000)
print("500 notes =", note500)
print("200 notes =", note200)
print("100 notes =", note100)