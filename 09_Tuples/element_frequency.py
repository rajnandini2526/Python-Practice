# Find the frequency of every element in a tuple.

numbers = (10, 30, 50, 10, 20, 30, 60, 20, 10)

for i in set(numbers):    #i stores one element of the set at a time.
    print(i,"appears", numbers.count(i), "times")


#     Tuple
# (10,30,50,10,20,30,60,20,10)
#               │
#               ▼
#      set(numbers) - removes duplicate values
#               │
#               ▼
#    {10,20,30,50,60}
#               │
#               ▼
# Loop starts
#               │
#               ▼
# i = 10 → count = 3 → Print  (The count() method counts how many times i appears in the tuple.)
# i = 20 → count = 2 → Print
# i = 30 → count = 2 → Print
# i = 50 → count = 1 → Print
# i = 60 → count = 1 → Print