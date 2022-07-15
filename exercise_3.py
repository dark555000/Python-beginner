s = input("Enter a string: ")
print(f"original string is {s}")
print("Printing only even index chars ")
a = len(s)
for i in range(0, a-1, 2):
    print(s[i])
