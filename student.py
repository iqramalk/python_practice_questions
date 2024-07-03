students=[{'id':1 ,'name':'Iqra Asad' ,'age':'21' , 'major': 'Astronomy'},
          {'id':2 ,'name':'sara Khan' ,'age':'22' , 'major': 'Microbiology'},
          {'id':3 ,'name':'Samaira' ,'age':'21' , 'major': 'Mathematics'}
]
def student_add(students,student):
    return students.append(student)

def remove_student(students,student_id):
    students[:]= [s for s in students if s["id"] != student_id ]

def update_major(students,student_id,new_major):
    for student in students:
        if student['id'] == student_id:
            student["major"] = new_major

def display_student(students):
    for student in students:
        print(f"ID : {student['id']} , NAME : {student['name']} , AGE: {student['age']}, MAJOR: {student['major']}")

new_student={'id':4 ,'name':'Ibrahim' ,'age':'19' , 'major': 'Computer Science'}   
student_add(students,new_student)

remove_student(students,3)

update_major(students, 2 ,"Chemistry")

display_student(students)
