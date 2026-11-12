


"""
shelter.py - STEP 3 and STEP 5

Functions that work with FILES: loading pets, saving a report,
and keeping a log of adoptions.
"""

import random
from datetime import datetime
from pathlib import Path

from pet import Pet


# ---------------------------------------------------------------
# File locations
# ---------------------------------------------------------------

DATA_FOLDER = Path(__file__).parent / "data"
PETS_FILE = DATA_FOLDER / "pets.csv"
REPORT_FILE = DATA_FOLDER / "shelter_report.txt"
ADOPTION_LOG = DATA_FOLDER / "adoptions.txt"


# ---------------------------------------------------------------
# STEP 3: Reading a file and handling exceptions
# ---------------------------------------------------------------

def load_pets(filename):
    """Read pets from a CSV file and return a list of Pet objects."""

    pets = []

    try:
        # Open the CSV file in read mode
        with open(filename, "r", encoding="utf-8") as file:

            # Skip the header line
            file.readline()

            # Go through each line in the file
            for line in file:

                # Remove extra spaces and newlines
                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                try:
                    # Separate the pet information
                    name, species, age, hunger, happiness = line.split(",")

                    # Create a new Pet object
                    pet = Pet(
                        name,
                        species,
                        int(age),
                        int(hunger),
                        int(happiness)
                    )

                    # Add the pet to the list
                    pets.append(pet)

                # Handle broken pet records
                except ValueError:
                    print(f"  ! Skipping bad line: {line}")

    # Handle missing files
    except FileNotFoundError:
        print(f"  ! Could not find the file: {filename}")

    # Return the list of pets
    return pets


# ---------------------------------------------------------------
# STEP 5: Saving a shelter report
# ---------------------------------------------------------------

def save_report(pets, filename):
    """Write a report of every pet to a text file."""

    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d")

    # Open the file in write mode
    with open(filename, "w", encoding="utf-8") as file:

        # Write the report title
        file.write(f"PyPaws Shelter Report - {today}\n")

        # Write each pet's information
        for pet in pets:
            file.write(str(pet) + "\n")


# ---------------------------------------------------------------
# STEP 5: Recording pet adoptions
# ---------------------------------------------------------------

def log_adoption(pet, adopter, filename):
    """Add one line to the adoption log."""

    # Get the current date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Open the file in append mode
    with open(filename, "a", encoding="utf-8") as file:

        # Write the adoption information
        file.write(
            f"{now} | {pet.name} the {pet.species} "
            f"was adopted by {adopter}\n"
        )


# ---------------------------------------------------------------
# Random surprise events (already completed)
# ---------------------------------------------------------------

def random_event(pets):
    """Something surprising happens to one random pet."""

    # Find pets that have not been adopted
    available = [p for p in pets if not p.adopted]

    # Check if all pets have been adopted
    if not available:
        return "The shelter is quiet... every pet has a home!"

    # Choose a random pet
    pet = random.choice(available)

    # Choose a random event from 1 to 4
    event = random.randint(1, 4)

    # Event 1: Pet finds food
    if event == 1:
        pet.feed(30)
        return f"{pet.name} found a secret snack stash under the couch! (hunger -30)"

    # Event 2: Pet goes to the park
    elif event == 2:
        pet.play(15)
        return f"A volunteer took {pet.name} to the park! (happiness +30)"

    # Event 3: Pet gets scared
    elif event == 3:
        pet.happiness = max(0, pet.happiness - 20)
        return f"{pet.name} got scared by the vacuum cleaner... (happiness -20)"

    # Event 4: Pet gets hungry
    else:
        pet.hunger = min(100, pet.hunger + 25)
        return f"{pet.name} did zoomies for an hour and is now STARVING! (hunger +25)"
