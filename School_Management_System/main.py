from school import School
from person import Student
from person import Teacher 
from classroom import Classroom
from subject import subject


school = School("ABC", "Dhaka")

# Adding Classroom
eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding Student
rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

# Adding Teachers
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")

# Adding Subjects
# 8th Grade
eight.add_subject(subject("Bangla", abul))
eight.add_subject(subject("Physics", babul))
eight.add_subject(subject("Chemistry", kabul))

# 9th Grade
nine.add_subject(subject("Biology", kabul))
nine.add_subject(subject("Physics", babul))
nine.add_subject(subject("Chemistry", kabul))

# 10th Grade
ten.add_subject(subject("Chemistry", kabul))
ten.add_subject(subject("Physics", babul))
ten.add_subject(subject("Bangla", abul))
ten.add_subject(subject("Biology", kabul))


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)





