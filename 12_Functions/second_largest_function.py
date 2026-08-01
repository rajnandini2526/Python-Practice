# Write a function that returns the second largest element in a list

def second_largest(numbers):

    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]

values = [10, 50, 30, 80, 60]

print(second_largest(values))