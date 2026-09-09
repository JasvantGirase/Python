#ex1:strip()
# data="      embedded"
# print("string is:",data)
# print("data using string function:",data.strip())


#ex2 split()
# data="my location is pune"
# print("string is:",data)
# print("data using split function:",data.split())


#ex3 replace()
# data="my location is pune"
# print("original str is",data)
# print("after change")
# print(data.replace("pune","delhi"))


#ex4 count()
# data="my location is pune"
# print("count of'i' is:",data.count('i'))


#ex5 upper() and lower()
# Data = "My Location is PUNE Pune"

# print("String --> ", Data)
# print("String In Upper Case: ", Data.upper())
# print("String In Lower Case: ", Data.lower())



#ex6 find()
# Data = "My Location is PUNE Pune"

# print("String --> ", Data)

# res = 0
# res = Data.find("i")

# print("Result is --> ", res)


# ex7 capitalize() and tite()
# data="i am trainer"
# print("data:-",data)
# print("after change:-",data.capitalize())
# print("second change:-",data.title())


#ex8 swapcase()
# data="my  Name is JasvANt"
# print("after swapping the letters",data.swapcase())


#ex9 startswith()
# Data = "My Class Name Is TECHNO SCRIPTS"

# print("Data :- ", Data)

# res = Data.startswith("My")

# print("Result --> ", res)

#ex10 endswith()
# Data = "My Class Name Is TECHNO SCRIPTS"

# print("Data :- ", Data)

# res = Data.endswith("SCRIPTS")

# print("Result --> ", res)

#ex11
# Data = "My Class Name Is TECHNO SCRIPTS"

# print("Data :- ", Data)

# ind = Data.index("TECHNO")

# print("Index No. of 'TECHNO' ", ind)

#ex12 isalpha()
# data = "jasvant girase"
# print(data.isalpha())

# ex13 
# data = "12345"
# print(data.isdigit())

#ex14
# data = "jasvant123"
# print(data.isalnum())

#ex15 task:check whether string contain alphabet or number
# data = input("Enter String: ")

# if data.isalnum():
#     print("Alphabet or Number")
# else:
#     print("Not Alphabet or Number")


#ex 16
# Data = "TECHNO SCRIPTS"

# print("Data is:", Data)

# Res = Data.isupper()
# print("\nResult of 'isupper' -->", Res)

# Res2 = Data.islower()
# print("Result of 'islower' -->", Res2)

#ex17
# Data = "Class Name Is Techno Scripts:"
# print("Data is --> ", Data)

# Res1 = Data.istitle()
# print("\nResult of 'istitle' --> ", Res1)

#ex 18
# Data = "TECHNO"

# Data = Data.center(35)

# print("\nString After Update :")
# print(Data)

# Len = len(Data)
# print("Length of Given String is:", Len)


#ex 19
# print("Enter Student Info".center(40))

# Name = input("Enter Student Name: ")
# Roll = int(input("Enter Student Roll No. : "))
# Per = float(input("Enter Student Per : "))

# print("\n")
# print("Student Info".center(25))

# print("Name: ", Name)
# print("Roll No.: ", Roll)
# print("Per: ", Per)



#ex20
# data="electronics"
# print("data is",data)
# print("string with ljust:",data.ljust(20))
# print("string with rjust:",data.rjust(20))
