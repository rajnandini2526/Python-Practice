# Q) WAP to enter marks of subjects from user and store them in dictionary.
#  start with an empty dictionary & add one by one. 
#  use subject name as key and marks as value

# ANS----------------------------------------------------------->
marks = {}

x = int(input("enter maths marks:"))
marks.update({"maths" : x})

x = int(input("enter phy marks:"))
marks.update({"phy" : x})

x = int(input("enter english marks:"))
marks.update({"english" : x})

x = int(input("enter hindi marks:"))
marks.update({"hindi" : x})

print("marks of", marks)

# Q) Figure out a way to store 9 & 9.0 as seperate values in a set
# hint: can take help of built-in data types

# ANS ------------------------------------------------------------>
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

# Q) store the following word meaning in python dictionary:
# table: "a piece of furniture" , "list of facts & figures"
# cat: " a small animal "

# ANS ------------------------------------------------------------------>
null_dict = {
    "cat" : "a small animal", 
    "table": ["a piece of furniture" , "list of facts & figures"]
}
print(null_dict)

# Q) you are given a list of subjects for students,
# assume 1 classroom is required for 1 subject. how many classrooms are needed by all students.
#  ("python" , "c++" , "java", "c++" , "js" , "python" , 
#   "c" , "java" , "js" , "python" , "c++" , "js" , "c")

# ANS --------------------------------------------------------------------->
subjects = {
    "python" , "c++" , "java", "c++" , "js" , "python" ,   
   "c" , "java" , "js" , "python" , "c++" , "js" , "c"
}
# we stored all sub in a set, bcuz in set duplicate values are removed
# 1 class for 1 sub, here we got which types of sub are there 
print(subjects)
print("total number of classroom required are:", (len(subjects)))