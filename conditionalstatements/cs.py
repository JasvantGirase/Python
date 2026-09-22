
#EX1
# num=int(input("enter one number"))
# if num%2 ==0:
#     print("given no is even")
# else:
#     print("given no is odd")



#EX2
# num = int(input("Enter one Number: "))

# cnt = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         cnt += 1

# if cnt == 2:
#     print("Given Number is Prime")
# else:
#     print("Given Number is Not Prime")


#EX3
# for i in range(10,0,-1):
#     print(i)


#ex4
# num = int(input("Enter One Number: "))

# temp = num
# p = len(str(num))
# sum = 0
# r = 0

# while num > 0:
#     r = num % 10
#     sum += r ** p
#     num //= 10

# if sum == temp:
#     print("Given Number is Armstrong")
# else:
#     print("Given Number is Not Armstrong")


#ex5
# def one_to_ten():  # Function Declaration & Definition
#     for i in range(1, 11):
#         print("Number:", i)

# one_to_ten()  # Function Calling


#ex6
# def Even_or_Odd(a):
#     if a % 2 == 0:
#         print("Given Number is Even.")
#     else:
#         print("Given Number is Odd.")

# num = int(input("Enter One Number: "))

# Even_or_Odd(num)


#ex7
# def Sorting(lst):
#     print("Data --> ")
#     print(lst)

#     lst.sort()

#     print("Sorted Data --> ")
#     print(lst)


# data = set(map(int, input("Enter data: ").split()))

# data = list(data)

# Sorting(data)