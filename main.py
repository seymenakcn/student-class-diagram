class Program:

    def __init__(self, program_id, program_name, faculty_name):
        self.program_id = program_id
        self.program_name = program_name
        self.faculty_name = faculty_name


class Instructor:

    def __init__(self, instructor_id, instructor_name, email):
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name
        self.email = email

    def assign_course(self, course):
        course.instructor = self
        print(self.instructor_name, "assigned to", course.course_name)


class Course:

    def __init__(self, course_id, course_name, credit_hours):
        self.course_id = course_id
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.instructor = None


class Student:

    def __init__(self, student_no, full_name, email, program):
        self.student_no = student_no
        self.full_name = full_name
        self.email = email
        self.program = program
        self.registered_courses = []

    def add_course(self, course):
        if course not in self.registered_courses:
            self.registered_courses.append(course)
            print(course.course_name, "added successfully.")

    def calculate_total_credits(self):
        total = 0

        for course in self.registered_courses:
            total += course.credit_hours

        return total



program1 = Program(
    "P101",
    "Software Engineering",
    "Engineering Faculty"
)

instructor1 = Instructor(
    501,
    "John Smith",
    "john@example.com"
)

course1 = Course("C101", "Programming", 4)
course2 = Course("C102", "Database Systems", 3)
course3 = Course("C103", "Software Engineering", 3)

instructor1.assign_course(course1)
instructor1.assign_course(course2)
instructor1.assign_course(course3)

student1 = Student(
    202501,
    "Ahmet Yilmaz",
    "ahmet@example.com",
    program1
)

student1.add_course(course1)
student1.add_course(course2)
student1.add_course(course3)

print("\n--- Student Information ---")
print("Student No:", student1.student_no)
print("Full Name:", student1.full_name)
print("Email:", student1.email)
print("Program:", student1.program.program_name)

print("\n--- Registered Courses ---")

for course in student1.registered_courses:
    print("Course:", course.course_name)
    print("Credits:", course.credit_hours)
    print("Instructor:", course.instructor.instructor_name)
    print("--------------------")

print("Total Credits:", student1.calculate_total_credits())
