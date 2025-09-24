# 1. "Given a list where each element represents the color of a sock, e.g., ['red', 'green', 'red', 'purple', 'green', 'black', 'red'],
# how many days can I sustain if I can wear only one matching pair of socks per day 
# and each pair can be used only once?"
list_socks = ['red', 'green', 'red', 'purple', 'green', 'black', 'red','red']
dict1 = {}
for socks in list_socks:
    if socks not in dict1:
        dict1[socks] = 1
    else:
        dict1[socks] += 1
print(dict1)   
days = 0     
for i,j in dict1.items():
    if j > 1:
        day = j//2
        days += day
print(days,"days")        

#2 Find the missing numbers inp:34581   ot : 267 missing

n = 34581
rev = 0
num_list = []
while n > 0:
    rem = n % 10
    num_list.append(rem)
    # rev = rev * 10 + rem
    n = n // 10
list_min = min(num_list)
list_max = max(num_list)
for num in range(list_min,list_max):
    if num not in num_list:
        print(num,end=" ")

print("These digits are missing")        

