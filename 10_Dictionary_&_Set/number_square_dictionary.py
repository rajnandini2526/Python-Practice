# Create a dictionary where the keys are numbers from 1 to 10 and the values are their squares.

squares = {} #the dictionary is empty, key = num, value = square

for number in range(1, 11):  #range(start, stop) generates numbers starting from 1 and stops before 11.
    squares[number] = number ** 2  #** is the power (exponent) operator.

print(squares)