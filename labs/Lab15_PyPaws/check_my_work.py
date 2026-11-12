
"""
check_my_work.py  -  Run this file after each step to test your code.

You do NOT need to change anything in this file.
Just press Run in your IDE and type the step number (1-5),
or press Enter to check everything.
"""

import builtins
import contextlib
import importlib
import io
import sys
import tempfile
import traceback
from pathlib import Path

LAB_FOLDER = Path(__file__).resolve().parent
sys.path.insert(0, str(LAB_FOLDER))

results = []          # list of (passed, message)


def check(passed, message, hint=""):
    """Record and print the result of one check."""
    results.append(passed)
    if passed:
        print(f"  [PASS] {message}")
    else:
        print(f"  [FAIL] {message}")
        if hint:
            print(f"         Hint: {hint}")


def safe(test_function, message, hint=""):
    """Run one check. If the student's code crashes, show why instead of stopping."""
    try:
        with contextlib.redirect_stdout(io.StringIO()):   # hide the student's prints
            passed = bool(test_function())
    except Exception as error:
        line = ""
        tb = traceback.extract_tb(error.__traceback__)
        student_lines = [f for f in tb if Path(f.filename).resolve().parent == LAB_FOLDER
                and Path(f.filename).name != "check_my_work.py"]
        if student_lines:
            last = student_lines[-1]
            line = f" (in {Path(last.filename).name}, line {last.lineno})"
        check(False, message, f"your code crashed with {type(error).__name__}: {error}{line}")
        return
    check(passed, message, hint)


def load(module_name):
    """Import one of the lab files, or explain why it could not be imported."""
    try:
        if module_name in sys.modules:
            return importlib.reload(sys.modules[module_name])
        return importlib.import_module(module_name)
    except SyntaxError as error:
        print(f"  [FAIL] {module_name}.py has a SYNTAX error on line {error.lineno}: {error.msg}")
        print("         Fix it first (look for a red squiggly line in your IDE).")
    except Exception as error:
        print(f"  [FAIL] Could not import {module_name}.py: {type(error).__name__}: {error}")
    results.append(False)
    return None


def fake_input(answers):
    """Return a replacement for input() that 'types' the given answers."""
    def _input(prompt=""):
        if not answers:
            raise RuntimeError("input() was called too many times - is your loop stopping?")
        return answers.pop(0)
    return _input


# ===================================================================
def step1():
    print("\nSTEP 1 - Build the Pet class")
    pet_module = load("pet")
    if not pet_module:
        return
    Pet = pet_module.Pet

    def attributes():
        p = Pet("Mochi", "cat", 3, 40, 75)
        return (p.name, p.species, p.age, p.hunger, p.happiness) == ("Mochi", "cat", 3, 40, 75)
    safe(attributes, "TODO 1a: Pet saves name, species, age, hunger and happiness",
         "inside __init__ write  self.species = species  (and the same for the others)")

    def defaults():
        p = Pet("Rex", "dog", 2)
        return p.hunger == 50 and p.happiness == 50
    safe(defaults, "TODO 1a: hunger and happiness use their default values (50)",
         "use the parameters hunger and happiness, not fixed numbers")

    def adopted():
        return Pet("Mochi", "cat", 3).adopted is False
    safe(adopted, "TODO 1b: a new pet has  adopted = False",
         "add  self.adopted = False  inside __init__")

    def as_text():
        return str(Pet("Mochi", "cat", 3, 40, 75)) == "Mochi the cat (age 3) | hunger 40 | happiness 75"
    safe(as_text, 'TODO 1c: str(pet) looks like "Mochi the cat (age 3) | hunger 40 | happiness 75"',
         "check spaces and the | symbols. Try  print(str(pet))  to compare")


def step2():
    print("\nSTEP 2 - Pet methods")
    pet_module = load("pet")
    if not pet_module:
        return
    Pet = pet_module.Pet

    def feed_basic():
        p = Pet("Mochi", "cat", 3, 40, 75)
        message = p.feed()
        return p.hunger == 20 and isinstance(message, str) and "Mochi" in message
    safe(feed_basic, "TODO 2a: feed() lowers hunger by 20 and RETURNS a message",
         "self.hunger = keep_in_range(self.hunger - amount), then return an f-string")

    def feed_floor():
        p = Pet("Mochi", "cat", 3, 40, 75)
        p.feed(100)
        return p.hunger == 0
    safe(feed_floor, "TODO 2a: hunger never goes below 0",
         "use keep_in_range(...) around the new value")

    def play_basic():
        p = Pet("Mochi", "cat", 3, 40, 50)
        message = p.play()
        return p.happiness == 70 and p.hunger == 45 and isinstance(message, str)
    safe(play_basic, "TODO 2b: play() adds minutes*2 happiness, 5 hunger, and returns a message",
         "10 minutes -> happiness +20 and hunger +5")

    def play_ceiling():
        p = Pet("Mochi", "cat", 3, 98, 90)
        p.play(30)
        return p.happiness == 100 and p.hunger == 100
    safe(play_ceiling, "TODO 2b: happiness and hunger never go above 100",
         "use keep_in_range(...) for BOTH values")

    def moods():
        def mood_at(h):
            return Pet("A", "cat", 1, 50, h).mood()
        return (mood_at(70) == "happy (^_^)" and mood_at(69) == "okay (-_-)"
                and mood_at(40) == "okay (-_-)" and mood_at(39) == "sad (T_T)")
    safe(moods, "TODO 2c: mood() returns happy / okay / sad at the right happiness levels",
         "check your >= signs: 70 is happy, 40 is okay, 39 is sad")


def step3():
    print("\nSTEP 3 - Reading a file + exceptions")
    shelter = load("shelter")
    if not shelter:
        return

    def good_rows():
        pets = shelter.load_pets(shelter.PETS_FILE)
        return len(pets) == 8 and pets[0].name == "Mochi" and pets[0].age == 3
    safe(good_rows, "TODO 3a: load_pets() skips the 2 broken lines and returns 8 pets",
         "wrap the 3 lines inside the loop in  try: / except ValueError:")

    def skip_message():
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            shelter.load_pets(shelter.PETS_FILE)
        return "Ghost" in buffer.getvalue() and "Bubbles" in buffer.getvalue()
    safe(skip_message, "TODO 3a: it prints which lines were skipped",
         "in the except block:  print(f\"  ! Skipping bad line: {line}\")")

    def missing_file():
        return shelter.load_pets(LAB_FOLDER / "data" / "no_such_file.csv") == []
    safe(missing_file, "TODO 3b: a missing file does not crash and returns an empty list",
         "wrap the  with open(...)  block in  try: / except FileNotFoundError:")


def step4():
    print("\nSTEP 4 - Bug hunt")
    bugs = load("bug_hunt")
    if not bugs:
        return

    safe(lambda: bugs.total_treats({"Mochi": 2, "Biscuit": 5, "Pickles": 1, "Waffles": 6}) == 14
         and bugs.total_treats({"A": 3, "B": 4}) == 7,
         "Bug 1: total_treats() adds up ALL the treats",
         "set a breakpoint inside the loop and watch  total  each time around")

    safe(lambda: bugs.average_age([3, 5, 1, 2, 12, 4, 8, 9]) == 5.5
         and bugs.average_age([10, 2]) == 6,
         "Bug 2: average_age() is correct",
         "watch  i  in the debugger. Which index is it the very first time?")

    safe(lambda: bugs.find_oldest([("Mochi", 3), ("Pixel", 12), ("Toast", 9)]) == ("Pixel", 12)
         and bugs.find_oldest([("A", 1), ("B", 2)]) == ("B", 2),
         "Bug 3: find_oldest() finds the oldest pet",
         "step through the if statement. Does it EVER become True?")

    report = (LAB_FOLDER / "bug_report.txt").read_text(encoding="utf-8")
    check(report.count("Line number:") >= 3 and "____" not in report,
          "bug_report.txt is filled in",
          "replace every ____ in bug_report.txt with your answers")


def step5():
    print("\nSTEP 5 - Writing files + running the shelter")
    shelter = load("shelter")
    pet_module = load("pet")
    main = load("main")
    if not (shelter and pet_module and main):
        return
    Pet = pet_module.Pet
    temp_folder = Path(tempfile.mkdtemp())

    def report():
        pets = [Pet("Mochi", "cat", 3, 40, 75), Pet("Toast", "cat", 9, 30, 35)]
        path = temp_folder / "report.txt"
        shelter.save_report(pets, path)
        shelter.save_report(pets, path)       # twice: "w" mode should REPLACE the file
        if not path.exists():
            return False
        lines = path.read_text(encoding="utf-8").splitlines()
        return (len(lines) == 3 and "PyPaws Shelter Report" in lines[0]
                and lines[1] == str(pets[0]) and lines[2] == str(pets[1]))
    safe(report, "TODO 5a: save_report() writes a title line + one line per pet",
         'no file yet? open it with "w". Extra lines? end every write with "\\n"')

    def adoption_log():
        pet = Pet("Mochi", "cat", 3)
        path = temp_folder / "adoptions.txt"
        shelter.log_adoption(pet, "Sam", path)
        shelter.log_adoption(pet, "Lee", path)  # twice: "a" mode should KEEP both lines
        if not path.exists():
            return False
        lines = path.read_text(encoding="utf-8").splitlines()
        return (len(lines) == 2 and "Mochi the cat was adopted by Sam" in lines[0]
                and "Lee" in lines[1] and "|" in lines[0])
    safe(adoption_log, "TODO 5b: log_adoption() APPENDS one line per adoption",
         'open the file with "a" (append), not "w", and end the line with "\\n"')

    def choose_valid():
        pets = [Pet("Mochi", "cat", 3), Pet("Toast", "cat", 9)]
        original = builtins.input
        builtins.input = fake_input(["hello", "99", "-1", "2"])
        try:
            return main.choose_pet(pets) is pets[1]
        finally:
            builtins.input = original
    safe(choose_valid, "TODO 5c: choose_pet() keeps asking after bad input, then returns the pet",
         "typed: hello, 99, -1, 2  ->  should return the 2nd pet")

    def choose_cancel():
        pets = [Pet("Mochi", "cat", 3)]
        original = builtins.input
        typed = ["oops", "0"]
        builtins.input = fake_input(typed)
        try:
            return main.choose_pet(pets) is None and len(typed) == 0
        finally:
            builtins.input = original
    safe(choose_cancel, "TODO 5c: typing 0 cancels and returns None",
         "typed: oops, 0  ->  should ask twice, then return None")

    log = shelter.ADOPTION_LOG
    check(log.exists() and log.read_text(encoding="utf-8").strip() != "",
          "You played main.py and adopted at least one pet (data/adoptions.txt exists)",
          "run main.py, get a pet happy enough, and adopt it!")


# ===================================================================
STEPS = {"1": step1, "2": step2, "3": step3, "4": step4, "5": step5}

if __name__ == "__main__":
    print("=" * 56)
    print("   Lab 15 (PyPaws) - Check My Work   /\\_/\\")
    print("                                  ( o.o )")
    print("=" * 56)
    choice = input("Which step do you want to check? (1-5, or Enter for ALL): ").strip()

    if choice in STEPS:
        STEPS[choice]()
    else:
        for run_step in STEPS.values():
            run_step()

    passed = results.count(True)
    total = len(results)
    print("\n" + "-" * 56)
    print(f"  {passed} / {total} checks passed")
    if total and passed == total:
        print("  ALL CLEAR!  (=^.^=)  Great work - move on to the next step!")
    else:
        print("  Read the hints above, fix one thing, and run me again.")
    print("-" * 56)
