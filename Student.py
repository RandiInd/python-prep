class Student:
    def __init__(self, name, major, gpa, is_on_probation):  #constructor
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_special_degree(self):
        return self.gpa > 3.5