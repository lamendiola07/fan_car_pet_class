#Name: MENDIOLA, LOGIE A | Year&Sec: BSCPE 1-5 | OBJECT ORIENTED PROGRAMMING | ASSIGNMENT #9
print("======================================================================= INSTRUCTIONS ==============================================================================\n*Write a test program named TestFan that creates two Fan objects.\n*For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.\n*Assign medium speed, radius 5, color blue, and turn it off for the second object.\n*Display each object’s speed, radius, color, and on properties\n====================================================================================================================================================================")

class Fan:
    def __init__(self, speed, radius, color, power):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__power = power

    #Fan Speed
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed

    #Fan Radius
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    #Fan Color
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
    
    #Fan Power
    def get_power(self):
       return self.__power
    
    def set_power(self, power):
        self.__power = power
    
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