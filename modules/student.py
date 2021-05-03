import names
import random
import string
import csv
from modules.course import Course
from modules.data_sheet import DataSheet


class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.image_url = image_url
        self.data_sheet = data_sheet

    def get_avg_grade(self):
        avg_grade = 0
        total_grades = 0
        grade_list = self.data_sheet.get_courses_as_list()

        for element in grade_list:
            total_grades += int(element.grade)

        avg_grade = total_grades / len(grade_list)

        return avg_grade

    def prog_of_study_in_proc(self):
        result = 0
        total_etcs = 0
        course_list = self.data_sheet.get_courses_as_list()

        for element in course_list:
            total_etcs += int(element.etcs)
        
        result = (total_etcs/150) * 100

        return result

def distribute_etcs(array):
    result = []
    tens = 0
    twenties = 0
    thirdies = 0
    fourties = 0
    fifties = 0
    sixties = 0
    seventies = 0
    eighties = 0
    nineties = 0

    for student in array:
        etcs = student.prog_of_study_in_proc()

        if etcs < 10:
            tens + 1
        if etcs < 20 and etcs > 10:
            twenties + 1
        if etcs < 30 and etcs > 20:
            thirdies + 1
        if etcs < 40 and etcs > 30:
            fourties + 1
        if etcs < 50 and etcs > 40:
            fifties + 1
        if etcs < 60 and etcs > 50:
            sixties + 1
        if etcs < 70 and etcs > 60:
            seventies + 1
        if etcs < 80 and etcs > 70:
            eighties + 1
        if etcs < 90 and etcs > 80:
            nineties + 1

    result.append(tens)
    result.append(twenties)
    result.append(thirdies)
    result.append(fourties)
    result.append(fifties)
    result.append(sixties)
    result.append(seventies)
    result.append(eighties)
    result.append(nineties)

    return result


def generate_students(number):
    course_names = ["Security", "Typescript", "Kotlin"]
    genders = ["male", "female"]
    grades = ["-3", "00", "02", "4", "7", "10", "12"]
    etcs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
    classRoom = ["A", "B", "C", "D", "E", "F"]
    teacher = ["Thomas", "Daniel", "Lars", "Jon", "Nikolai", "Palle"]

    for x in range(0, number):
        with open("week3.csv", "a") as file_obj:
            name = names.get_full_name()
            image_url = "".join(
                random.choice(string.ascii_lowercase) for i in range(15)
            )

            courses = list([])
            for x in range(0, 5):
                course = Course(
                    random.choice(course_names),
                    random.choice(classRoom),
                    random.choice(teacher),
                    random.choice(etcs),
                    random.choice(grades),
                )
                
                courses.append(course)

            data_sheet = DataSheet(courses)

            student = Student(name, random.choice(genders), data_sheet, image_url)

            text_to_file = "Student name: {stud_name}, gender: {stud_gender}, course name: {course_name}, teacher: {teacher}, etcs: {etcs}, classroom: {classroom}, grade: {grade}, image_url: {image_url}".format(
                stud_name=student.name,

                stud_gender=student.gender,

                course_name = data_sheet.courses[0].name + ", " +
                data_sheet.courses[1].name + ", " +
                data_sheet.courses[2].name + ", " +
                data_sheet.courses[3].name + ", " +
                data_sheet.courses[4].name,

                teacher=data_sheet.courses[0].teacher + ", " +
                data_sheet.courses[1].teacher + ", " +
                data_sheet.courses[2].teacher + ", " +
                data_sheet.courses[3].teacher + ", " +
                data_sheet.courses[4].teacher,

                etcs=data_sheet.courses[0].etcs + ", " +
                data_sheet.courses[1].etcs + ", " +
                data_sheet.courses[2].etcs + ", " +
                data_sheet.courses[3].etcs + ", " +
                data_sheet.courses[4].etcs,

                classroom=data_sheet.courses[0].classroom + ", " +
                data_sheet.courses[1].classroom + ", " +
                data_sheet.courses[2].classroom + ", " +
                data_sheet.courses[3].classroom + ", " +
                data_sheet.courses[4].classroom,

                grade=data_sheet.courses[0].grade + ", " +
                data_sheet.courses[1].grade + ", " +
                data_sheet.courses[2].grade + ", " +
                data_sheet.courses[3].grade + ", " +
                data_sheet.courses[4].grade,

                image_url=student.image_url,
            )

            file_obj.write(text_to_file + "\n")


def csv_to_list(imported_file):
    new_list = list([])

    with open(imported_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            name = line.split("Student name: ")[1].split(", ")[0]
            gender = line.split("gender: ")[1].split(", ")[0]
            course_names = (line.split("course name: ")[1].split(", t")[0]).split(",")
            teachers = (line.split("eacher: ")[1].split(", e")[0]).split(",")
            all_etcs = (line.split("tcs: ")[1].split(", c")[0]).split(",")
            classrooms = (line.split("lassroom: ")[1].split(", g")[0]).split(",")
            grades = (line.split("rade: ")[1].split(", i")[0]).split(",")
            image_url = line.split("mage_url: ")[1]

            courses = []

            for x in range(0, 5):
                courses.append(Course(course_names[x], classrooms[x], 
                teachers[x], all_etcs[x], grades[x]))

            data_sheet = DataSheet(courses)
            student = Student(name, gender, data_sheet, image_url)

            new_list.append(student)

    return new_list