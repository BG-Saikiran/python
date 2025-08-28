# 1. get(key, default=None)
#Returns value for the key if it exists; otherwise returns default.

d = {
    "name" : "sai",
    "age" : 22
}
print(d.get("name")) #sai
print(d.get("gender","none"))  #none

#2. keys()
#Returns a view object of dictionary keys.

d = {
    'a': 1,
    'b': 2}
print(d.keys())  #dict_keys(['a', 'b'])
print(list(d.keys()))   #['a', 'b']

#3. values()
#Returns a view object of dictionary values.

d = {
    'a': 1,
    'b': 2
    }
print(list(d.values()))  #[1, 2]

# 4. items()
#Returns a view object of (key, value) tuples.

d = {
    'a': 1,
    'b': 2
    }
print(d.items())  #dict_items([('a', 1), ('b', 2)])

for k,v in d.items():
    print(k,v)  #a 1
                #b 2

#5. update([other]) 

d = {
    'a': 1,
    'b': 2
    }  
d.update({"c":3,"f":4,"b":5})
print(d)

d.update([('a',7),('d',4)])
print(d)

#6. pop(key, default)
#Removes specified key and returns its value.
print(d.pop("a"))
#print(d.pop())  #error atleast one arguement need to pass

#Edge Case:
print(d.pop("z","not found")) #not found

#7. popitem()
#Removes and returns the last inserted item. Applicable for dictionaries after version 3.7
print(d.popitem())  #('d', 4)

#Edge Case:
empDic = {}
#empty.popitem()  #keyerror

#8. clear()
#Removes all items from the dictionary.
d.clear()
print(d)

#9. copy()
#Returns a shallow copy. If values are mutable (like lists), changes in the copy will affect the original.
d = {
    'a': 1,
    'b': 2
    } 
shallow = d.copy()
shallow.update({"c":3})
print(d)  #values are immutable so it is not shallow copy its deep copy

d = {
    'a': [1,2]
    } 
shallow = d.copy()
shallow["a"].append(3)
print(d)  #{'a': [1, 2, 3]}

# 10. fromkeys(keys, value=None)
#Creates a new dictionary from keys and a common value. If value is mutable (like a list), all keys share the same object.
keys = ['a','b']
new_d = dict.fromkeys(keys,1)
print(new_d)  #{'a': 1, 'b': 1}

#11. zip(keys, values)
#Zip(keys, values) pairs up items from both lists. dict(zip(...)) converts those pairs into key-value pairs.
keys = ['a','b']
values = [1,2,3]
print(dict(zip(keys,values)))  #{'a': 1, 'b': 2}
print(zip(keys,values)) 


keys = ['a','b']
values = [1]
print(dict(zip(keys,values)))  #{'a': 1}

keys = ['a','a']
values = [1,2]
print(dict(zip(keys,values)))  #{'a': 2}