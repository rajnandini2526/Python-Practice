# Find the GCD (HCF) of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

small = min(num1, num2)

gcd = 1

for i in range(1, small + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD =", gcd)