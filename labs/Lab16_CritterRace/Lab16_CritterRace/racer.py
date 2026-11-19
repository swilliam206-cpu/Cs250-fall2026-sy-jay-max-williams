"""
racer.py  -  the Racer class

One Racer object = one critter in the Critter Grand Prix.
"""
import random
# TODO 2a: import the whole  random  library (it is part of Python's standard library).
#          You will use  random.random()  and  random.randint()  in Step 3.



class Racer:
    """A critter that runs a race, one round at a time."""

    def __init__(self, name, species, symbol, min_step, max_step, nap_chance=0.0):
        self.name = name                # e.g. "Tina"
        self.species = species          # e.g. "turtle"
        self.symbol = symbol            # one letter drawn on the race track, e.g. "T"
        self.min_step = min_step        # smallest distance it can move in one round
        self.max_step = max_step        # largest distance it can move in one round
        self.nap_chance = nap_chance    # chance (0.0 to 1.0) it takes a nap and does not move
        self.position = 0               # how far it has run so far
        self.history = [0]              # its position after every round (for the chart)

    def __str__(self):
        nap = int(self.nap_chance * 100)
        return (f"{self.name} the {self.species} [{self.symbol}]  "
                f"moves {self.min_step}-{self.max_step} per round, naps {nap}% of the time")

    # ---------------------------------------------------------------
    # STEP 3
    # ---------------------------------------------------------------
    def move(self):
        """Move forward one round. Return how far the racer moved."""

        if random.random() < self.nap_chance:
            step = 0
        else:
            step = random.randint(self.min_step, self.max_step)

        self.position += step
        self.history.append(self.position)
        return step

    def reset(self):
        """Put the racer back at the starting line."""
        self.position = 0
        self.history = [0]