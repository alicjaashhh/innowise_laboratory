def add_new_student(students):
    name = input("Enter student name: ")

    if not name:
        print("Invalid student name!")
        return

    for student in students:
        if student['name'] == name:
            print(f"Student '{name}' already exists!")
            return

    students.append({
        'name': name,
        'grades': []
    })
    print(f"Student '{name}' added successfully!")


def add_grades_for_student(students):
    if not students:
        print("No students available. Please add a student first.")
        return

    name = input("Enter student name: ")

    student_found = None
    for student in students:
        if student['name'] == name:
            student_found = student
            break

    if not student_found:
        print(f"Student '{name}' not found!")
        return

    print(f"Adding grades for {name}. Enter grades one by one (0-100) or 'done' to finish:")

    while True:
        grade_input = input("Enter grade: ")

        if grade_input == 'done':
            break

        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                student_found['grades'].append(grade)
                print(f"Grade {grade} added successfully.")
            else:
                print("Error: Grade must be between 0 and 100!")
        except ValueError:
            print("Error: Please enter a valid number or 'done' to finish!")

    print(f"Finished adding grades for {name}. Current grades: {student_found['grades']}")


def calculate_average(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return None


def show_report(students):
    if not students:
        print("No students available.")
        return

    print("\n--- Student Report ---")

    averages = []
    valid_averages = []

    for student in students:
        avg = calculate_average(student["grades"])

        if avg is None:
            print(f"{student['name']}'s average grade is N/A (no grades)")
            averages.append(None)
        else:
            formatted_avg = f"{avg:.1f}"
            print(f"{student['name']}'s average grade is {formatted_avg}")
            averages.append(avg)
            valid_averages.append(avg)

    if not valid_averages:
        print("\nNo students have grades to calculate statistics.")
        return

    max_avg = max(valid_averages)
    min_avg = min(valid_averages)
    overall_avg = sum(valid_averages) / len(valid_averages)

    print(f"\n--- Summary ---")
    print(f"Maximum average: {max_avg:.1f}")
    print(f"Minimum average: {min_avg:.1f}")
    print(f"Overall average: {overall_avg:.1f}")


def find_top_performer(students):
    if not students:
        print("No students available.")
        return

    students_with_grades = []
    for student in students:
        avg = calculate_average(student["grades"])
        if avg is not None:
            students_with_grades.append((student, avg))

    if not students_with_grades:
        print("No students have grades to determine top performer.")
        return

    try:
        top_student = max(students_with_grades, key=lambda x: x[1])
        print(f"Top performer: {top_student[0]['name']} with average grade {top_student[1]:.1f}")
    except ValueError:
        print("Error finding top performer.")


def main():
    students = []

    while True:
        try:
            print("\n--- Student Grade Analyzer ---")
            print("1. Add a new student")
            print("2. Add grade for a student")
            print("3. Show report (all students)")
            print("4. Find top performer")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                add_new_student(students)
            elif choice == "2":
                add_grades_for_student(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-5.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()





