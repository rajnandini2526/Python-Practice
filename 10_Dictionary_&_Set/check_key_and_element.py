# Check whether a given key exists in a dictionary and whether a given element exists in a set.

students = {
    "name" : "raj",
    "age" : 21,
    "branch" : "CSBS"
}

numbers = { 10, 20, 30, 40}

key = "age"
element = 60

if key in students:
    print("key exists")
else : 
    print("key does not exist")

if element in numbers:
    print("element exists")
else : 
    print("element doest not exist")