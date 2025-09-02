# # # 3 strings to overcome error of apostrophe
# # str1 = 'This is a string.'
# # str2 = "Komal"
# # str3 = """ String"""


# # ----------------- Escape Sequence Characters -----------------------------(tab next line etc)
# str1 = "This is a string.\nwe are using new line escape seq character"
# print(str1,"\n")


# str2 = "This is a string.\t'Tab' escape seq character"
# print(str2)
# ---------------------------------------------------Operations on String --------------------------------------

#  -----------------Concatenation-------------------
# a = "Komal"
# b = "Shahzeb"
# c = a+" "+b 
# print(c)

# # ------------------Length----------------------- (spaces also add in length)
# str1 = 'This is a string.'
# print(len(str1))

# # --------------Indexing (starts from 0)------- (assignment in indexing is not allowed)
# name = "Komal_Shahzeb"
# #       0123456789.....
# print(name[4])

# age = "Twenty_eight"
# ch = age[4]
# print(ch)

# naam = "Komal"
# naam[2] = "y"  #  ❌❌❌❌
# print(naam)

# #  ---------------------Slicing--------------------------  str[start ✅, end not included ❌]
# clg = "Apna-ghar"
# print(clg[2:5])
# print(clg[0:5])

# print(clg[0:9])
# print(clg[0:len(clg)])      # if we write leng(clg) instead of last index, python takes it to the last
# print(clg[0:])               #if we skip last index, python by default takes it to the last
# print(clg[:6])               #if we skip first index, python by default assume from start
# print(clg[9:6])    # blank      makes no sense


# # -------------------------- Negative Indexing ------------------- str[start ✅, end not included ❌]
# fruit = "Apple"
# print(fruit[-3:-1])






# # ----------------------------------- STRING FUNCTIONS ---------------------------------------------

# # 1. .endswith()  // returns "TRUE" if string ends with substring.

# str = "Komal Shahzeb"
# print(str.endswith("zeb"))   # True
# print(str.endswith("Kom"))   # False

# fruit = "Mango"
# print(fruit.endswith("ngo"))



# # 2. .capitalize() //  Capitalizes 1st character..... it does not change original string.. it works one time only
# naam = "komal shahzeb"
# print(naam.capitalize()) # Komal shahzeb

# centre = "i am in giaic"
# print(centre.capitalize()) # I am in giaic        
  
# age = "twenty"
# print(age.capitalize()) # original string does not change

# age = age.capitalize()
# print(age.capitalize()) # Original string changes



# # 3. replace(old, new) // replace all occurences of old with new

# sub = "I am studying Python"
# print(sub.replace("y", "--")) # I am stud--ing P--thon
# print(sub.replace("Python", "JS")) # I am studying JS

# sub = sub.replace("Python", "JS") 
# print(sub) # I am studying JS



# # 4. .find(word) // returns 1st index of 1st occurences

# ball = "I play with original football"
# print(ball.find("o")) # 12 (first "o" ka index 12 hai)
# print(ball.find("K")) # -1 bcz no such word occur



# 5. .count() // counts the occurence of substring in string

school = "Lindenberg grammar school"
print(school.count("r")) # 3     ( "r" occur 3 times)
