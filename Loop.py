num_of_std=int(input("Enter number of students"))
for i in range(0,num_of_std):
    num_of_marks=int(input(f"Enter number of {i+1} stduent marks"))
    student_marks = []
    sum=0
    for i in range(0,num_of_marks):

     mark=int(input(f"Enter mark{i+1}"))
     student_marks.append(mark)
     sum += student_marks[i]

    print("student marks:",student_marks)
    print("average=",round(sum / len(student_marks),2))
    print("max=",max(student_marks))
    print("min=",min(student_marks))