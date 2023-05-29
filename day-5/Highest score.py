student_score=input("input a list of student score ").split()
for n in range(0, len(student_score)):
    student_score [n]= int(student_score[n])
print(student_score)

max_score = 0
for i in student_score:
    if i>max_score:
        max_score=i
print(f"the highest score in the class is :{max_score}") 