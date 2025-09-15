# #1. Strings are immutable 
# str = "Hello"
# str[2] = "Y"
# print(str) # ERROR ❌ 'str' object does not support item assignment

# 2. slicing possible ✅










# # Lists are mutable through indexing
# days = ["mon", "tues", "wed"]
# days[1] = 4 # can change original list. ✅
# print(days) # ['mon', 4, 'wed']
# print(len(days)) # 3

# 2. slicing possible ✅

 # sort() ascending order main ajaega sb (numbers, alphabets,  sb main hogi)
# a = [5, 9, 6, 8, 5, 5, 7]
# print(a.sort()) # None ----- sort method kuch return nhi krta( yani print krny pr "None" ayega)
# # sort kuch return nhi krta sirf original list k andar changes kr rha hai. 
# print(a) # [5, 5, 5, 6, 7, 8, 9]


# alp = ["a",  "d", "b", "c", "e"]
# print(alp.append("g")) # None --- append method kuch return nhi krta( yani print krny pr "None" ayega)
# alp.append("s")
# print(alp) # ["a", "b", "c", "d", "e", "s"]




# # 3. sort(reverse = True) ------sorts in descending order.(numbers, alphabets,  sb main hogi)
# opp = [2, 3, 8, 7, 3, 7]
# print(opp.sort(reverse = True)) # None
# print(opp) # [8, 7, 7, 3, 3, 2]

# reverse() --- list ki values reverse hongi

# pop value return krta hai ✅



















# tup = (87, 64, 33, 95, 76) # cannot change any value
# # tup[0] = 100 # ❌ NOT allowed in python
# print(type(tup))
# print(tup[0]) # 87

# app = () #  valid tuple hai ✅
# print(app) # ()   

# single_tup = (1,) # single elt ko hamesha comma k sath likhengy warna python usay integer consider kryga
# print(single_tup)

# man = (2) # ab python isay tuple ki jaga integer consider kryga aur iski type b "int" krdega
# print(type(man)) # <class 'int'>
  

# acc = (1, 2, 3, 4,) # last main comma acceptable hai. error nhi ayega. marzi hai lagao ya na lagao
# print(acc[1:3]) # (2, 3)







# --------------------------------- Tuple Methods ( 2 ) --------------------------------------

# # 1. index() returns index of first occurence 

# tup = 2, 1, 3, 1 # acceptable
# print(type(tup)) # <class 'tuple'>
# print(tup) # (2, 1, 3, 1)


# appp = (2, 1, 3, 1)
# print(appp.index(1)) # 1

# #2. count() count total occurences
# ppp = (2, 1, 3,1, 1, 1, 1, 1)
# print(ppp.count(1)) # 6




# ----------------------------IMPORTANT ----------------------4
# there is no indexing in dictionaries bcz they are " UNORDERED". they can be accessed by their key names.

# info = {
#     "key": "value", 
#     "name": "Shahzeb", 
#     "sub": 8,
#     "languages": ["JS", "TS", "Python"], 
#     90 : 98, # acceptable ✅✅✅✅✅
#     1.2565 : "k",
# }
# print(info)
# print(info["name"]) # Shahzeb
# print(info["sub"]) # 8
# # print(info["father_name"]) # keyError
# info["father_name"] = "Ali" # adds new key value pair

# info["name"] = "Shahzaib khan"
# print(info)





# student = {
#     "name": "Komal",
#     "sub_marks":{
#         "eng": 58,
#         "urdu": 98, 
#         "maths": 99,
#     },
#     "age": 98,
# }
# print(student)
# print(student["sub_marks"] )
# print(student["sub_marks"]["maths"]) # to access value in NESTED dictionary
# student["sub_marks"]["maths"] = 100
# print(student)




# imp point:    dictionary main hm keys jo hain wo zyada tar string ko banaty hain like {"name": value} lekin 
# hm keys main str k elava int, float, tuples ki b keys bana skty hain bcz they are immutable. sirf list aur dictionary ko "key" nahi bana skty kyun k ye change ho jaty hain












# null_set = set()
# print(null_set)# set()
# print(type(null_set))# <class 'set'>
# print("\n")

# null_dictionary = {}
# print(null_dictionary)# {}
# print(type(null_dictionary))# <class 'set'>
# print("\n")

# null_list = []
# print(null_list)# []
# print(type(null_list)) # <class 'list'>
# print("\n")

# null_tuple = ()
# print(null_tuple) # ()
# print(type(null_tuple)) # <class 'tuple'>
# single_tup = (1,) # always written with comma
# print(single_tup) #(1,)

