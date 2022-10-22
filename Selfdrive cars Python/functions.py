import random as rnd

class Scenario:
        
    def __init__(self, p=0, lbe=False, lmp=0, lcs=False, rbe=False, rnp=0, rcs=False):
        self.passengers = p
        self.left_barrier = lbe
        self.left_pedestrians = lmp
        self.left_crossing_signal = lcs
        self.right_barrier = rbe
        self.right_pedestrians = rnp
        self.right_crossing_signal = rcs
        
    def randomize(self):
        self.passengers = rnd.randint(1,5)
        
        barrier = rnd.choice([True, False])
        if (barrier):
            self.left_barrier = rnd.choice([True, False])
            self.right_barrier = not self.left_barrier
        else:
            self.left_barrier = False
            self.right_barrier = False
            
        if (not self.left_barrier):
            self.left_pedestrians = rnd.randint(0,7)
            self.left_crossing_signal = rnd.choice([True, False])
        else:
            self.left_pedestrians = 0
            self.left_crossing_signal = False
            
        if (not self.right_barrier):
            self.right_pedestrians = rnd.randint(0,7)
            self.right_crossing_signal = rnd.choice([True, False])
        else:
            self.right_pedestrians = 0
            self.right_crossing_signal = False
        
    def num_passengers(self):
        return self.passengers
    
    def left_barrier_exists(self):
        return self.left_barrier
    
    def left_num_pedestrians(self):
        return self.left_pedestrians
    
    def left_crossing_signal_on(self):
        return self.left_crossing_signal
    
    def right_barrier_exists(self):
        return self.right_barrier
    
    def right_num_pedestrians(self):
        return self.right_pedestrians
    
    def right_crossing_signal_on(self):
        return self.right_crossing_signal


    