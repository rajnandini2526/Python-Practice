# Reverse a number using a loop

num = int(input("enter number:"))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //=10

print("Reverse = ", reverse)