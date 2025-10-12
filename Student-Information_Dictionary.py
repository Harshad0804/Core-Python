student = {
    "name": "Harshad",
    "age": 20,
    "course": "BCA",
    "marks": {
        "python": 85,
        "math": 90,
        "english": 88
    }
}

print("Name:", student["name"])
print("Course:", student["course"])

print("Python Marks:", student["marks"]["python"])

student["city"] = "Mumbai"

student["age"] = 21

student.pop("course")

print("\nUpdated Student Details:")
for key, value in student.items():
    print(f"{key} : {value}")
