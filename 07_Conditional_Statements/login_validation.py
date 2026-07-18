# Build a login system that validates username and password.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")