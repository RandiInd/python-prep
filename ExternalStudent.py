from Student import Student


class ExternalStudent(Student):
    def __init__(self, name, major, gpa, is_on_probation, fee):  #constructor
        self.fee = fee
        super().__init__(name, major, gpa, is_on_probation)
    def get_class_fee(self):
        return self.fee * self.gpa
