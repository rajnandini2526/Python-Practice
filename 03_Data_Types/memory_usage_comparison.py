# Compare memory usage of different data types.

import sys

a = 100
b = 3.14
c = "Python"
d = [1, 2, 3]

print("Integer:", sys.getsizeof(a), "bytes")
print("Float:", sys.getsizeof(b), "bytes")
print("String:", sys.getsizeof(c), "bytes")
print("List:", sys.getsizeof(d), "bytes")