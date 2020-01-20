 
x =int(input("Examination result:"))
if x >= 90 and x <= 100:
	print("Grade A")
elif x >= 70 and x < 90:
	print("Grade B")
elif x >= 60 and x < 70:
	print("Grade C")
elif x >= 40 and x < 60:
	print("Grade D")
elif x >= 0 and x < 40:
	print("Fail")
else:
	print("Absent")