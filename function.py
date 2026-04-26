class course:
    def __init__(self,course_name,price):
        self.course_name=course_name
        self.price=price
    def show_course(self):
        print(self.course_name)
        print(self.price)

class prolanguage(course):
    def __init__(self,course_name,price,language,duration):
        super().__init__(course_name,price)
        self.language=language
        self.duration=duration
    def show_program_course(self):
        super().show_course()
        print(self.language)
        print(self.duration)
c1=prolanguage("python program",15000,"python","3months")
c2=prolanguage("java program",12000,"java","2months")
c1.show_program_course()
c2.show_program_course()