raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

PASSING_GRADE = 75

student_scores = {}

for record in raw_records:
    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0]

    try:
        scores = [int(fields[1]), int(fields[2]), int(fields[3])]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores


print("\nORGANIZED STUDENT RECORDS")

for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")


ranking = []
passed_count = 0
failed_count = 0
sum_of_averages = 0

for name, scores in student_scores.items():
    if len(scores) == 0:
        print(f"Skipped student with no scores: {name}")
        continue

    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    sum_of_averages += average
    ranking.append((average, name, highest_score, lowest_score, remark))


ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5} {name:<10} {average:<8.2f} {highest_score:<8} {lowest_score:<7} {remark}")
    

if len(student_scores) > 0:
    class_average = sum_of_averages / len(student_scores)
else:
    class_average = 0

print("\nCLASS SUMMARY")
print(f"Number of Students: {len(student_scores)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

if len(ranking) > 0:
    highest_student = ranking[0]
    lowest_student = ranking[-1]
    print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
    print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")