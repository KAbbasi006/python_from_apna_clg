# Set : collection of unordered items(like dictionary). each elt must be unique and immutable.
# IMPORTANT----------------------> Set is mutable but "Elements in set" are immutable
# we can store int, float, boolean, str, tuple in our set --> {1, 2.3, "a", True, (6,"yt")} but we cannot store 
# list and dictionary in our set bcz they are mutable ---(IMPORTANT POINT)
# --------------NULL SET (MOST IMPORTANT CONCEPT) -------------------------------
# null_set = set()
# print(null_set)# set()
# print(type(null_set))# <class 'set'>
# print("\n")

# collection = {"Komal",1, 2, 2, 2, "hello"}
# print(collection)# {1, 2, 'hello', 'Komal'}   no order, no sequence, no duplicate
# print(len(collection)) # 4




# --------------------------------------------SET METHODS ---------------------------------------------------

# Sets are mutable (we can add/remove elt from set) but elts in sets are immutable (cannot change values) 




# 1. set.add(el) Adds an elt (can add tuple , str etc but cannot add list, dict bcz they are mutable)
# collec = set()
# collec.add(1)
# collec.add(6)
# collec.add(1)
# collec.add(2)
# print(collec) # {1, 2, 6}




# # 2. set.remove(el) removes the elt

# collec = set()
# collec.add(1)
# collec.add(6)
# collec.add(1)
# collec.add(2)
# print(collec) #{1, 2, 6}

# collec.remove(2)
# print(collec) # {1, 6}

# collec.add("Komal") # can pass str
# print(collec) # {1, 'Komal', 6}

# collec.add((1, '9', "hania")) # can pass tuple
# print(collec) # {1, 6, 'Komal', (1, '9', 'hania')}



# --------------------------------- cannot add list in set bcz list is mutable --------------------------

# collec.add(["mana", "hana", "sana"]) # cannot pass list
# print(collec) # TypeError: unhashable type: 'list'

# hashable ---> immutable
# Unhashable means mutable
# kisi bhi immutable value ki hashing value ban skti hai

# --------------------------------- cannot add set in set bcz set is mutable --------------------------
# collec.add({"mana", "hana", "sana"}) # cannot pass set
# print(collec) # TypeError: unhashable type: 'set'


# # --------------------------------- cannot add dictionary in set bcz dict is mutable --------------------
# collec.add({"a": "mana", "b": "hana", "c": "sana"}) # cannot pass dictionary
# print(collec) # TypeError: unhashable type: 'dict'

# collec.remove(7)
# print(collec) # KeyError: 7


# # 3. set.clear() empties the set

# a = {1, "Komal", 9.0}
# print(len(a)) # 3
# a.add((1, 8, "D"))
# a.add("Ghania")
# print(a) # {1, 9.0, 'Ghania', 'Komal', (1, 8, 'D')}
# a.clear()
# print(a) # set()
# print(len(a)) # 0
# a.add(5)
# print(a) # {5}
# print(a.clear()) # None



# # 4. set.pop() removes a random value
# A = {"a", "b", "c", "d"}
# A.pop()
# print(A) # {'b', 'c', 'd'}
# print(A.pop()) # d
# print(A.pop()) # c

# 5. set.union(set2) ---> combines both sets values and returns new
# set1 = {1, 2, 8, 9}
# set2 = {7, 8, 9}
# print(set1.union(set2)) # {1, 2, 7, 8, 9}




# # 6. set.intersection(set2) ---> combines "Common values" and returns new
# set1 = {1, 2, 8, 9}
# set2 = {7, 8, 9}
# print(set1.intersection(set2)) # {8, 9}
