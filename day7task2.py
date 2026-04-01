from abc import ABC, abstractmethod
# Abstract Base Class
class AbstractUser(ABC):
    """
    Abstract base class for all user types.
    Enforces implementation of get_details() in subclasses.
    """

    @abstractmethod
    def get_details(self):
        """
        Abstract method to be implemented by all subclasses.
        Should return user details as a string or dictionary.
        """
        pass


# Example subclass: Student
class Student(AbstractUser):
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def get_details(self):
        return f"Student Name: {self.name}, Roll No: {self.roll_no}"


# Example subclass: Teacher
class Teacher(AbstractUser):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_details(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}"


# Example usage
if __name__ == "__main__":
    try:
        # This will raise an error because AbstractUser cannot be instantiated directly
        user = AbstractUser()
    except TypeError as e:
        print(f"Error: {e}")

    # Create objects of subclasses
    student = Student("kani", 101)
    teacher = Teacher("kanama", "Maths")

    # Call get_details() from each subclass
    print(student.get_details())
    print(teacher.get_details())

