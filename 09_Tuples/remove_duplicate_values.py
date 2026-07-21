# Remove duplicate values by converting a tuple appropriately.

numbers = (10, 20, 30, 20, 40, 10, 50)

unique = tuple(set(numbers))
#set() removes duplicates, but it does not preserve the original order.
print(unique)
