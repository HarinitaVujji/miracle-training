"""
How Python Access Modifiers is Useful for Programming in Python?
 Public
 Private
 Protected
"""
class Student:
    def __init__(self):
        self._marks = 95   # Protected variable
class Result(Student):
    def show(self):
        print(self._marks)
r = Result()
r.show()