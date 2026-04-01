class Student:
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer")
        self.name = name
        self.age = age

# Sample list of Student objects
students = [
    Student("Anbu", 20),
    Student("Barani", 22),
    Student("Chandru", 19)
]

# Extract only names using map()
names = list(map(lambda s: s.name, students))

print("Student Names:", names)

