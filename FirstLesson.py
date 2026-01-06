print("First mini project")

print("Enter your name: ")
name = input()

print("Enter your age: ")
age = int(input())

print("Enter your liked programming language: ")
programming_language = input()

if age >= 18:
    status = "adult"
else:
    status = "young"

print("Hello", name, "!")
print("Your age is", status, "!")
print("Your liked programming language is: ", programming_language, "!")



