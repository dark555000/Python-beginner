price = int(input("What's the price? "))
percentage_tip = float(input("Enter the percentage you wanna tip: "))
tip = price * percentage_tip/100
tip = round(tip, 2)
print(tip)
