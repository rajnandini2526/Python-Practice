# . Given two dictionaries, find:
# Keys common to both dictionaries.
# Keys present only in the first dictionary.
# Keys present only in the second dictionary.

dict1 = {
    "a" : 10,
    "b" : 20,
    "c" : 30
}
dict2 = {
    "b" : 40,
    "c" : 50,
    "d" :60
}

keys1 = set(dict1.keys())
keys2 = set(dict2.keys())

print("Common keys:", keys1 & keys2)
print("only in first", keys1 - keys2)
print("only in second", keys2 - keys1)