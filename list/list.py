#EX1
#PRINT THE LIST
# LST=[100,"TECHNO@",61,True,90.87,'#']
# print("LIST DATA IS:")
# print(LST)


#EX2
#TAKE 3 NUMBERS IP FROM USER AND PRINT 
# n1 = int(input("Enter 1st number: "))
# n2 = int(input("Enter 2nd number: "))
# n3 = int(input("Enter 3rd number: "))

# LST = [n1, n2, n3]

# print("List is:", LST)


#EX3
#INDEXING
# LST=[100,"TECHNO@",61,True,90.87,'#']
# print("LIST DATA IS:")
# print(LST[4])
# print(LST[-4])

#EX4
#SLICING
# LST = [10, 20, 30, 40, 50, 60]

# print(LST[1:4])
# print(LST[1:4:2])


#EX 5
#CONCATATION
# LST = [100, "TECHNO@", 61, True, 90.87, '#']

# print("LIST1 DATA IS:")
# print(LST)

# L2 = ["PUNE", 12, 14, 61]

# RES = LST + L2

# print("\nLIST2 DATA IS:")
# print(L2)

# print("\nRESULT")
# print(RES)

# print("Data type is:", type(RES))

#ex 6
#append()
# LST = [180, "TECHNO@", 61, True, 98.87, '#']

# print("LIST1 DATA IS:")
# print(LST)

# LST.append(12)

# print("\nList After Change:")
# print(LST)


#ex7
#pop()
# LST = [100, "TECHNO@", 61, True, 98.87, '#']

# print("LIST1 DATA IS:")
# print(LST)

# LST.pop()

# print("\nList After Change:")
# print(LST)

#ex8
#remove
# LST = [100, "TECHNO@", 61, True, 98.87, '#']

# print("LIST1 DATA IS:")
# print(LST)

# LST.remove(61)

# print("\nList After Change:")
# print(LST)

#ex 9
#reverse
# LST = [100, "TECHNO@", 61, True, 98.87, '#']

# print("LIST1 DATA IS:")
# print(LST)

# LST.reverse()

# print("\nList After Change:")
# print(LST)


#ex10
#sorting
# LST = [100, 61, 98.87, 51]

# print("LIST DATA IS:")
# print(LST)

# LST.sort()

# print("\nList After sort:")
# print(LST)

#ex11
#sorting in reverse way
# LST = [100, 61, 98.87, 51]

# print("LIST DATA IS:")
# print(LST)

# LST.sort(reverse=True)

# print("\nList After sort:")
# print(LST)


#ex12
# LST = [108, "TECHNO@", 61, True, 90.87, '#']

# print("LIST DATA:")
# print(LST)

# # Operation
# LST.insert(2, "SCRIPTS_")

# print("\nList After Change:")
# print(LST)


#ex13
# extend()
# LST = [100, "TECHNO@", 61, True, 98.87, '#']

# L1 = [99, 22, 42, 37, 58, 11]

# print("LIST DATA:")
# print(LST)

# # Operation
# LST.extend([12, "Python_Lang", 6.7])

# print("\nLIST:")
# print(LST)



#ex14
# L1=[99,22,45]
# print(L1)
# L2=[25,65,87]
# print(L2)
# L1=L2.copy()
# print(L1)
# print(L2)



#ex15 
#clear()
# L1=[25,65,87]
# print(L1)
# L1.clear()
# print(L1)



#ex16
#count()
# LIST=[1,2,3,4,4,4,5,6]
# c_1=LIST.count(1)
# c_4=LIST.count(4)
# print("count of 1 is",c_1)
# print("count of 4 is",c_4)




#ex17
#index()
# LIST=[1,2,3,4,5,6]
# ind_1=LIST.index(1)
# ind_4=LIST.index(4)
# print("index of 1 is",ind_1)
# print("index of 4 is",ind_4)



#ex18
# LIST=[1,2,3,4,5,6]
# length=len(LIST)
# print("length of list is",length)



#ex19
#Max and Min
# LIST=[20,40,50,80,90]
# MAX=max(LIST)
# MIN=min(LIST)
# print(MAX)
# print(MIN)

#ex20
#HOW TO ACCEPT A LIST FROM USER(METHOD 1ST)
# LIST=list(input("enter list:"))
# print(LIST)
# print("Length is LIST",len(LIST))




#ex21
#HOW TO ACCEPT A LIST FROM USER(METHOD 2ST)

# LIST=[]
# n1=int(input("enter 1 integer value:"))
# LIST.append(n1)

# s=(input("enter 1 string value:"))
# LIST.append(s)

# f=float(input("enter 1 float value:"))
# LIST.append(f)

# print(LIST)


#ex22
#HOW TO ACCEPT A LIST FROM USER(METHOD 3ST)
# import ast

# LST = input("Enter LIST in String Format: ")

# # Example input: [12, "PUNE@", 61, 65.56]

# print("Data Type of LST -->", type(LST))

# LST = ast.literal_eval(LST)

# print("\nUSER LIST IS -->")
# print(LST)

# print("Length of LIST -->", len(LST))
# print("Data Type of LST -->", type(LST))



#ex23
#LIST INSIDE LIST
# LIST=[45,"jasvant",[12,13],[565,82,98,[56,82,10]]]
# print(LIST[3][0])
# print(LIST[3][3][0])



#ex24
# STUDENT = [
#     ["JASVANT", 12, 93.77],
#     ["VIVEK", 13, 92.99]
# ]

# print("Student 1 info:")

# print("Name:", STUDENT[0][0])
# print("Roll No:", STUDENT[0][1])
# print("Percentage:", STUDENT[0][2])

# print("Student 2 info:")

# print("Name:", STUDENT[1][0])
# print("Roll No:", STUDENT[1][1])
# print("Percentage:", STUDENT[1][2])