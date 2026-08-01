# Write a function that accepts a variable number of arguments and returns their sum

def total(*numbers):

    return sum(numbers)

print(total(10, 20, 30))
print(total(5, 15, 25, 35))