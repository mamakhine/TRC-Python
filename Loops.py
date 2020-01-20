#Loops

-while Loops
-for Loops
Condition is true, while Loop execute a set of statements

x = 1
while x < 7:
	print(x)
	x += 1

While loop require variable ready.

x = 1
while x < 7:
	print(x)
	if x == 5:
		break
	x += 1

For Loops
#for Loops is iterating over a sequence 
fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)


#Looping in String
for x in "pineapple":
	print(x)

for x in [1,2,a,4]:
	print(x)

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:

for x in "pineapple":
	print(x)




#The continues Statement stop the current iteration.

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "orange":
		continues
		print(x)