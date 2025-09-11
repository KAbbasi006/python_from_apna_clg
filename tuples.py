# Tuples : built-in data type that lets us create immutable sequences of values.

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
# print(acc)







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
