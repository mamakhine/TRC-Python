#If_Else_Statement
If_Else_Statement.py

#Boolean Expression
print(20 > 10)
 print(20 > 10)
True
>>> print(20 == 10)
False
>>> print(20 < 10)
False
>>> print(bool("Helllo World"))
True
>>> print(bool(20))
True

Python Conditions

Equals                     ->  X == y
Not Equal                  ->  x != y
Less than                  ->  x < y
Less than or equal to      ->  x <= y
Greater than               ->  x > y
Greater than or equal to   ->  x >= y
Boolean OR                 ->  x or y, x | y
Boolean AND                ->  x and y, x & y
Boolean NOT                ->  not x



if -
else -

 x = 10
>>> if x == 0:
...     print("Hello")
... elif x != 0:
...     print("world")
... elif x >= 20:
...     print("x ix 20")
... else:
...     print("x is 10")
...
world
>>>


x = 10
>>> if x == 0:
...     print("x is zero")
... elif x != 0:
...     print("x is equal zero")
... elif x < 20:
...     print("X is 20")
... elif x == 10:
...     print("x is 10")
... else:
...     print("x is nothing")
...
x is equal zero

x = 70
y = 60
>>> if x < y:
...     print("x is greater than y")
...

x = 50
>>> y = 150
>>> if x > y:
...     print("x is greater than y")
... elif x == y:
...     print("x and y are equal")
... else:
...     print("x is less than y")
...
x is less than y


#short hand if
if x > y: print("x is greater than y")


x = 50
>>> y = 150
>>> print(x) if x > y else print(y)

#And is logical operator
x = 50
y = 40
z = 100
if x > y and z > x:
	print("All Conditions are True")

x = 50
y = 40
z = 100
if x > y and x > z:
	print("All Conditions are True")
else:
	print("one condition is true")

x = 50
y = 40
z = 100
if x > y or x > z:
	print("All Conditions are True")
else:
	print("one condition is true")

x = 50
y = 40
z = 100
if x > y and z > y or x > z:
	print("All Conditions are True")
else:
	print("one condition is true")

#Or is logical operator
x = 50
y = 40
z = 100
if x > y or z < y:
	print("one of the Conditions is True")
elif x > y and z > y:
	print("All  Conditions are True")
else:
	print("Nothing")

#Nested IF is if statements in if statements
 x = 50
 if x > 10:
 	print("x is ten")
 	if x > 20:
 		print("x is grater than 20")
 	else:
 		 print("No,x is not greater than 20")
...
x is ten
x is grater than 20


 x = 50
 if x < 10:
 	print("x is ten")
 	if x > 20:
 		print("x is grater than 20")
 	else:
 		 print("No,x is not greater than 20")
 else:
 	print("x is 50")

x = 100
y = 50
if x > y:
	pass


	
x = int(input("Please enter an integer:"))

if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')


	int(input("Examination result:"))
100 - 90        - A
90  -70         - B
70  -60         - C
60  -40         - D
40  -10         -Fail




if x >= 70 and x < 90:
	Print("Grade B")
