# LIST: a built-in data type that stores set of values.
# it can store elements of different types(int, float, str).

# marks = [87, 85, "Sana", 90]
# print(marks[2]) # Sana
# print(marks[0]) # 87

# days = ["mon", "tues", "wed"]
# days[1] = 4 # can change original list. ✅
# print(days) # ['mon', 4, 'wed']
# print(len(days)) # 3


# eng = 98
# urdu = 95
# maths = 54
# isl = 45
# phys = 90
# sub = [eng, urdu, maths, isl, phys, urdu, urdu, "chem = 76"] # can repeat elts, add any type of data ✅
# print(sub) # [98, 95, 54, 45, 90]
# print(type(sub)) # list
# print(len(sub)) # 8
# print(sub[5]) # 95
# print(sub[6]) # 95


# #Index ->  0      1        2       3              
# std  = ["Komal", "maha", "zoya", "hira"]
# # if we try to access any index that is out of range then error is thrown
# print(std[4]) # Error ❌  list index out of range


# std  = ["Komal", "maha", "zoya", "hira"]
# print(std[1:3]) # ['maha', 'zoya']
# print(std[:3]) # ['Komal', 'maha', 'zoya']
# print(std[1:]) # ['maha', 'zoya', 'hira']
# print(std[1:len(std)]) # ['maha', 'zoya', 'hira']
# print(std[-4:-2]) # ['Komal', 'maha']
# std = ["a", "b"]
# print(std) # ['a', 'b']







# # ------------------------------- list Methods -------------------------------------------------------------

# alp = ["a",  "d", "b", "c", "e"]

# # 1. append (Adds one element at the end)
# print(alp.append("g")) # None --- append method kuch return nhi krta( yani print krny pr "None" ayega)
# alp.append("s")
# print(alp) # ["a", "b", "c", "d", "e", "s"]

# # 2. sort (sorts in ascending order) -------Ye "None" return krna hai. mtlb kuch b nhi
# print(alp.sort()) # None 
# print(alp) # ['a', 'b', 'c', 'd', 'e']


# a = [5, 9, 6, 8, 5, 5, 7]
# print(a.sort()) # None ----- sort method kuch return nhi krta( yani print krny pr "None" ayega)
# # sort kuch return nhi krta sirf original list k andar changes kr rha hai. 
# print(a) # [5, 5, 5, 6, 7, 8, 9]

#  #          m        b        a         g
# fruits = ["mango", "banana", "apple", "grapes"]
# fruits.sort()
# print(fruits) # ['apple', 'banana', 'grapes', 'mango']
# #                 a         b         g         m



# # 3. sort(reverse = True) ------sorts in descending order.
# opp = [2, 3, 8, 7, 3, 7]
# print(opp.sort(reverse = True)) # None
# print(opp) # [8, 7, 7, 3, 3, 2]

#  #          m        b        a         g
# fruits = ["mango", "banana", "apple", "grapes"]
# fruits.sort(reverse = True)
# print(fruits) # ['mango', 'grapes', 'banana', 'apple']
# #                  m       g          b         a




# #4. reverse() --- list ki values reverse hongi
# naam = ["k", "o", "m", "a", "l"]
# print(naam.reverse()) # None
# print(naam) # ['l', 'a', 'm', 'o', 'k']






# #5. insert(index, el)add elt at specific index  kuch b delete ni hoga.us index pr jo b hoga wo shift hojaega
# sub = ["eng", "urdu", "maths", "sci", "sst", "comp"]
# print(sub.insert(0, "Drawing")) # None
# print(sub) # ['Drawing', 'eng', 'urdu', 'maths', 'sci', 'sst', 'comp']



# # 6. remove() removes 1st occurence of elt
# lst = [2, 1, 3, 1, 2, 1, 1, 4]
# lst.remove(1) 
# print(lst) # [2, 3, 1, 2, 1, 1, 4]   pehla one remove hua hai bs


# IMP NOTE: ------------------------------- POP returns value ------------------------

# # 7. pop(index) removes elt at specific index
# a = ["k", "o", "m", "a", "l"]
# print(a.pop(2)) # m
# print(a)
