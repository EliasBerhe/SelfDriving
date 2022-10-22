# imports
import functions as av
from matplotlib.pyplot import * 
import random


#Defines a function that controls a car so that it preserves its passengers' lives at all cost
def selfishCar(sc):
	if sc.left_barrier_exists()==True:
		return "Swerve" 
	else:
		return "Stay"
s = av.Scenario(3, False, 5, True, True, 0, True)
assert selfishCar(s) == "Stay", "Swerved but should have stayed."
print("Success!")



#a helper function that returns the number of fatatlities that occur when the car "Stays" and when it "Swerves"
def numDead(lane, nsc):
    #lane - a string which will be "left" or "right"(indicates the lane that the car ends up in)
    #nsc - a Scenario object (describes the situation on  the road)
	if lane == "Left":
		if nsc.left_barrier_exists() == True:
			return nsc.passengers
		elif nsc.left_barrier_exists() == False:
			return nsc.left_pedestrians
	if lane == "Right":
		if nsc.right_barrier_exists() == True:
			return nsc.passengers
		elif nsc.right_barrier_exists() == False:
			return nsc.right_pedestrians



def case_selfishCar(csc):
	total_dead = 0
	for i in range(10000):
		csc.randomize()
		if selfishCar(csc) == "Stay":
			total_dead = total_dead + numDead("Left", csc)
		else:
			total_dead = total_dead + numDead("Right", csc)
	avg = total_dead/10000
	return(avg)

s = av.Scenario(3, True, 5, True, False, 0, False)
case_selfishCar(s)

x = []
y = []


s = av.Scenario()
pct_selfish = 1 # set the starting percentage of selfish cars
for fract in range(100): # for each fraction of selfish cars
	totalDead = 0
	for i in range(1000): # 1000 trials per fraction.
		if random.randint(1,100) < pct_selfish: # Pick selfish or utilitarian
			totalDead = totalDead + case_selfishCar( s)
	
		else:
			case_selfishCar( s)
			totaldead = totalDead + case_selfishCar( s)

	x.append(fract/100)
	y.append(totalDead/1000)
		
	pct_selfish = pct_selfish+1
# Generate a plot of the x and y values.

scatter(x, y) # plot x and y.
title("Fatalities Due to Selfish Cars") # Title for the plot.
xlabel("Fraction of Selfish Cars") # Label the x axis.
ylabel("Deaths/Scenario") # Label the y axis
grid(True) # Turn on the grid lines.
show() 