# Build a Student Record Management System.

students = {}

# Add students
students["101"] = {
    "name": "Raj",
    "age": 20,
    "branch": "CSBS",
    "skills": {"Python", "C"}
}

students["102"] = {
    "name": "Neha",
    "age": 21,
    "branch": "IT",
    "skills": {"Java", "SQL"}
}

# Display all students
print("All Students:")
for roll, details in students.items():
    print(roll, details)

# Update student details
students["101"]["age"] = 22
students["101"]["skills"].add("HTML")

# Search student
roll = "101"

if roll in students:
    print("\nStudent Found:")
    print(students[roll])
else:
    print("Student Not Found")

# Delete student
del students["102"]

print("\nAfter Deletion:")
for roll, details in students.items():
    print(roll, details)