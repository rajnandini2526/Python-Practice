# Find the intersection of two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = []  #Create an empty list to store common elements.

for i in list1:  #The loop checks every element of list1.
    if i in list2:  #Check whether that element also exists in list2.
        intersection.append(i)  #Store the common element.

print(intersection)

#or

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(list(set(list1) & set(list2)))

# (set(list1)) This converts list1 into a set, same for list 2.
#set(list1)--> Output:{1, 2, 3, 4, 5}
#set(list2)--> Output:{3, 4, 5, 6, 7}

# The & operator means intersection.
# It returns only the elements that are common in both sets.

# {1, 2, 3, 4, 5}
#         &
# {3, 4, 5, 6, 7}
# ----------------
# {3, 4, 5}