from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student('bob', [65])
rof = Student('rof')
bob.take_exam(89)
print(bob.grades)
print(rof.grades)