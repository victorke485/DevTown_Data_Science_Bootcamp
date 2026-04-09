# Variables
name = "john"
print(name)
print(f"The student name is {name}")

# List
my_list = [23, 13, 42, 35]
print(my_list[0])
print(my_list[-2])

# Dictionary
student = {
    "name":  "Victor",
    "age": 29,
}
print(student["name"])
print(student["age"])

# Conditions
marks = 75
if marks > 50:
    print("Pass")
else:
    print("Fail")

student_marks = int(input("Enter your marks: "))
if student_marks > 50:
    print("Pass")
else:
    print("Fail")

# For loop
for i in range(5):
    print(i)

# Mini Task - program to check the voting eligibility of a person
age = int(input("Enter your age : "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Check if number is positive or negative
number = 12
if number > 0:
    print("Number is positive")
else:
    print("The number is negative")
