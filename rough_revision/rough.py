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
# n = 5

# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("total sum = ", sum)


# Q) WAP to find factorial of first n natural nums (using while)
# ANS--------------------------------------->
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= 1
#     i += 1
# print("Factorial", fact)





# (FUNCTIONS)
 
#  function defination 
# def calc_sum (a, b):     #(a, b) are called parameters
#     return a + b

#function call
# sum = calc_sum(1, 2)     #(1, 2) are called arguments
# print(sum)

# sum = calc_sum(8, 2)
# print(sum)

# sum = calc_sum(4, 2)
# print(sum)

# def calc_sum(a, b):
#     sum = a + b
#     print (sum)
#     return sum


# or 

# def print_hello():     #dosen't take any input
#     print("hi hello")       #dosen't need any argument
#                              #these types of fun are also possible
# print_hello()
# print_hello()
# print_hello()



# Q) average of 3 numbers
# ANS---------------------------------------->
# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return(avg)

# calc_avg(1, 2, 3)
# calc_avg(5, 3, 9)
# calc_avg(9, 6, 4)
# calc_avg(7, 1, 8)


# Q) write a function to print the length of list (list is the parameter)
# ANS----------------------------------------------->
# cities = ["delhi", "pune", "mumbai", "nagpur", "banglore", "noida"]
# seasons =  ["monsoon", "summer", "autom", "winter"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(seasons)


# Q) WAP to print the element of list in a single line (list is the parameter) 
# ANS-------------------------------------------------> 
# cities = ["delhi", "pune", "mumbai", "nagpur", "banglore", "noida"]
# seasons =  ["monsoon", "summer", "autom", "winter"]

# def print_list(list):
#     for item in list:
#         print(item, end = " ")

# print_list(seasons) 
# print_list(cities)
# print()



# Q)WAF to find the factorial of n (n is the parameter) 
# ANS---------------------------------------------------->
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)



# Q) WAF to convert USD to INR 
# ANS---------------------------------------------------->
# def usd_to_inr(usd):
#     inr = usd * 95.4      # Exchange rate (example)
#     return inr

# usd = float(input("Enter amount in USD: "))
# print("Amount in INR =", usd_to_inr(usd))



# Q) WAF to chech weather number is even or odd, output should be a str 
# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# n = int(input("Enter a number: "))
# print(check_even_odd(n))
# print(type(check_even_odd(n)))






# (RECURSION)- which re-occure / repeating itself 

# Q) return n! 
# def fact(n):
#     if (n == 0 or n ==1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(2)) 



# Q) WAF to find the sum of first n natural numbers using recursion
# ANS---------------------------------------------------->
def sum_natural(n):
    if n == 0:
        return 0
    return sum_natural(n - 1) + n   
sum = sum_natural
print (sum(5))  # Example usage



# Q) WAF to find the nth fibonacci number using recursion
# ANS---------------------------------------------------->
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)      
    
print(fibonacci(5))  # Example usage




# Q) WAF to find the sum of digits of a number using recursion
# ANS---------------------------------------------------->
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)  
    
print(sum_of_digits(12345))  # Example usage



# Q) WAF to reverse a string using recursion
# ANS---------------------------------------------------->
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("hello"))  # Example usage



# Q) Write a recursive function to print all element in a list(use list & index as parameter)
# ANS---------------------------------------------------->
def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1)  

fruits = ["apple", "banana", "cherry", "date"]
print_list(fruits)  # Example usage