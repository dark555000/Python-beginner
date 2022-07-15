market_price = int(input("What is the market price of your car? "))
a = input("Enter your sex(male/female) ")
if a == "male":
    age = int(input("Enter your age "))
    if age >= 26:
        print(23 * market_price / 100)
    else:
        print(9 * market_price / 100)
elif a == "female":
    car = input("is your car sports? ")
    if car == "yes":
        print(21 * market_price / 100)
    else:
        print(10 * market_price / 100)
