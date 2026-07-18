# Accept different input types and convert them appropriately.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
is_employee = input("Are you an employee (True/False): ") == "True"

print("\n--- User Details ---")
print("Name:", name, type(name))
print("Age:", age, type(age))
print("Salary:", salary, type(salary))
print("Employee:", is_employee, type(is_employee))