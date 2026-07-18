# Take multiple inputs in a single line.

name, age, city = input("Enter name, age, city: ").split()

print("\nUser Details")
print("Name :", name)
print("Age  :", age)
print("City :", city)