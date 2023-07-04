#Name: MENDIOLA, LOGIE A | Year&Sec: BSCPE 1-5 | OBJECT ORIENTED PROGRAMMING | ASSIGNMENT #9
print("======================================================================= INSTRUCTIONS ==============================================================================\n*Write a test program named TestFan that creates two Fan objects.\n*For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.\n*Assign medium speed, radius 5, color blue, and turn it off for the second object.\n*Display each object’s speed, radius, color, and on properties\n====================================================================================================================================================================")

class Fan:
    def __init__(self, speed, radius, color, power):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__power = power

    #Fan Speed: SLOW
    def speed_SLOW(self):
        fan_slow = 1
        Slow = fan_slow
        return Slow
    
    #Fan Speed: MEDIUM
    def speed_MEDIUM(self):
        fan_medium = 2
        Medium = fan_medium
        return Medium
    
    #Fan Speed: FAST
    def speed_FAST(self):
        fan_fast = 3
        Fast = fan_fast
        return Fast
    

    
    #creating fan objects of the class_Fan
        #place holder for object template:
            #first object = Fan1(FAST, 10, yellow, ON)
            #second object = Fan2(MEDIUM, 5, blue, OFF)