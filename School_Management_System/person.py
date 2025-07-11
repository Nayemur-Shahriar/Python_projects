import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(50, 100)  # Simulating exam evaluation with a random score


class Student(Person):

    def __init__(self, name,classroom):
        super().__init__(name)
        self.marks = {} # "subject : marks"
        self.classroom= classroom
        self.__id=None
        self.subject_grade = {} # "subject : grade"
        self.grade= None

    def calculate_final_grade(self):
        
        sum = 0
        for grade in self.subject_grade.values():
          point = School.grade_to_gpa(grade)
          sum += point

        if sum == 0:
         gpa= 0.0
         self.grade = "F"
        else:
         gpa = sum / len(self.subject_grade)
         self.grade = School.gpa_to_grade(gpa)
         return f"{self.name} Final Grade : {self.grade} with GPA = {gpa:.2f}"



    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id( self,value):

        self.__id = value






        