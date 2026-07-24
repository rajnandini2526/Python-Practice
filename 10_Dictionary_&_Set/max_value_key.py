# Find the key with the maximum value in a dictionary.

marks = {
    "raj" : 95 , 
    "nandini" : 98 , 
    "aditya" : 64 ,
    "rahul" : 78
}
highest = max(marks, key = marks.get)
# "While finding the maximum, don't compare the keys. Compare their corresponding values."

print("Students", highest)
print ("Marks", marks[highest])