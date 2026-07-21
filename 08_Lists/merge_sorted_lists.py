# Merge two sorted lists into a single sorted list.

list1 = [1, 5, 8, 2, 6]
list2 = [10, 9, 4, 7, 3]

merged_list = list1 + list2  #first add both list
merged_list.sort()  #then sort and print

print(merged_list)