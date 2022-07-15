s = ("e", 3, "apple", 9, "orange", "Banana")
print(type(s))
print(len(s))
# slicing of tuples.
print(s[:3])
a = tuple(("Hello", 2, True))
print(a)
print(type(a))
print(len(a))
# converting a tuple to a list and then back to a tuple!
s = list(s)
print(s)
print(type(s))
# unpacking of tuples
fruit = ("apples ", "Bananas", "Pears", "Oranges", "Strawberries")
(one, *two) = fruit
print(tuple(two))
# incoporate loops within tuples
for i in range(len(fruit)):
    print(fruit[2])
