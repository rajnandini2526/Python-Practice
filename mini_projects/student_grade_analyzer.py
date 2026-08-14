# Student Grade Analyzer
# Analyzes a student's marks using functions, lists, loops, and conditions.
#
# Challenge:
# - Receive a list of marks through a function.
# - Calculate the total using a loop.
# - Calculate the average.
# - Find the highest and lowest marks using loops.
# - Assign a grade based on the average.
# - Return the calculated results.


def calculate_result(marks):
    total = 0

    # Calculate total
    for mark in marks:
        total += mark

    # Calculate average
    average = total / len(marks)

    # Find highest mark
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark

    # Find lowest mark
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark

    # Determine grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return total, average, highest, lowest, grade


marks = [78, 65, 92, 45, 81]

result = calculate_result(marks)

print("Total:", result[0])
print("Average:", result[1])
print("Highest:", result[2])
print("Lowest:", result[3])
print("Grade:", result[4])

































































