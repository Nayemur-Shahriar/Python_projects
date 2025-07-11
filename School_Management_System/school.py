class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # "subject : obj"
        self.classrooms = {} # "class_name : obj"

   
    def add_teacher(self,subject, teacher):
        self.teachers[subject] = teacher

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod

    def calculate_grade(marks):
        if marks >= 90:
            return 'A+'
        elif marks >= 80:
            return 'A'
        elif marks >= 70:
            return 'B'
        elif marks >= 60:
            return 'C'
        elif marks >= 50:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_gpa(grade):
        grade_map ={
            'A+': 4.0,
            'A': 3.75,
            'B': 3.0,
            'C': 2.5,
            'D': 2.0,
            'F': 0.0
        }
        return grade_map[grade]
    
    @staticmethod
    def gpa_to_grade(gpa):
        if gpa >= 3.75:
            return 'A+'
        elif gpa >= 3.0:
            return 'A'
        elif gpa >= 2.5:
            return 'B'
        elif gpa >= 2.0:
            return 'C'
        elif gpa >= 1.0:
            return 'D'
        else:
            return 'F'
        

    def __repr__(self):
        # All Classrooms
        for key in self.classrooms.keys():
            print(key)
        # All Students
        print("All Students")
        result = ''
        for key,value in self.classrooms.items(): # prottekta classroom e gelam
            result += f"---{key.upper()} Classroom Students\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)
        # All Subjects
        subject = ''
        for key,value in self.classrooms.items(): # prottekta classroom e gelam
            subject += f"---{key.upper()} Classroom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)
        # All Teachers - Homework
        # All Student Results
        print("Students Results")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.calculate_final_grade())
        return ''