# Dictionaries: are used to store data in "Key : Value" pairs
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
# print(len(student))





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
# print(student.values())





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
# # print(student.items())
# a = list(student.items())
# print(a[1]) # ('sub_marks', {'eng': 58, 'urdu': 98, 'maths': 99})




# 4. .get() ----> returns the key according to value


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
 
student = {
    "name": "Komal",
    "sub_marks":{
        "eng": 58,
        "urdu": 98, 
        "maths": 99,
    },
    "age": 98,
}
student.update({"city": "Karachi"})
print(student)