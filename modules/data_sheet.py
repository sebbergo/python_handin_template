class DataSheet:
    def __init__(self, courses=[]):
        self.courses = courses

    def get_courses_as_list(self):
        new_list = list([])
        for element in self.courses:
            new_list.append(element)

        return new_list
