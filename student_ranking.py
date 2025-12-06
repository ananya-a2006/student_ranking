# student_ranking.py

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.total = m1 + m2 + m3

    def __repr__(self):
        return f"{self.name} - Total: {self.total}"


def get_students():
    students = []
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        name = input("Enter name: ")
        m1 = int(input("Enter mark in Subject 1: "))
        m2 = int(input("Enter mark in Subject 2: "))
        m3 = int(input("Enter mark in Subject 3: "))

        students.append(Student(name, m1, m2, m3))
    return students


def rank_students(students):
    # Custom sorting rule:
    # 1. Higher total marks first  (descending)
    # 2. If totals are equal, sort by name (ascending)
    return sorted(students, key=lambda s: (-s.total, s.name))


def display_ranking(sorted_students):
    print("\n===== Student Ranking =====")
    print("{:<6} {:<15} {:<8} {:<8} {:<8} {:<8}".format(
        "Rank", "Name", "Sub1", "Sub2", "Sub3", "Total"
    ))
    print("-" * 60)

    rank = 1
    for s in sorted_students:
        print("{:<6} {:<15} {:<8} {:<8} {:<8} {:<8}".format(
            rank, s.name, s.m1, s.m2, s.m3, s.total
        ))
        rank += 1


def main():
    students = get_students()
    sorted_students = rank_students(students)
    display_ranking(sorted_students)


if __name__ == "__main__":
    main()
