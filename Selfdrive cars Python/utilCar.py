import functions as av
from matplotlib.pyplot import * 
import random


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

#function that controls a car usin Bentham's utilitarian principle
def utilCar(us):
    #us - a scenario object as a parameter
	if us.left_barrier_exists() == True and us.right_barrier_exists() == False:
		if numDead("Left", us) <= numDead("Right", us):
			return "Stay"
		elif numDead("Left", us) > numDead("Right", us):
			return "Swerve"
	elif us.right_barrier_exists() == True and us.left_barrier_exists() == False:
		if numDead("Left", us) < numDead("Right", us):
			return "Stay"
		elif numDead("Left", us) >= numDead("Right", us):
			return "Swerve"
s = av.Scenario(3, False, 5, True, True, 0, False)
s2 = av.Scenario(2, True, 5, True, False, 3, True)
s3 = av.Scenario(0, False, 4, True, True, 0, True)
s4 = av.Scenario(0, True, 3, True, False, 4, False)
s5 = av.Scenario(2, False, 4, True, True, 3, True)
assert utilCar(s)== "Swerve", "Stayed but should have Swerved"
assert utilCar(s2)== "Stay", "Swerved but should have Stayed"
assert utilCar(s3)== "Swerve", "Stayed but should have Swerved"
assert utilCar(s4)== "Stay", "Swerved but should have Stayed"
assert utilCar(s5)== "Swerve", "Stayed but should have Swerved"
print("Success!")
def case(car, cs):
	total_dead = 0
	for i in range(10000):
		cs.randomize()
		if car(cs) == "Stay":
			total_dead = total_dead + numDead("Left", cs)
		else:
			total_dead = total_dead + numDead("Right", cs)
	avg = total_dead/10000
	return(avg)



s = av.Scenario()

case(utilCar, s)
x = []
y = []


s = av.Scenario()
pct_util = 1 # set the starting percentage of util cars
for fract in range(100): # for each fraction of util cars
	totalDead = 0
	for i in range(1000): # 1000 trials per fraction.
		if random.randint(1,100) < pct_util: # Pick selfish or utilitarian
			totalDead = totalDead + case(utilCar, s)
	
		else:
			case(utilCar, s)
			totaldead = totalDead + case(utilCar, s)

	x.append(fract/100)
	y.append(totalDead/1000)
		
	pct_util  = pct_util +1
# Generate a plot of the x and y values.

scatter(x, y) # plot x and y.
title("Fatalities Due to Util Cars") # Title for the plot.
xlabel("Fraction of Util Cars") # Label the x axis.
ylabel("Deaths/Scenario") # Label the y axis
grid(True) # Turn on the grid lines.
show() 