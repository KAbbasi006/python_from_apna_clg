# Dictionaries: are used to store data in "Key : Value" pairs. Dicionary main koi indexing nhi hoti balky ye
# aesy access hoty hain.------------->         print(info["name"]) # Shahzeb
# Duplicate keys not allowed agr duplicate likhengy tou existing value over write hojaegi.


# They are: 
#       unordered
#       mutable (changeable)
#       don't allow duplicate keys

# dictionary = {
#     "name": "Komal", 
#     "cgpa": 3.2,
#     "marks": [63, 85, 98, 100, 58], 
# }


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



# # ------------------------NULL DICTIONARY --------------
# null_dict = {}
# print(null_dict) // {}
# null_dict["name"] = "Komal"
# print(null_dict)


# # ------------------------NESTED DICTIONARY -------------------------------
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







# --------------------------------------- Dictionary Methods ---------------------------------------
# # 1. .keys() -----> returns all keys in form of list
# student = {
#     "name": "Komal",
#     "sub_marks":{
#         "eng": 58,
#         "urdu": 98, 
#         "maths": 99,
#     },
#     "age": 98,
# }
# print(student.keys()) # dict_keys(['name', 'sub_marks', 'age'])
# print(list(student.keys())) # ['name', 'sub_marks', 'age']
# print(len(list(student.keys()))) # 3





# 2. .values() ------return all values

# student = {
#     "name": "Komal",
#     "sub_marks":{
#         "eng": 58,
#         "urdu": 98, 
#         "maths": 99,
#     },
#     "age": 98,
# }
# print(student.values()) # dict_values(['Komal', {'eng': 58, 'urdu': 98, 'maths': 99}, 98])





# 3. .items() ---> returns all (key, value) pairs as tuples

# student = {
#     "name": "Komal",
#     "sub_marks":{
#         "eng": 58,
#         "urdu": 98, 
#         "maths": 99,
#     },
#     "age": 98,
# }
# print(student.items())# dict_items([('name', 'Komal'), ('sub_marks', {'eng': 58, 'urdu': 98, 'maths': 99}), ('age', 98)])
# a = list(student.items())
# print(a) # [('name', 'Komal'), ('sub_marks', {'eng': 58, 'urdu': 98, 'maths': 99}), ('age', 98)]
# print(a[1]) # ('sub_marks', {'eng': 58, 'urdu': 98, 'maths': 99})
# print(a[0]) # ('name', 'Komal')



# 4. .get() ----> returns the value according to key.. we can acces value as ---> print(student["name"]) but 
# to overcome error we use this .get()
# # print(student["full_name"]) # Error (no key found)
# print(student.get("full_name")) # None


# student = {
#     "name": "Komal",
#     "sub_marks":{
#         "eng": 58,
#         "urdu": 98, 
#         "maths": 99,
#     },
#     "age": 98,
# }

# print(student["name"]) # Komal
# print(student.get("name")) # Komal

# # print(student["full_name"]) # Error
# print(student.get("full_name")) # None





# 5 .update(newDict) inserts the specified items to the dictionary
 
# student = {
#     "name": "Komal",
#     "sub_marks":{
#         "eng": 58,
#         "urdu": 98, 
#         "maths": 99,
#     },
#     "age": 98,
# }
# student.update({"city": "Karachi"})
# print(student) # {'name': 'Komal', 'sub_marks': {'eng': 58, 'urdu': 98, 'maths': 99}, 'age': 98, 'city': 'Karachi'}
# letters = {
#     "a" : "apple",
#     "b": "ball"
# }
# student.update(letters)
# print(student) # {'name': 'Komal', 'sub_marks': {'eng': 58, 'urdu': 98, 'maths': 99}, 'age': 98, 'city': 'Karachi', 'a': 'apple', 'b': 'ball'}