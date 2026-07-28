# Print the multiplication table of a given number

# (while)
n = int(input("enter number:"))

i = 1
while i <= 10:
    print(n * i)
    i += 1

# (for)
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)