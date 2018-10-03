class Person:

    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

def addPet():
    newOwner = Person()
    number = input ("How many pets?: ")
    for x in range(int(number)):
        pet= input ("Pet name?: ")
        newOwner.add_pet(pet)
    owner = input ("Owner's name?: ")
    print (pet + " added")

    print (newOwner.pets)
    print(owner + " has "+str(len(newOwner.pets))+" pets in total")
    return owner

exit = 0
ownerList=[]

while exit == 0 :
    newCommand = input ("Command?: ")

    if newCommand in ('add','Add'):
        ownerList.insert(0 ,addPet())

    if newCommand in ('Exit','exit'):
        exit = 1

    if newCommand in ('owners','Owners'):
            print(ownerList)
