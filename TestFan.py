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
        speed = 1
        Slow = speed
        return Slow
    
    #Fan Speed: MEDIUM
    def speed_MEDIUM(self):
        speed = 2
        Medium = speed
        return Medium
    
    #Fan Speed: FAST
    def speed_FAST(self):
        speed = 3
        Fast = speed
        return Fast
    
    #Fan Radius
    def radius(self):
        self.__radius = 5
        return self.__radius
    
    #Fan Color
    def color(self):
        self.__color = "blue"
        return self.__color
    
    #Fan Power
    def power(self):
        on = False
        self.__power = on
        return self.__power
    
    #accessing private members
    def show(self):
        print("Speed:", self.__speed,"\nRadius:", self.__radius, "\nColor:", self.__color, "\nPower:", self.__power)
    
    #creating fan objects of the class_Fan
fan_one = Fan("FAST", 10, "yellow", True)
fan_two = Fan("MEDIUM", 5, "blue", False)

#Display Fan One Properties
print("\nFan One Properties:\n")
fan_one.show()

#Display Fan Two Properties
print("\nFan Two Properties:\n")
fan_two.show()