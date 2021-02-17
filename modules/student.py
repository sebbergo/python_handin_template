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
        grade_list = self.data_sheet.get_grades_as_list()

        for element in grade_list:
            total_grades += element.grade

        avg_grade = total_grades / len(grade_list)

        return avg_grade


def generate_students(number):
    course_names = ["Security", "Typescript", "Kotlin"]
    genders = ["male", "female"]
    grades = ["-3", "00", "02", "4", "7", "10", "12"]

    for x in range(0, number):
        with open("week3.csv", "a") as file_obj:
            name = names.get_full_name()
            image_url = "".join(
                random.choice(string.ascii_lowercase) for i in range(15)
            )
            course = Course(
                random.choice(course_names),
                "D klassen",
                "Thomas",
                "20",
                random.choice(grades),
            )
            data_sheet = DataSheet([course])
            student = Student(name, random.choice(genders), data_sheet, image_url)
            text_to_file = "Student name: {stud_name}, gender: {stud_gender}, course name: {course_name}, teacher: {teacher}, etcs: {etcs}, classroom: {classroom}, grade: {grade}, image_url: {image_url}".format(
                stud_name=student.name,
                stud_gender=student.gender,
                course_name=course.name,
                teacher=course.teacher,
                etcs=course.etcs,
                classroom=course.classroom,
                grade=course.grade,
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
            course = line.split("course name: ")[1].split(", ")[0]
            teacher = line.split("teacher: ")[1].split(", ")[0]
            etcs = line.split("etcs: ")[1].split(", ")[0]
            classroom = line.split("classroom: ")[1].split(", ")[0]
            grade = line.split("grade: ")[1].split(", ")[0]
            image_url = line.split("image_url: ")[1]

            course = Course(course, classroom, teacher, etcs, int(grade))
            data_sheet = DataSheet(courses=[course])
            student = Student(name, gender, data_sheet, image_url)

            new_list.append(student)

    return new_list
