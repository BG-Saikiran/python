#Palindromic Bus Ticket
inpName = input("enter your bus ticket number: ")
if inpName == inpName[::-1]:
    print("luckyNumber!")
else:
    print("NotLucky !")
#enter your bus ticket number: 98876
# NotLucky !
# enter your bus ticket number: 124421
# luckyNumber!



#Sum of Magic Squares
n = int(input('enter a number: '))
sum = 0
for i in range(1,n+1):
    pow = i**2
    sum = sum + pow
print(sum)    
# enter a number: 10
# 385


#Treasure Hunt Guessing Game
secretNumber = 38
i = 1
while i<=100:
    n = int(input('your number: '))
    if n == secretNumber:
        print("Tressure Found")
        break
    else:
        print("try again !")
    i +=1
# your number: 3
# try again !
# your number: 7
# try again !
# your number: 38
# Tressure Found            


#Perfect Square Festival
for i in range(1,500):
    if i*i <= 500:
        print(i*i,end =" ")
#1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484         
  

#Cube Challenge  
cubeNum = int(input("enter a number: "))
for i in range(1,cubeNum+1):
    print(i**i)

# enter a number: 10
# 1
# 4
# 27
# 256
# 3125
# 46656
# 823543
# 16777216
# 387420489
# 10000000000    