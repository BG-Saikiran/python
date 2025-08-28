# num1 ,num2 = input("enter a num: ").split(",")
# print(num1,num2)

# num1,num2,num3 = map(float,input("enter a num: ").split(","))
# print(num1,num2,num3)

# inp_li = list(map(str,input("enter a num: ").split(",")))
# print(inp_li)

# inp_li1 = input("name: ").split(",")
# print(inp_li1)

#join
list1 = ["1","2","hi"]
enocode_str = ",".join(list1)
print(enocode_str)

#set methods
#add
s = {1,2}
s.add(3)
print(s)
#remove
s = {1,2,3}
s.remove(2)
print(s)

# s = {1,2,3}
# s.remove(4)
# print(s) #error

#discard 
s = {1,2,3}
s.discard(4)
print(s)  #{1,2,3}

#pop
s = {1,2,3}
s.pop()
print(s) #{2,3}

#clear

#union
s1 = {1,2}
s2 = {2,3}
print(s1.union(s2))

s1 = {1,2}
s2 = {2,3}
print(s1 | s2)


#intersection
s1 = {1,2}
s2 = {2,3}
print(s1.intersection(s2))

s1 = {1,2}
s2 = {2,3,4}
print(s1&s2)

#difference 
s1 = {1,2}
s2 = {2,3}
print(s1.difference(s2))

s1 = {1,2}
s2 = {2,3}
print(s1-s2)

#symmetric_difference
s1 = {1,2}
s2 = {2,3}
print(s1.symmetric_difference(s2))

#issubset
s1 = {1,2}
s2 = {1,2,3}
print(s1.issubset(s2))  #true

s1 = {1,2}
s2 = {1,2,3}
print(s2.issubset(s2)) #false

#issuperset
s1 = {1,2}
s2 = {1,2,3}
print(s2.issuperset(s1)) #true

s1 = {1,2}
s2 = {1,2,3}
print(s1.issuperset(s2))  #false
