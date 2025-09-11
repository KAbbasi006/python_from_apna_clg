# # traffic light example 

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


# # Write a program to input two numbers and print their sum.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum = num1+ num2
# print("Sum: ", sum)



# # write a program to input side of a square and print its area
# side = float(input("Enter side of a square: "))
# area_of_sq = side * side
# print( "Area of square: ",area_of_sq)


# # Write a program to input two floating point numbers and print their averages.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# avg = (num1 + num2)/2
# print("Average of given numbers is: ",avg)


# # Write a program to input two int numbers, a and b.
# # Print "True" if a>=b if not print "False"
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# if a>=b:
#     print("True")
# else:
#     print("False")
#                 # ---------  or ---------

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print(a>=b)



# # Q. Write a program to input user's first name and print its length.

# naam = input("Enter your name: ")
# print("Length of your name is:", len(naam))


# #Q. Write a program to find the occurence of "$" in a string.
# str = "I have $5 amd i spent $$ $2"
# print(str.count("$"))



# # Write a program to print grade of student by taking user input.
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




# # Q. Write a program to check if a number entered by a  user is odd/even.
# num = int(input("Enter a number: "))
# if (num % 2 == 0):
#     print(num, "is an Even number")
# else:
#     print(num, "is an Odd number")




# # Q. Write a program to find greatest of 3 numbers entered by the user.
# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# third = int(input("Enter third number: "))

# if (first >= second and first >= third):
#     print(first, "is the greatest number.")
# elif (second >= first and second >= third):
#     print(second, "is the greatest number.")
# else: 
#     print(third, "is the greatest number.")




# # WAP to check if a number is a multiple of 7 or not?
# numm = int(input("Enter a number: "))
# if (numm % 7 == 0):
#     print(numm, "is a multiple of 7 ✅")
# else: 
#     print(numm, "is not a multiple of 7 ❌")






# Q. WAP to ask the user to enter names of their 3 fav movies and store them in a list.

# # Solution 1            --------BETTER -----
# a = input("Enter your first favourite movie name: ")
# b = input("Enter your second favourite movie name: ")
# c = input("Enter your third favourite movie name: ")
# abc = [a, b, c]
# print(abc)

# # Solution 2            --------BEST-----✅✅✅✅✅✅✅✅✅
# movies = []
# mov1 = input("Enter your first favourite movie name: ")
# mov2 = input("Enter your second favourite movie name: ")
# mov3 = input("Enter your third favourite movie name: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# # Solution 3            --------BESt -----✅✅✅✅✅✅✅✅✅
# movies = []
# mov = input("Enter your first favourite movie name: ")
# movies.append(mov)
# mov = input("Enter your second favourite movie name: ")
# movies.append(mov)
# mov = input("Enter your third favourite movie name: ")
# movies.append(mov)
# print(movies)

# # Solution 4            --------BEST -----✅✅✅✅✅✅✅✅✅
# movies = []
# movies.append(input("Enter your first favourite movie name: "))
# movies.append(input("Enter your second favourite movie name: "))
# movies.append(input("Enter your third favourite movie name: "))
# print(movies)






# Q. WAP to check if a list contains a "Palindrome" of elts.(hint: use copy() method)  
# example:    ma'am      racecar        maham
# to check for list  ------------->>     [1, 2, 3, 2, 1]     [1, "ab", 2, "ab", 1]
# #  Solution:

# a =  [1, 2, 3, 2, 1, 8] 
# copy_a = a.copy()
# copy_a.reverse()
# if (copy_a == a):
#     print("Palindrome ✅")
# else:
#     print("Not a palindrome ❌❌❌❌")




# list1 = [1, "ab", 2, "ab", 1]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not a palindrme")




# Q. WAP to count no of students with the "A" grade in the following tuple 
#then store the values in list
# then sort them from "A"  to "D"

# # Solution
# grade = ("A","A", "B", "D",  "B","C",  "A", "B", "D",  "B","C" ,"A","B")
# print(grade.count("A")) # 4

# a = list(grade)
# print(a)

# a.sort()
# print(a)

