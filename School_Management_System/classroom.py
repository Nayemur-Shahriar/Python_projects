from subject import subject
class Classroom:

    def __init__(self,name):
        self.name = name
        self.students = [] # List of Student objects
        self.subjects = [] # List of Subject objects

    def add_student(self, student):

        roll_no = len(self.students) + 1

        class_id= f"{student.name} --> {self.name} --> {roll_no}"
        student.id = class_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)

        for student in self.students:
            student.calculate_final_grade()