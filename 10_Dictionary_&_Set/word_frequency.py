# Count the occurrence of every word in a sentence 
# and display the result in descending order of frequency.

sentence = "python is easy and python is powerful"

words = sentence.split()  #split() converts the sentence into a list of words.

frequency = {}   #A dictionary counts each word's occurrences.

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_frequency = sorted(   #sorted() arranges the words by frequency.
    frequency.items(),
    key=lambda item: item[1],    #Creates a small one-line function
                                 # Sort using the second element of each tuple
    reverse=True      #reverse=True sorts in descending order.
)

for word, count in sorted_frequency:
    print(word, ":", count)