# Write a function to check whether a string is a palindrome 

def palindrome(text):
    
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
    
print(palindrome("madam"))
print(palindrome("python"))
print(palindrome("101"))
print(palindrome("hello"))
print(palindrome("racecar"))
print(palindrome("level"))