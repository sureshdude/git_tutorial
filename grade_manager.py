
# Student Grade Manager

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "E"


def main():
    students = []

    print("===== Student Grade Manager =====")

    number_of_students = int(input("Enter number of students: "))

    for i in range(number_of_students):
        print(f"\nStudent {i + 1}")

        name = input("Enter student name: ")
        marks = float(input("Enter marks (0-100): "))

        grade = calculate_grade(marks)

        students.append({
            "name": name,
            "marks": marks,
            "grade": grade
        })

    print("\n========== STUDENT GRADE REPORT ==========")
    print(f"{'Name':<20} {'Marks':<10} {'Grade':<10}")
    print("-" * 40)

    for student in students:
        print(
            f"{student['name']:<20} "
            f"{student['marks']:<10.2f} "
            f"{student['grade']:<10}"
        )


if __name__ == "__main__":
    main()
