import fish

terry=fish.Trout()
terry.first_name = "Terry"
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)
print(terry.water)
terry.swim()


casey = fish.Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()


sammy = fish.Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)
