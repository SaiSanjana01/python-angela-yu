student_height=input("Input a list of students heights ").split()

for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

total_height=0
for height in student_height:
    total_height+=height
# print(total_height)

number_of_student=0
for student in student_height:
    number_of_student+=1 #iterates till the students ie 5
# print(number_of_student)

average=round(total_height/number_of_student)
print(average)