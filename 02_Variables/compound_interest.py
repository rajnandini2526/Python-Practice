# Calculate compound interest using variables.

principal = 10000
rate = 10
time = 2

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)