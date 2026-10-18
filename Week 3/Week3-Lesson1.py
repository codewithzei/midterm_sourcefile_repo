scores = [75, 67, 94, 85, 63]

print("Student Scores:")

for score in scores:
    print(score)

print()

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

passed = 0
failed = 0

for x in range(len(scores)):
    score = scores[x]

    if score >= 75:
        if score >= 90:
            remark = "Excellent"
        elif score >= 80:
            remark = "Very Good"
        else: 
            remark = "Good"

        print(f"Student {x + 1}: {score} - {remark} - Passed!")
        passed += 1

    else:
        print(f"Student {x + 1}: {score} - Failed!")
        failed += 1

print()

print(f"Total Score: {total}")
print(f"Average Score: {average}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
