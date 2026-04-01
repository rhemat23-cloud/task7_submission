# Base class
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def display(self):
        print(f"Name: {self.name}, ID: {self.user_id}")


# Student inherits from User
class Student(User):
    def __init__(self, name, user_id, dept, fees):
        super().__init__(name, user_id)  # Reuse User's initialization
        self.dept = dept
        self.fees = fees

    def display(self):
        super().display()
        print(f"Department: {self.dept}, Fees: {self.fees}")


# Faculty inherits from User
class Faculty(User):
    def __init__(self, name, user_id, salary):
        super().__init__(name, user_id)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")


# TempFaculty inherits from Faculty
class TempFaculty(Faculty):
    def __init__(self, name, user_id, salary, duration):
        super().__init__(name, user_id, salary)
        self.duration = duration

    def display(self):
        super().display()
        print(f"Duration: {self.duration} months")


# Example usage
s = Student("Anbu", 101, "Computer Science", 50000)
f = Faculty("mani", 201, 75000)
t = TempFaculty("kanimozhil", 301, 40000, 6)

print("Student Info:")
s.display()
print("\nFaculty Info:")
f.display()
print("\nTemp Faculty Info:")
t.display()

