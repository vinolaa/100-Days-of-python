student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

heights_sum = 0
for a in student_heights:
    heights_sum += a
media = round(heights_sum / (n + 1))
print(media)

