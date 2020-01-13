set&Dictionary.py


#sets
 

 #includes a data type for sets.
#Curly braces or the set () function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)


#show that duplicates have been removed
#fast membership testing
'orange' in basket
'crabgrass' in basket

Demonstate set operation on unique letter from two words
a = set('abracedabra')
b = set('alacazam')
a - b   #unique letters in a
b - a   #letters in a but not in b
a | b   #letters in a or b or both
a & b  # letters in both a and  b 

a ^ b  # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a


fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits

fruits.append("pipeapple")

fruits.update("grape")
fruits

fruits.remove("banana")
fruits

fruits.discard("kiwi")
fruits


>>>Dictionaries
#Dictionaries
#Another useful data type built into Python is the dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['sape']

tel[1]
tel['jack']


tel['guido'] = 4124
tel
del tel['sape']
tel
tel['irv'] = 4137

list(tel) # change to list 
 
sorted(tel)   # alphabet sorting

'guido' in tel

'jack' not in tel

dict([('sape',4139), ('guido', 4127),('jack',4098)])
dict(sape=4139, guido=4127, jack=4098)


{x: x**2 for x in (2, 4, 6)}
2 : 4
4 : 16
6 : 36

{x: x**3 for x in (1, 2, 3, 4, 5)}
1 : 1
2 : 8
3 : 27
4 : 64
5 : 125

#when looping through dictrionaries
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
...     print(k, v)


knights = {'gallahad': 'the pure', 'robin': 'the brave', 'sape':4355}
for x, y in knights.items():
...     print(x, y)

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)