import random
my_list = ["France", "Germany", "America", "China", "India"]
another_list = ["one", "two", "three", "four", "five"]
new_list = my_list + another_list
print(" ".join(new_list))
print(new_list)
print(my_list[3])
print(my_list[-5])
print(my_list.pop())
my_list.append("Argentina")
print(my_list)
random.shuffle(my_list)
print(my_list)
print(random.choice(my_list))
print(" ".join(my_list))
print(my_list[3])
print(my_list[-3])
s = "awesome"
print(random.sample(s, len(s)))
