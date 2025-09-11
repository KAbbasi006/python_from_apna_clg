# traffic light example 

# light = input("Light: ").lower()

# if light =="red":
#     print("Stop")
# elif light == "green":
#     print("Go")
# elif light == "yellow":
#     print("Wait")
# else:
#     print("Light is broken 🙁")



# # Grades of Students
# marks = float(input("Enter your marks: "))
# if (marks>= 90):
#     print("A")
# elif (marks >=80 and marks<90):
#     print("B")
# elif(marks>= 70 and marks < 80):
#     print("C")
# else:
#     print("D")


# # practice question 
# # A = 5       G = M
# # A = 2       G = F
# A = int(input("A: "))
# G = input("M/F: ")
# if ((A == 1 or A == 2) and (G == "M")):
#     print("Fee is 100")
# elif(A == 3 or A == 4 or G == "F"):
#     print("Fee is 200")
# elif(A == 5 and G == "M"):
#     print("Fee is 300")
# else:
#     print("No fee")

     
# ------------------------------- Ternary Operator --------------------------------------------

1.          #Single line IF 

# # <var> = <val> if <condition> else <val2>
# food = input("Food: ")
# eat = "Yes" if food == "cake" else "no"
# print(eat)

# # <stt1> if <condition> else <stt2>
# food = input("Fod: ")
# print("sweet! 😋") if food == "cake" or food == "jalebi"  else print("not sweet! 😞")




2.          # Clever IF 
# <var> = (false_val , true_val) [<condition>]

# age = int(input("Enter your age: "))
# vote = ("Not eligible", "You can vote! 🙂") [age >=18]
# print(vote)


# sal = float(input("Salary: "))
# tax = sal*(0.1, 0.2) [sal > 50000]
# print(tax)



# age = 21
# if (age >= 18):
#     print("You are eligible to apply for liscence.")



# we can also use if if if instead of using elif
# -------------if ------------                     ------------elif------------
# jitny bhi "if" hongy wo sb check hongy.        agr if satify nhi kryga condition tou elif pr ayega. warna nhi

# Example:
# marks = float(input("Enter your marks: "))
# if(marks>=90):
#     print("Grade A")
# elif(marks >=80 and marks <90):
#     print("Grade B")
# elif(marks>=70 and marks <80):
#     print("Grade C")
# elif(marks >= 60 and marks <70):
#     print("Grade D")
# else:
#     print("Fail")


# marks = float(input("Enter your marks: "))
# if(marks>=90):
#     grade = "A"
# elif(marks >=80 and marks <90):
#     grade = "B"
# elif(marks>=70 and marks <80):
#     grade = "C"
# elif(marks >= 60 and marks <70):
#     grade = "D"
# else:
#     grade = "Fail"
# print("Grade of the student:->", grade)



# # ----------------------------Nested If -------------------------------
# age = int(input("Enter your age: "))
# if age >= 18:
#     if (age >=80):
#         print("You should not drive....")
#     else:
#         print("You can drive")
# else:
#     print("Not allowed to drive!")


# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# third = int(input("Enter third number: "))

# if (first >= second and first >= third):
#     print(first, "is the greatest number.")
# elif (second >= first and second >= third):
#     print(second, "is the greatest number.")
# else: 
#     print(third, "is the greatest number.")







