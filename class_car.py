#Name: MENDIOLA, LOGIE A | Year&Sec: BSCPE 1-5 | OBJECT ORIENTED PROGRAMMING | ASSIGNMENT #9

print("======================================================================= INSTRUCTIONS ==============================================================================")                            
print("                                     Design a program that creates a Car object then calls the accelerate method five times                                        ")
print("                                    After each call to the accelerate method, get the current speed of the car and display it                                      ")
print("                                                           Then call the brake method five times                                                                   ")
print("                                        After each call to the brake method get the current speed of the car and display it                                        ")
print("===================================================================================================================================================================")

class Car:
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    #Car Acceleration
    def accelerate(self):
        self.__speed += 5

    #Car Brake
    def brake(self):
        self.__speed -= 5

    #getter method for speed    
    def get_speed(self):
        return self.__speed