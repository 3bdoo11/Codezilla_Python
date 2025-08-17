def pirnt_student(name, grades, school = "Codezilla"):
    print(f"Student: {name.title()}")
    print(f"School: {school.title()}")
    print("Grades:")
    print("----------")
    for supject, score in grades.items():
        print(f"{supject.title()}: {score}")

name = "hamada codezilla"
grades = {
"math": 99,
"english": 98,
"science": 99,
"arabic": 100,
"history": 99
}
pirnt_student(name, grades)