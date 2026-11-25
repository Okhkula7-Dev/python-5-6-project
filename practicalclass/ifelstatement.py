# get  name , and age
# check the age if it was iligable
# exam
# number of exam checked
# grade
# ducument check
# final decission
#


print("======== Student Admition System =======")
name = input("Please  Enter your name : ")
age = int(input("Please Enter your age : "))
tacken_exam = input("Did you take the exam please select : (yes / no ) : ").lower()
if age >= 18 and age <= 30:
    if tacken_exam == "yes":
        score = int(input("please enter you exam score (0-100) :"))
        if score >= 0 and score <= 100:
            if score >= 90:
                print("Grade A")
            elif score >= 80:
                print("Grade B ")
                
            
    elif tacken_exam == "no" and score >= 50:
        print("your are passe but you document is not apploded: ")
else:
    print("your age is not allowed: ")
