
class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        avg_grade = 0
        total_grades = 0
        grade_list = self.data_sheet.get_grades_as_list()

        for element in grade_list:
            total_grades += element.grade
        
        avg_grade = total_grades/len(grade_list)
        
        return avg_grade