student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

high_score = 0
for high in student_scores:
    if high > high_score:
        high_score = high
print(f"The highest score in the class is: {high_score}")

