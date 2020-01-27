#fibonacci.py

#Fibonacci numbers module

#n = int(input('Please enter a number: '))

def fib(n): # Write fibonacci series upto n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()

#Go to Fibonacci Powerpoint

def fib2(n): #Return fibonacci series upto n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

def name():
	print("Hello World")

def hello():
 	print(12345)

def dog():
 	print("dog is sleeping")

# >>> fib # import
