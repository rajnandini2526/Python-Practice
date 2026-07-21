# Rotate a list to the left by k positions.


numbers = [10, 20, 30, 40, 50]

k = 2  #We want to rotate the list 2 positions to the left.

rotated_list = numbers[k:] + numbers[:k]

# (numbers[k:])--->Since k = 2:  +  (numbers[:k])--->Starts from index 2 and goes to the end.

print("Original List:", numbers)
print("Rotated List:", rotated_list)