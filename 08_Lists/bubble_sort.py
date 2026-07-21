# Implement Bubble Sort using a list.

numbers = [64, 34, 25, 12, 22, 11, 90]

n = len(numbers)   #Find the length. n=5

for i in range(n):  #Runs 5 times (one pass for each element).
    for j in range(0, n - i - 1):        #for j in range(0, n - i - 1):
                                         # For the first pass (i = 0):
                                         # Compare 5 and 2
                                         # Compare 5 and 8
                                         # Compare 8 and 1
                                         # Compare 8 and 9

        if numbers[j] > numbers[j + 1]:  #If the left number is larger than the right number, swap them.
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  #This is Python's shorthand for swapping values without using a temporary variable.

print("Sorted List1:", numbers)



#or



# Create a list of numbers
numbers = [4, 2, 3, 1]

# Find the total number of elements in the list
n = len(numbers)

# Outer loop - controls the number of passes
# It runs 4 times because there are 4 elements
for i in range(n):

    # Inner loop - compares adjacent elements
    # n - i - 1 reduces the number of comparisons after each pass
    for j in range(0, n - i - 1):

        # Check if the current element is greater than the next element
        if numbers[j] > numbers[j + 1]:

            # Swap the two elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Print the list after every pass
    print("Pass", i + 1, ":", numbers)

# Print the final sorted list
print("Sorted List2:", numbers)


#or


numbers = [7, 5, 2, 4]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("Pass", i + 1, ":", numbers)

print("Sorted List3:", numbers)