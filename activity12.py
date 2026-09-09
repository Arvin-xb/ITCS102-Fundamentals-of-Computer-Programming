#elif
#


name = input("Enter your Name: ")
age = int(input("Input your age: "))

if age>= 0 and age<= 5:
	print("That Age is considered as Infant")
elif age>= 6 and age<= 12 :
	print("That Age is considered as Kid")
elif age>= 13 and age<= 15 :
	print("That Age is considered as Pre-Teen")
elif age>= 16 and age<= 19 :
	print("That Age is considered as Teen")
elif age>= 20 and age<= 29 :
	print("That Age is considered as Early Adulthood")
elif age>= 30 and age<= 58 :
	print("That Age is considered as Adult")
elif age>= 59 and age<= 150 :
	print("That Age is considered as Senior")
else :
	print("Age invalid")