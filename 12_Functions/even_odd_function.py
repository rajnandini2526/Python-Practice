# Write a function to check whether a number is even or odd 

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check(10)) 
print(check(7))