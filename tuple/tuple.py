#EX1 
##A tuple is immutable
##IF I WANT TO ADD DATA, THEN Tuple → List → Modify → Tuple

# TUP = ("Techno", 106, 15.28, "IOT", True)

# print(TUP)

# TUP = list(TUP)

# TUP.append("EMB_C")

# print("Data Type of 'TUP' Var: ", type(TUP))

# TUP = tuple(TUP)

# print("\nTuple After Change: ")
# print(TUP)



#EX2
# TUP = ("Techno", 106, 15.28, "IT", True)

# print(TUP)

# TUP = list(TUP)

# TUP[4] = False

# TUP = tuple(TUP)

# print("Tuple --> ", TUP)



#EX3
#PACKING CONCEPT
# Name = input("Enter Your Name: ")
# Age = int(input("Enter Your Age: "))
# Pro = input("Enter Your Roll: ")

# My_Info = (Name, Age, Pro)

# print("Tuple --> ")
# print(My_Info)


#EX4
#UNPACKING CONCEPT
# CAR = ("Supra_MK4", "GTR_R34", "RX7")

# print("Tuple --> ", CAR)

# Toyota, Nissan, Mazda = CAR

# print("\nToyota Car --> ", Toyota)
# print("Nissan Car --> ", Nissan)
# print("Mazda Car --> ", Mazda)



#EX5
# data=input("enter the data")
# data=tuple(data.split())
# print("tuple is",data)


