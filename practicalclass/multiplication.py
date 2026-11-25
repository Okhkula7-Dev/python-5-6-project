# number = 5

# for x in range(1, 10):
#     result = number * x
#     print(f"{number} x {x} = {result}")     

# for i in range(1, 10):

#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

#     print("----------------")

subjects = ["Python", "HTML", "CSS"]

total_students = int(input("How many students? "))

for student_number in range(1, total_students + 1):

    print("\nStudent Number:", student_number)

    name = input("Enter student name: ")

    if name == "":
        print("Name is empty. Skipping student.")
        continue

    total_marks = 0

    for subject in subjects:

        while True:

            mark = int(input(f"Enter {subject} mark: "))

            if 0 <= mark <= 100:
                break

            print("Invalid mark! Enter a number between 0 and 100.")

        total_marks += mark

    average = total_marks / len(subjects)

    print("\nStudent Name:", name)
    print("Total Marks:", total_marks)
    print("Average:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    print("-----------------------------")

print("All students have been processed!")