class Shark:
    def swim(self):
        print ("Sharks can swim")
    def swim_backward(self):
        print("Sharks can't swim backward")
    def skeleton(self):
        print("Shark skeleton is made of cartilage")

class clownfish:
    def swim(self):
        print ("Clownfish can swim")
    def swim_backward(self):
        print("Sharks can swim backward")
    def skeleton(self):
        print("Shark skeleton is made of bone")

        #same method names across the classes

def in_the_pacific(fish):
    fish.swim() #Call the passed objects swim function

sammy = Shark()
casey = clownfish()

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backward()
    fish.skeleton()

in_the_pacific(sammy)
in_the_pacific(casey)
