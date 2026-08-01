# Write a function to check whether a number is prime

def prime(num):

    if num <= 1:
        return "Not Prime"

    for i in range(2, num):

        if num % i == 0:
            return "Not Prime"

    return "Prime"

print(prime(17))
print(prime(12))