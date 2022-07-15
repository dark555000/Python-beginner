import random
a = random.randint(1, 10)
b = random.randint(1, 10)
print(a)
print(b)
c = int(input(f" What is the product of {a} and {b}? "))
if c == a*b:
    print("Great job! You are correct ")
else:
    print("Oh , you are wrong. The answer is ", a*b)
