"""
bug_hunt.py  -  STEP 4: Debugging

The shelter's "Treat & Stats Calculator" runs without crashing...
but its answers are WRONG. There is exactly ONE bug in each of the
three functions below (3 bugs total).

Your mission:
  1. Run this file and compare its output with the CORRECT output below.
  2. Use your IDE's DEBUGGER (breakpoints + Step Over + Variables panel)
     to watch the variables change and find each bug.
  3. Fix the bug (usually a one-line change).
  4. Write what you found in bug_report.txt.

CORRECT output (what it SHOULD print when every bug is fixed):
    Treats needed per day: 14
    Average pet age: 5.5
    Oldest pet: Pixel (age 12)
"""


"""
bug_hunt.py - STEP 4: Debugging

The shelter's Treat & Stats Calculator.
All three bugs have been corrected.
"""


def total_treats(treats_per_pet):
    """Add up the treats every pet needs per day."""
    total = 0
    for name in treats_per_pet:
        total += treats_per_pet[name]
    return total


def average_age(ages):
    """Return the average of a list of ages."""
    total = 0
    for i in range(0, len(ages)):
        total += ages[i]
    return total / len(ages)


def find_oldest(pets):
    """Return (name, age) of the oldest pet."""
    oldest_name = ""
    oldest_age = 0

    for name, age in pets:
        if age > oldest_age:
            oldest_name = name
            oldest_age = age

    return oldest_name, oldest_age


def main():
    treats = {"Mochi": 2, "Biscuit": 5, "Pickles": 1, "Waffles": 6}

    ages = [3, 5, 1, 2, 12, 4, 8, 9]

    pets = [
        ("Mochi", 3),
        ("Biscuit", 5),
        ("Pickles", 1),
        ("Sir Hops-a-Lot", 2),
        ("Pixel", 12),
        ("Noodle", 4),
        ("Waffles", 8),
        ("Toast", 9)
    ]

    print("Treats needed per day:", total_treats(treats))
    print("Average pet age:", average_age(ages))

    name, age = find_oldest(pets)
    print(f"Oldest pet: {name} (age {age})")


if __name__ == "__main__":
    main()
