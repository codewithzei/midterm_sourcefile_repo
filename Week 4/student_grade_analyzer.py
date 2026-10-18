"""Student Grade Analyzer - Complete Solution

This program reads student records from grades.txt, analyzes the data,
and provides a menu-driven interface for viewing and reporting.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    if 90 <= grade <= 100:
        return "Excellent", "Passed"
    elif 85 <= grade <= 89:
        return "Very Good", "Passed"
    elif 80 <= grade <= 84:
        return "Good", "Passed"
    elif 75 <= grade <= 79:
        return "Satisfactory", "Passed"
    else:
        return "Needs Improvement", "Failed"


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(",")
                if len(parts) != 3:
                    continue
                
                try:
                    student_id = parts[0].strip()
                    name = parts[1].strip()
                    grade = float(parts[2].strip())
                    
                    if 0 <= grade <= 100:
                        students.append({
                            "student_id": student_id,
                            "name": name,
                            "grade": grade
                        })
                except ValueError:
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Please make sure the file exists in the same folder.")
    
    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    student_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        student_count += 1
        grade = student["grade"]
        total_grade += grade
        
        classification, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1
        
        if grade > highest_student["grade"]:
            highest_student = student
        
        if grade < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / student_count if student_count > 0 else 0
    
    return {
        "count": student_count,
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("No student records to display.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<12} {'Name':<25} {'Grade':<10} {'Classification':<20} {'Status':<10}")
    print("-"*80)
    
    for student in students:
        classification, status = classify_grade(student["grade"])
        
        name = student["name"]
        if len(name) > 25:
            name = name[:23] + ".."
        
        print(f"{student['student_id']:<12} "
              f"{name:<25} "
              f"{student['grade']:<10.2f} "
              f"{classification:<20} "
              f"{status:<10}")
    
    print("="*80 + "\n")


def display_statistics(statistics):
    """Display the calculated class statistics."""
    if not statistics:
        print("No statistics available.")
        return
    
    print("\n" + "="*40)
    print("CLASS STATISTICS")
    print("="*40)
    print(f"Number of students: {statistics['count']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    if statistics['highest']:
        print(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}")
    if statistics['lowest']:
        print(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}")
    print("="*40)


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []

    keyword = keyword.strip().lower()
    if not keyword:
        return matches
    
    for student in students:
        student_id_lower = student["student_id"].lower()
        name_lower = student["name"].lower()
        
        if keyword in student_id_lower or keyword in name_lower:
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    try:
        with open(filename, 'w') as file:
            file.write("="*80 + "\n")
            file.write("STUDENT GRADE REPORT\n")
            file.write("="*80 + "\n\n")
            
            file.write(f"{'ID':<12} {'Name':<25} {'Grade':<10} {'Classification':<20} {'Status':<10}\n")
            file.write("-"*80 + "\n")
            
            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(f"{student['student_id']:<12} "
                          f"{student['name']:<25} "
                          f"{student['grade']:<10.2f} "
                          f"{classification:<20} "
                          f"{status:<10}\n")
            
            file.write("\n" + "="*80 + "\n")
            file.write("CLASS STATISTICS\n")
            file.write("="*80 + "\n")
            file.write(f"Number of students: {statistics['count']}\n")
            file.write(f"Class average: {statistics['average']:.2f}\n")
            file.write(f"Passed: {statistics['passed']}\n")
            file.write(f"Failed: {statistics['failed']}\n")
            if statistics['highest']:
                file.write(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}\n")
            if statistics['lowest']:
                file.write(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}\n")
            
            print(f"Report successfully saved to '{filename}'")
            
    except OSError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"Unexpected error while saving report: {e}")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    print("Loading student data...")
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        print("Please check that grades.txt exists and contains valid records.")
        return

    print(f"\nSuccessfully loaded {len(students)} student records.")
    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        
        elif choice == "2":
            display_statistics(statistics)
        
        elif choice == "3":
            keyword = input("Enter student ID or name to search: ").strip()
            if keyword:
                results = search_student(students, keyword)
                if results:
                    print(f"\nFound {len(results)} matching student(s):")
                    display_students(results)
                else:
                    print(f"No students found matching '{keyword}'")
            else:
                print("Please enter a search term.")
        
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        
        elif choice == "5":
            print("\nThank you for using Student Grade Analyzer!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue


if __name__ == "__main__":
    main()