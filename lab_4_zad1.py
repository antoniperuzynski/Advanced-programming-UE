# Zadanie 1
class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self) -> str:
        return f'Name:{self.name} Marks:{self.marks}'

    @property
    def is_passed(self) -> bool:
        return self.marks > 50


student1 = Student('Antoni', 60)
student2 = Student('Dawid', 40)
print(student1.is_passed)
print(student2.is_passed)
