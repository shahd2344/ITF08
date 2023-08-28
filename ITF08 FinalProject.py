#ITF 08 Final Project
import random
#TODO 1 Enter your name and submission date

print("shahd abu oudah")
print("Enter submission date")

# in Global Scope
student_list = []


def add_new_std():

    student_name = input("Enter Student Name: ")
    while True:
        try:
            student_age = int(input("Enter Student Age: "))
            break  # Exit the while loop if a valid integer is entered
        except:
            print("Invalid Value")
    # Create student object and append it to students list
    student = Student(student_name, student_age, student_number)
    student_list.append(student)

    print("Student Added Successfully")


def delete():
    input_student_number = input("Enter Student Number: ")
    found = False
    for student in student_list:
        if student.student_number == input_student_number:
            student_list.remove(student)
            print("Student Deleted")
            found = True
            break

    if not found:
        print("Student Not Exist")



# TODO 2 Define Course Class and define constructor with (course_id generated ,course name (user_input) and
# course mark

class Course:

 def __init__(self, course_name, course_mark):
  self.course_id = generate_course_id(self)
  self.course_name = course_name
  self.course_mark = course_mark
#a unique course ID as a counter
course_id_counter = 0

def generate_course_id(self):
    global course_id_counter
    course_id_counter += 1
    return course_id_counter
class Student:
   # static variable indicates total student count
    total_student_count = 1
  # a constructor which includes
    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(1000,9999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        self.total_student_count = Student.total_student_count
        Student.total_student_count+=1

 # enroll new course to student courses list
def add_course():
    input_student_number = input("Enter Student Number: ")
    for student in student_list[:]:
        if student_number== input_student_number:
            course_name = input("Enter name of course: ")
            course_mark = float(input("Enter mark for course: "))
            course = Course(course_name, course_mark)
            student.courses_list.append(course)
            print("Course Added to Student Successfully")
            break
    else:
        print("Student Not Exist")



# method to get_student_details as dict
def get_student_details(self):
    details = {
        "Student ID": self.student_id,
        "Name": self.student_name,
        "Age": self.student_age,
        "Student Number": self.student_number,
        "Courses": [course.course_name for course in self.courses_list]
    }
    return details
# method to get_student_courses
def get_student_courses(self):
    for course in self.courses_list[:]:
        print(f"Course: {course.course_name}, Mark: {course.course_mark}")
 # method to get student_average as a value
def get_student_average(self):
    if len(self.courses_list) == 0:
        return 0  # Return 0 if there are no courses

    total = 0  # Initialize a variable to store the total marks
    for course in self.courses_list[:]:
        total+= course.course_mark

    average = total/ len(self.courses_list)
    return average

def find_std(student_number):
    found=False
    if len(student_list)==0:

        return found
    for student in student_list:
        if student.student_number==student_number:
            found =True


    return found
while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except:
        print("Invalid input. Please enter a valid option.")
        continue  # Jump to the beginning of the loop (not exit)

    if selection == 1:
        student_number = input("Enter Student Number: ")
        if not find_std(student_number):

            add_new_std()

        elif find_std(student_number):
          print("student alreagy exists")

    elif selection == 2:
       delete()


    elif selection == 3:

        # Display Student Details

        # Display Student Details
        input_student_number = input("Enter Student Number: ")
        for student in student_list:
            if student_number == input_student_number:
                details = get_student_details(student)

                print("Student Details:")

                print(details)

                break

        else:

            print("Student Not Exist")

    elif selection == 4:
         student_number = input("Enter Student Number: ")
         for student in student_list[:]:
             if student.student_number == student_number:
                 average = get_student_average(student)
                 print(f"Student Average: {average}")
                 break
         else:
             print("Student Not Exist")
    elif selection == 5:
     add_course()

    else:
     # TODO 15 call a function to exit the program
         print("exiting the program")
         exit()
