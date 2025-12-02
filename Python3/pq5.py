stu_marks_info = {}
print(type(stu_marks_info))
def add_student():
    name = input("Enter student name : ")
    marks = input("Enter student marks : ")
    stu_marks_info[name] = marks
def update_marks():
    name = input("Enter student name : ")
    marks = input("Enter student marks to update: ")
    stu_marks_info[name] = marks
def search_for_student():
    name = input("Enter student name : ")
    for key, value in stu_marks_info.items():
        if(key == name):
            print("Student found!!!\n")
def display_all_student_marks():
    for key, value in stu_marks_info.items():
        print(f"student name : {key}, marks are {value}")
while(True):
    val = input('''Enter A -> To add a student
                   B -> To update marks of a student
                   C -> Search for a student
                   D -> Display all students and marks
                   ''')
    match val:
        case 'A':
            add_student()
        case 'B':
            update_marks()
        case 'C':
            search_for_student()
        case 'D':
            display_all_student_marks()


