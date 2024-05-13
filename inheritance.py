class person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking")
    def talk(self):
        print(f"{self.name} is talking")
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class teacher(person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
    def grade_students(self):
        print(f"{self.name} is grading students")
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting")

class student(person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying")
    def attend_class(self):
        print(f"{self.name} is attending class")
    def write_exam(self):
        print(f"{self.name} is writing exam")

# creating objects
teacher1 = teacher("Mr. Sangay", 30, "S156", "Math", 40000, "Mathematics", "Head of ECE")     
student1 = student("Yeshi", 18, "W700", "T735", "ECE", 1, 4 )

# using ojjects
teacher1.walk()
teacher1.talk()
teacher1.teach()
student1.walk()
student1.study()
student1.write_exam()




