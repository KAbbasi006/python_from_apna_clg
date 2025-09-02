# two types of coversion

        # 1. Coversion ( automatic )
        # 2. Casting   ( zabardasti)

# Float is superior
a,b = 1, 2.3
sum  = a+b
print(sum) # float

a, b = 1, 3
sum  = a+b
print(sum) # int

a = 1
b = "3"
sum  = a+b
print(sum) # error     str cannot concatenate with int/float

a = 1
b = int("4")
sum  = a+b
print(sum) # error     str cannot concatenate with int/float