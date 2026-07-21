# Remove duplicate elements from a list.

numbers = [10, 20, 20, 30, 40, 40, 50]
duplicate = list(set(numbers))    #set() removes duplicates, but it does not preserve the original order of the elements.
print(duplicate)


#another method

numbers = [10, 20, 10, 30, 20, 40, 50, 30]  #This is the original list containing duplicate values.

unique_list = []  #Create an empty list where we'll store only unique elements.

for num in numbers:   #The loop checks every element one by one.
    if num not in unique_list:  #Check whether the current element already exists in unique_list.
        unique_list.append(num)  #If the number is not already present, add it to unique_list.

print("Original List:", numbers)
print("List without duplicates:", unique_list)

