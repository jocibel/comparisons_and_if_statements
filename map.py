class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.46), Student("Jane", 0.84), Student("Sarah", 0.63)]

student_results = []
for student in students:
    if  student.score >= 0.7:
        student_results.append(f"{student.name} Passed")
    else: 
        student_results.append(f"{student.name} Failed")

     # can be down the way above or like this---->>> student_results.append(f"{student.name} Passed") if  student.score >= 0.7 else student_results.append(f"{student.name} Failed")

map_results = list(map(lambda student:f"{student.name} Passed" if student.score >= 0.7 else f"{student.name} Failed", students))

print(map_results)

