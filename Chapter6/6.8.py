#The Egg Drop Problem: There is a building of 100 floors.
# If an egg drops from the Nth floor or above, it will break.
#If it's dropped from any floor below, it will not break.
#You're given two eggs. Find N, while minimizing the number of drops for the worst case.

class eggs_problem():
    def __init__(self):
        self.breaking_point = 68
        self.count_drops = 0

    def drop(self, floor):
        self.count_drops +=1
        return floor >= breaking_point #if broken returns true otherwise returns false

    def find_breaking_point(self,floors):
        interval = 14
        prev_floor = 0
        egg1 = interval
        #DROP egg1
        while(not self.drop(egg1) and egg1 <= floors):
            interval -=1
            prev_floor = egg1
            egg1 += interval

        #DROP egg2
        egg2 = prev_floor + 1
        while(egg2 <egg1 and egg2 <= floors and not self.drop(egg2)):
            egg2+=1

        return egg2
