# Find the factorial of a number

# (while)
n = int(input("enter number:"))
fact = 1
i = 1
while i <= n:
    fact *= 1
    i += 1
print("Factorial", fact)

# (for)
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)
