import random
my_list = ["father", "enterprise",  "science", "programming",
           "resistance", "fiction", "condition", "reverse", "computer", "python"]
while True:
    b = input("Play or stop? ")
    if b == "stop":
        print("The game has ended")
        break
    else:
        c = random.choice(my_list)
        s = "".join(random.sample(c, len(c)))
        print(s)
        a = input("Enter the word ")
        if a == c:
            print("Yes, you are correct.")
        else:
            print(f"sorry, you are wrong.The correct word is {c}")
