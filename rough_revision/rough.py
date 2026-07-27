# Q) WAP to enter marks of subjects from user and store them in dictionary.
#  start with an empty dictionary & add one by one. 
#  use subject name as key and marks as value

# ANS----------------------------------------------------------->
# marks = {}

# x = int(input("enter maths marks:"))
# marks.update({"maths" : x})

# x = int(input("enter phy marks:"))
# marks.update({"phy" : x})

# x = int(input("enter english marks:"))
# marks.update({"english" : x})

# x = int(input("enter hindi marks:"))
# marks.update({"hindi" : x})

# print("marks of", marks)



# Q) Figure out a way to store 9 & 9.0 as seperate values in a set
# hint: can take help of built-in data types

# ANS ------------------------------------------------------------>
# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)



# Q) store the following word meaning in python dictionary:
# table: "a piece of furniture" , "list of facts & figures"
# cat: " a small animal "

# ANS ------------------------------------------------------------------>
# null_dict = {
#     "cat" : "a small animal", 
#     "table": ["a piece of furniture" , "list of facts & figures"]
# }
# print(null_dict)



# Q) you are given a list of subjects for students,
# assume 1 classroom is required for 1 subject. how many classrooms are needed by all students.
#  ("python" , "c++" , "java", "c++" , "js" , "python" , 
#   "c" , "java" , "js" , "python" , "c++" , "js" , "c")

# ANS --------------------------------------------------------------------->
# subjects = {
#     "python" , "c++" , "java", "c++" , "js" , "python" ,   
#    "c" , "java" , "js" , "python" , "c++" , "js" , "c"
# }
# (we stored all sub in a set, bcuz in set duplicate values are removed
# 1 class for 1 sub, here we got which types of sub are there )
# print(subjects)
# print("total number of classroom required are:", (len(subjects)))



# (loops)
# Q) print numbers from 1 to 100
# ANS ------------------------------------------------------->
# count = 1
# while count <= 100 :
#     print (count)
#     count += 1

# Q) print numbers from 100 to 1
# ANS---------------------------------------------------------->
# count = 100
# while count >= 1 :
#     print(count)
#     count -= 1


# Q) Print the multiplication table of a number n 
# ANS ----------------------------------------------------->
# n = int(input("Enter a Number:"))
# i = 1
# while i <= 10 :
#     print (n * i) 
#     i += 1


# Q) print the element of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
# ANS ------------------------------------------------------------>
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(nums) :
#     print(nums[idx])
#     idx += 1

# Q) search for a number x in this tuple using loop :(1,4,9,16,25,36,49,64,81,100)
# ANS----------------------------------------------->
# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 25

# i = 0
# while i < len(nums):
#     if(nums[i] == x) :
#         print("Found at index", i)
#         break
#     else:
#         print("finding...")
#         i += 1



# (ex of BREAK)
# i = 1
# while i <= 5:
#     print(i) 
#     if (i == 3):
#         break
#     i += 1
# print("end of loop")

# (ex of CONTINUE)
# i = 0
# while i <= 5:
#     if (i == 3): #
#         i += 1
#         continue
#     print(i)
#     i += 1



# Q) (using for) print the element of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
# ANS ------------------------------------------------------------>
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums :
#     print(el)


# Q) (using for) search for a number x in this tuple using loop :(1,4,9,16,25,36,49,64,81,100,49)
# ANS----------------------------------------------->
# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
                                        #  (this searching method id called linear search)
# idx = 0
# for el in nums:
#     if (el == x):
#         print("number found at idx", idx)
#     idx += 1 




# (RANGE)
# seq = range(10)

# for i in seq:
#     print(i)

                 
                   # OR 

# for i in range(2, 6):    #(start, stop)
#     print(i)

                   # OR

# for i in range(2, 10, 2):    #(start, stop, step)
#     print(i)

                   # OR

# for i in range(2, 100, 5):    #(start, stop, step)
#     print(i)


# (USING for and range())
# Q) print numbers from 1 to 100
# ANS--------------------------------------->
# for i in range(1, 101):
#     print(i)

# Q) print numbers from 100 to 1
# ANS--------------------------------------->
# for i in range(100, 0, -1):
#     print(i)

# Q) print the multiplication table of n
# ANS--------------------------------------->
# n = int(input("enter number:"))

# for i in range(1, 11):
#     print(n * i)

# Q) WAP to find the sum of first n natural nums (using while)(1+2+3+4+5)
# ANS--------------------------------------->
n = 5

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum = ", sum)


# Q) WAP to find factorial of first n natural nums (using while)
# ANS--------------------------------------->
n = 5
fact = 1
i = 1
while i <= n:
    fact *= 1
    i += 1
print("Factorial", fact)











