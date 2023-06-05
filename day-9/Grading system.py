student_scores={'Harry':81,
                'Ron':78 , 
                'Hermoine':99,
                'Draco':74,
                'Neville':62}

student_grades={} # to make a empty dictionary!

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "outstanding" # TO add into an empty dictionary!

    elif student_scores[key] > 80 and student_scores[key]<90:
        student_grades[key] = "Exceeds Expectations"

    elif student_scores[key] >70 and student_scores[key] <80:
        student_grades[key] = "Acceptable"

    else:
        student_grades[key] = "Failure"

print(student_grades)