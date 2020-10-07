for number in range(1, 100):
	if (number % 3) == 0 and (number % 5) == 0:
		print("FizzBuzz \n")
	elif (number % 3) == 0:
		print("Fizz \n")
	elif (number % 5) == 0:
		print("Buzz \n")
	else:
		txt = ("{}  \n")
		print(txt.format(number))

