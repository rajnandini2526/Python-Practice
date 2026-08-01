# Write a function to count vowels in a string

def count_vowels(s):
    count = 0

    for letter in s:
        if letter.lower() in 'aeiou':
            count += 1
    return count

print(count_vowels("Hello World"))
print(count_vowels("Python Programming"))