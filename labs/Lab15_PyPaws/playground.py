"""
playground.py  -  Your scratch space. Try things out here!

Nothing in this file is graded. Run it any time to see your classes in action.
Remove the  #  in front of a line to switch it on.
(Tip: select several lines and press Ctrl + /  (Cmd + / on Mac) to un-comment them at once.)
"""

from pet import Pet                       # import a class from pet.py

# ----- After STEP 1 -----
mochi = Pet("Mochi", "cat", 3, 40, 75)
print(mochi)                              # uses your __str__ method
print(mochi.speak())

# ----- After STEP 2 -----
# print(mochi.feed())
# print(mochi.play(15))
# print("Mochi feels", mochi.mood())

# ----- After STEP 3 -----
# import shelter
# pets = shelter.load_pets(shelter.PETS_FILE)
# print("Loaded", len(pets), "pets")
# for pet in pets:
#     print("  ", pet)
# print(shelter.load_pets("this_file_does_not_exist.csv"))
