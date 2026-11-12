"""
main.py  -  STEP 5: Run the PyPaws Pet Shelter!

GOAL OF THE GAME: find a home for every pet.
A pet will only go home if it is NOT sad and NOT too hungry,
so feed them and play with them first!
"""

import shelter              # import our own module (shelter.py)

BANNER = r"""
   /\_/\      ===========================
  ( o.o )        PyPaws  Pet  Shelter
   > ^ <      ===========================
             Feed them. Play with them.
                Find them a home!
"""

MENU = """
  1. See the pets
  2. Feed a pet
  3. Play with a pet
  4. Adopt a pet
  5. Save a shelter report
  6. Surprise event!
  0. Quit
"""


def available_pets(pets):
    """Return only the pets that still need a home."""
    return [pet for pet in pets if not pet.adopted]         # SPOT IT: list comprehension


def show_pets(pets):
    """Print the pets that still need a home, happiest first."""
    waiting = available_pets(pets)
    if not waiting:
        print("  Every pet has a home!")
        return
    for pet in sorted(waiting, key=lambda p: p.happiness, reverse=True):   # SPOT IT: lambda
        print(f"  {pet}  ->  {pet.mood()}")


# -------------------------------------------------------------------
# STEP 5c: input validation with try / except
# -------------------------------------------------------------------
def choose_pet(pets):
    """Show a numbered list of pets and let the user pick one.

    Return the chosen Pet, or None if the user types 0 (cancel).
    """

    if not pets:
        print("  There are no pets to choose from.")
        return None

    for number, pet in enumerate(pets, start=1):
        print(f"  {number}. {pet.name} the {pet.species}")

    while True:
        answer = input("  Pick a pet number (0 to cancel): ")

        try:
            number = int(answer)

        except ValueError:
            print("  Please type a NUMBER.")
            continue

        if number == 0:
            return None

        if 1 <= number <= len(pets):
            return pets[number - 1]

        print(f"  Please pick a number from 1 to {len(pets)}.")

    # TODO 5c: Keep asking until the user types a valid number.
    #   - Use a  while True:  loop and  input("  Pick a pet number (0 to cancel): ")
    #   - Turn the answer into an int inside  try: ... except ValueError:
    #       (if it fails, print "  Please type a NUMBER." and ask again)
    #   - If the number is 0, return None
    #   - If the number is from 1 to len(pets), return pets[number - 1]
    #   - Otherwise print "  Please pick a number from 1 to <len(pets)>." and ask again
    return None

def adopt(pets):
    """Try to send a pet home with a new family."""
    pet = choose_pet(available_pets(pets))
    if pet is None:
        return

    if pet.happiness < 40:
        print(f"  {pet.name} is too sad to leave today. Play with them first!")
    elif pet.hunger > 70:
        print(f"  {pet.name} is too hungry to travel. Feed them first!")
    else:
        adopter = input("  What is the new owner's name? ").strip() or "a kind stranger"
        pet.adopted = True
        shelter.log_adoption(pet, adopter, shelter.ADOPTION_LOG)
        print(f"  Congratulations! {pet.name} is going home with {adopter}!")
        print(f"  {pet.speak()}")


def main():
    print(BANNER)
    pets = shelter.load_pets(shelter.PETS_FILE)
    print(f"  {len(pets)} pets are waiting for a home.")

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        print()

        if choice == "1":
            show_pets(pets)
        elif choice == "2":
            pet = choose_pet(available_pets(pets))
            if pet:
                print("  " + pet.feed())
        elif choice == "3":
            pet = choose_pet(available_pets(pets))
            if pet:
                print("  " + pet.play())
        elif choice == "4":
            adopt(pets)
        elif choice == "5":
            try:                                            # SPOT IT: try / except / else / finally
                shelter.save_report(pets, shelter.REPORT_FILE)
            except OSError as error:
                print("  Could not save the report:", error)
            else:
                print(f"  Report saved to data/{shelter.REPORT_FILE.name}")
            finally:
                print("  (back to the menu)")
        elif choice == "6":
            print("  SURPRISE! " + shelter.random_event(pets))
        elif choice == "0":
            print("  Thanks for volunteering at PyPaws. Bye!")
            break
        else:
            print("  That is not an option. Try again.")

        if pets and not available_pets(pets):
            print("\n  *** YOU WIN! Every pet found a forever home! ***")
            break


if __name__ == "__main__":                                  # SPOT IT: only runs when you run main.py
    main()
