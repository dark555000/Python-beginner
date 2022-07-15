from random import randint
print("choice 1 = rock, choice 2 = paper, and choice 3 = scissors")
choice = int(input("What is your choice(1/2/3)?  "))
comp_choice = randint(1, 3)
print(f"computer's choice is {comp_choice}")
if choice == comp_choice:
    print("draw")
elif choice == 1:
    if comp_choice == 2:
        print("paper beats rock , you lose...")
    elif comp_choice == 3:
        print("rock beats scissors, you win")
elif choice == 2:
    if comp_choice == 1:
        print("paper beats rock , you win")
    elif comp_choice == 3:
        print("scissors beats paper, you lose")
else:
    if comp_choice == 1:
        print("rock beats scissors, you lose")
    elif comp_choice == 2:
        print("scissors beats paper, you win")



