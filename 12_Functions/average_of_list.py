# Write a function that returns the average of a list of numbers

def avg(num):
    return sum(num) / len(num)

marks = [90, 80, 70, 60, 50]
print(avg(marks))