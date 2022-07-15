my_list = list(range(0, 101, 2))
print(my_list)
print(my_list[0: 10])
my_list.append(True)
print(my_list)

def pyth(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(pyth(3, 4, 5))