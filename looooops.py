s = "a b c d"
f = "e f g h i j k l m n o p q r s t u v w x y z"
while True:
    c = input("Enter an alphabet or stop the game? ")
    if c == "stop the game":
        print("The game has ended")
        break
    elif c in s:
        print(c, "is in s")
    elif c in f:
        print(c, "is not in s")
    else:
        print("syntax error")
