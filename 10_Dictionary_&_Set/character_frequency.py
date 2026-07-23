# Count the frequency of each character in a string using a dictionary.

str = "rajnandini"
frequency = {}

for letter in str:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(frequency)