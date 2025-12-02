info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
#List all unique courses
def find_unique_courses(info):
    unique_courses = set()
    print(type(unique_courses))
    for tup in info:
        unique_courses.add(tup[1])
    print(unique_courses)
    return unique_courses

def list_students_inEnglish(info):
    in_english = []
    for tup in info:
        if(tup[1] == "English"):
            in_english.append(tup[0])
    print(in_english)
    return in_english

def create_student_set_courses(info):
    stu_set_courses = {}
    for tup in info:
        name = tup[0]
        subject = tup[1]
        if(name in stu_set_courses):
            stu_set_courses[name].add(subject)
        else:
            subjects = set()
            subjects.add(subject)
            stu_set_courses[name] = subjects
    print(stu_set_courses)
    return stu_set_courses
    

print(f"All the unique courses are : {find_unique_courses(info)}")
print(f"List of all the students enrolled  in English are : {list_students_inEnglish(info)}")
print(f"Student and the set of courses enrolled are : {create_student_set_courses(info)}")