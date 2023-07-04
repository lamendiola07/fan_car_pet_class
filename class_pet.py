#Name: MENDIOLA, LOGIE A | Year&Sec: BSCPE 1-5 | OBJECT ORIENTED PROGRAMMING | ASSIGNMENT #9

print("======================================================================= INSTRUCTIONS ==============================================================================")
print("                 Write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet.                      ")
print("                                                  This data should be stored as the object’s attributes                                                            ")
print("                               Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.                    ")
print("===================================================================================================================================================================")

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    #getter method for pet name
    def get_name(self):
        return self.__name
    
    #setter method for pet name
    def set_name(self, name):
        self.__name = name
    


    #getter method for animal type
    def get_animal_type(self):
        return self.__animal_type
    
    #setter method for animal type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    


    #getter method for animal age
    def get_age(self):
        return self.__age
    
    #setter method for animal age
    def set_age(self, age):
        self.__age = age

def show():
    #Promp user to enter pet's name
    pet_name = input("What is your pet's name? ")

    #Prompt user to enter pet's animal type
    pet_type = input("What is your pet's animal type? ")

    #Prompt user to enter pet's age
    pet_age = input("What is your pet's age? ")

    #User's Pet as Object's Attribute
    user_pet = Pet(pet_name, pet_type, pet_age) 
    
    #Display Object's Attribute
    print("\nPet's Properties","\nName:", user_pet.get_name(),"\nAnimal Type:", user_pet.get_animal_type(), "\nAge:", user_pet.get_age())

show()
    



    

    