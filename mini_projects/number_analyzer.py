# Build a Python program that analyzes numbers from 1 to 20.
# Loop through numbers 1 to 20.
# Skip numbers divisible by 3 using continue.
# If the number is 17, stop the loop completely using break.
# For every remaining number:
# If it's even, print: 4 → even
# If it's odd, print: 5 → odd

for i in range(1, 21):
    if i % 3 == 0:
        continue

    if i == 17:
        break

    if i % 2 == 0:
        print(i, "even")
    else:
        print(i,"odd")

