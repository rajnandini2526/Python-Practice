# Create a dictionary from two lists (one containing keys and the other containing values).

keys = { "name" , "age" , "branch"}
values = {"raj" , 21 , "CSBS"}

student = dict(zip(keys , values))  #zip(keys, values) pairs corresponding elements
print(student)