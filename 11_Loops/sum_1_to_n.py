# Find the sum of numbers from 1 to n

# (while)
n = int(input("enter a number:"))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum = ", sum)

# (for)
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)