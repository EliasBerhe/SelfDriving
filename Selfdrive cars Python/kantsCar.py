import functions as av

#Function that controls a car according to the interpretation of kant's ethical princples
def kantCar(ks):
    #ks - accept a Scenario object as a parameter
	if ks.right_barrier_exists() == False and ks.right_pedestrians == 0:
		return "Swerve"
	else:
		return "Stay"

s = av.Scenario(3, True, 5, True, False, 0, False)
s2 = av.Scenario(2, True, 5, True, False, 3, True)
s3 = av.Scenario(0, False, 4, True, True, 0, True)
s4 = av.Scenario(0, True, 3, True, False, 0, False)
s5 = av.Scenario(2, False, 4, True, True, 3, True)

assert kantCar(s)== "Swerve", "Stayed but should have Swerved"
assert kantCar(s2)== "Stay", "Swerved but should have Stayed"
assert kantCar(s4)== "Swerve", "Stayed but should have Swerved"
assert kantCar(s5)== "Stay", "Swerved but should have Stayed"
print("Success!")