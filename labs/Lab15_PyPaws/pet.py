"""
pet.py  -  STEP 1 and STEP 2

The Pet class is the blueprint for every animal in the PyPaws Shelter.
Look for the lines that start with  # TODO  and complete them.
"""


def keep_in_range(value, low=0, high=100):
    """Return value, but never lower than low or higher than high.
    (Already done for you! You will use it in Step 2.)

    keep_in_range(130)  ->  100
    keep_in_range(-5)   ->  0
    keep_in_range(42)   ->  42
    """
    return max(low, min(high, value))


class Pet:
    """A shelter pet with a hunger level and a happiness level (both 0-100)."""

    # A CLASS attribute: one dictionary shared by every Pet.
    SOUNDS = {
        "cat": "Meow!",
        "dog": "Woof woof!",
        "hamster": "Squeak squeak!",
        "rabbit": "*thump thump*",
        "parrot": "Hello! Hello! Pretty bird!",
        "snake": "Hissssss...",
        "turtle": "...",
    }

    # ---------------------------------------------------------------
    # STEP 1: build the pet
    # ---------------------------------------------------------------
    def __init__(self, name, species, age, hunger=50, happiness=50):
        # TODO 1a: Save each of the 5 parameters as an INSTANCE attribute.
        #          The first one is done for you:
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.happiness = happiness

        # TODO 1b: Add one more attribute called  adopted  and set it to False.
        #          (Every pet starts out waiting for a home.)
        self.adopted = False

    def __str__(self):
        return f"{self.name} the {self.species} (age {self.age}) | hunger {self.hunger} | happiness {self.happiness}"
        # Tip: use an f-string with self.name, self.species, ...
        

    def speak(self):
        """Return the sound this pet makes. (Already done for you!)"""
        sound = self.SOUNDS.get(self.species, "*stares at you*")
        return f"{self.name} says: {sound}"

    # ---------------------------------------------------------------
    # STEP 2: give the pet some behavior (methods)
    # ---------------------------------------------------------------
    def feed(self, amount=20):
        # TODO 2a: Feeding makes the pet LESS hungry.
        self.hunger = keep_in_range(self.hunger - amount)
        return f"{self.name} munches happily. Hunger is now {self.hunger}."
        #   1. Subtract amount from self.hunger  (use keep_in_range so it never goes below 0)
        #   2. Return a message like:  "Mochi munches happily. Hunger is now 20."

    def play(self, minutes=10):
        # TODO 2b: Playing makes the pet happier, but also a little hungrier.
        #   1. Add  minutes * 2  to self.happiness  (never above 100)
        #   2. Add  5  to self.hunger                (never above 100)
        #   3. Return a message like:
        #      "You played with Mochi for 10 minutes! Happiness is now 95."
        self.happiness = keep_in_range(self.happiness + minutes * 2)
        self.hunger = keep_in_range(self.hunger + 5)
        return f"You played with {self.name} for {minutes} minutes! Happiness is now {self.happiness}."

    def mood(self):
        # TODO 2c: Use if / elif / else on self.happiness and return:
        #   70 or more      ->  "happy (^_^)"
        #   40 up to 69     ->  "okay (-_-)"
        #   less than 40    ->  "sad (T_T)"
        if self.happiness >= 70:
            return "happy (^_^)"
        elif self.happiness >= 40:
            return "okay (-_-)"
        else:
            return "sad (T_T)"
