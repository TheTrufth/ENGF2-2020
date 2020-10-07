
import math, random #Importing the required libraries 
def estimatepi(NumOfTrials):
	NumOfHits = 0  #Set number of hits to 0 to initialise the value
	for i in range(NumOfTrials): 
		x = random.random() / 2 #Dividing by 2 to get the range of x and y values from 0 to 0.5 as we are focusing on 1 quad.
		y = random.random() / 2
		if math.sqrt(x*x + y*y) <= 0.5:
			NumOfHits += 1
	return (4*(NumOfHits/NumOfTrials)) #Multiply by 4 to get 4 quadrants

NumOfTrials = int(input("Enter number of trials(integer): \n")) #Asking user for required precision.
pi_estimate = estimatepi(NumOfTrials)
txt = "Pi value: {}"
print(txt.format(pi_estimate))
 

			


