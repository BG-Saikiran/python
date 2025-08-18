#METHOD 1
# num1 = int(input('enter a number: '))
# count = 0
# for i in range(1,num1+1):
#     if num1%i==0:
#         count +=1

# if count == 2:
#     print('prime number','having',count,'factors') 
# else:
#     print('not a prime','having',count,'factors')    
 
# METHOD 2

# num1 = int(input('enter a number: '))
# if num1<= 1:
#     print('not a prime')
# else:
#     flag = True
#     for i in range(2,num1):
#         if num1%i==0:
#             flag = False
#             print('not a prime')
#             break

#     if flag == True:
#         print('Prime number')

#METHOD 3
# def check_prime(num1):
#     if num1<= 1:
#         return 'Not a prime'
    
#     for i in range(2,num1):
#         if num1%i==0:
#             return 'Not a Prime'
        
#     return 'Prime'    

# num1 = int(input('enter a number: '))
# print(check_prime(num1))

#METHOD 4
# def check_prime(num1):
#     if num1<= 1:
#         return 'Not a prime'
    
#     for i in range(2,num1 // 2 + 1):
#         if num1%i==0:
#             return 'Not a Prime'
        
#     return 'Prime'    

# num1 = int(input('enter a number: '))
# print(check_prime(num1))


# def check_prime(num1):
#     if num1 <= 1:
#         return "not a prime"
    
#     for i in range(2,int(num1**0.5)+1):  #3 iterations
        
#         if num1%i==0:
#             return "not a prime"
        
#     return "prime"

# num1 = int(input('enter a number: '))
# print(check_prime(num1))


# def check_prime(num):
#     if num<=1:
#         return "Not a Prime"
    
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return num,"Not a prime"
#     else:
#         return num,"Prime"

# inp_1 = int(input("enter a first number: "))      
# inp_2 = int(input("enter a second number: "))

# for num in range(inp_1,inp_2+1):
#     print(check_prime(num))


# arr = []
# def check_prime(num):
#     if num<=1:
#         return "Not a Prime"
    
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return num,"Not a prime"
#     else:
#         return num,"Prime"

# inp_1 = int(input("enter a first number: "))      
# inp_2 = int(input("enter a second number: "))
# for num in range(inp_1,inp_2):
#         arr.append(check_prime(num))
# print(arr)

