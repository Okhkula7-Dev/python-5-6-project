
print("===== STUDENT ADMISSION SYSTEM =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

exam_taken = input("Did you take the entrance exam? (yes/no): ").lower()

if age >= 18 and age <= 30:

    if exam_taken == "yes":

        score = float(input("Enter your exam score (0-100): "))

        if score >= 0 and score <= 100:

            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 50:
                grade = "D"
            else:
                grade = "F"

            documents = input(
                "Are your documents complete? (yes/no): "
            ).lower()

            if score >= 50 and documents == "yes":
                print("\nCongratulations!")
                print("Name:", name)
                print("Grade:", grade)
                print("Admission Status: Accepted")

            elif score >= 50 and documents == "no":
                print("You passed, but your documents are incomplete.")

            else:
                print("Sorry! You failed the entrance exam.")

        else:
            print("Invalid score! Enter a number between 0 and 100.")

    else:
        print("You must take the entrance exam first.")

else:
    print("Sorry! Your age is not eligible.")

print("\nThank you for using our system!")
