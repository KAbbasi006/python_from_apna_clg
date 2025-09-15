# Loops: are used to repeat instructions
# 2 types of loops  ----->                      1. while         2. for

# Q. print "hello" 5 times

# # # Solution 1:
# i=1    # iterator
# while i<=5:
#     print("Hello", i)
#     i +=1
# print(i)

# # Solution 2:
# for i in range(1, 6):
#     print("Hello", i)


# # Q. print numbers from 1 to 50
# i=1
# while i<=50:
#     print(i)
#     i +=1


# # Q. print numbers from 10 to 1
# i = 10
# while i>=1:
#     print(i)
#     i-=1
# print("Loop ended")


# --------------------------------------------Break ----------------------------------------
# Break is used to terminate the loop when encountered

# i = 1
# while i<=5:
#     print(i)
#     if (i == 3):
#         break
#     i+=1


# nums = [1, 2, 9, 16, 25, 36, 49, 64, 81, 100, 36]
# x = 36
# i = 0
# while i< len(nums):
#     if (nums[i] == x):
#         print("Found at index", i)
#     else:
#         print("Finding.....")
#     i +=1
# output: 
# Finding.....
# Finding.....
# Finding.....
# Finding.....
# Finding.....
# Found at index 5
# Finding.....
# Finding.....
# Finding.....
# Finding.....
# Found at index 10


# nums = (1, 2, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Found at index", i)
#         break
#     else:
#         print("Finding....")
#     i +=1







# ------------------------------------------Continue-----------------------------------------
# Continue terminates execution in the current iteration and continues execution of the loop with the next iteration 

# i = 0
# while i <= 5:
#     if (i == 3):
#         i+=1 # We increment i by 1. Now i becomes 4.(agr ye line ni likhi tou loop 012 k baad rk jaega)
#         continue # continue skips the rest of the code in the loop and goes back to the while condition check.
#     print(i)
#     i +=  # 0 1 2 4 5


# # to print only even numbers
# # Solution 1 :
# i = 0
# while i <= 10:
#     if (i%2 == 0 ):
#         print(i)
#     i +=1


# # Solution 2:
# i = 0
# while i <= 10:
#     if (i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i +=1



# ----------------------------------- FOR LOOP ------------------------------------
# num = [1, 2, 3, 4, 5]

# for el in num:
#     print(el)
# # output:
# # 1
# # 2
# # 3
# # 4
# # 5



# veggies = ["Brinjal", "Potato", "Guord", "cucumber"]
# for val in veggies:
#     print(val) 
# # output:
# # Brinjal
# # Potato
# # Guord
# # cucumber
 

# tup = (2, 3, 8, 8, 9, 7, 3, 5, 4)
# for i in tup:
#     print(i)

# # output:
# # 2
# # 3
# # 8
# # 8
# # 9
# # 7
# # 3
# # 5
# # 4


# str = "Komal"
# for char in str:
#     print(char)

# # # output:
# # K
# # o
# # m
# # a
# # l





# str = "Komal"
# for char in str:
#     print(char)
# else:
#     print("End")
# # output:
# # K
# # o
# # m
# # a
# # l
# # End
# # Why we use else? 
# # Ans: It can be used in some specific cases when we use "break"


# str = "KOMAL"
# for char in str:
#     if (char == "O"):
#         print("O Found")
#         # break
#     print(char)
# else: #             if /else ❌         for else (in same seq)
#     print("End") # end not execute due to break.
# # K
# # O Found




# # Example 
# str = "Komal"
# for char in str:
#     if (char == "m"):
#         print("m Found")
#     else:
#         print(char)
# # # Output
# # K
# # o
# # m Found   
# # a
# # l


