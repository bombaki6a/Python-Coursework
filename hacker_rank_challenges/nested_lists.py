if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key=lambda x: x[1])
    students = list([student for student in students if (students[0][1] != student[1])])
    students = list([student for student in students if (students[0][1] == student[1])])
    students = sorted(students, key=lambda x: x[0])

    print("\n".join(student[0] for student in students))

