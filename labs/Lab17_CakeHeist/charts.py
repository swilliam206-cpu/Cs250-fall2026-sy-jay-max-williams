"""
charts.py  -  the case file picture

STEP 6  draw two charts side by side and save them as case_file.png
"""

import matplotlib.pyplot as plt
from pathlib import Path

CASE_FILE = Path(__file__).parent / "case_file.png"


def minutes_after_two(time):
    """(15, 18) -> 78   (minutes after 14:00). Tuple unpacking!"""
    hour, minute = time
    return (hour - 14) * 60 + minute


def plot_case_file(messages, counts, culprit_names, window, filename=CASE_FILE):
    """Left: messages per critter (bar chart). Right: chat timeline with the heist window."""
    fig, (left, right) = plt.subplots(1, 2, figsize=(13, 5))


    # ---------------- LEFT: who talks the most? ----------------
    # TODO 6: Draw a bar chart of the counts dictionary

    # Step 1: Get the names from the dictionary
    names = list(counts.keys())

    # Step 2: Get the message counts
    numbers = list(counts.values())

    # Step 3: Create the bar chart
    left.bar(names, numbers, color="#E2702A")

    # Step 4: Add the title and label
    left.set_title("Who talks the most?")
    left.set_ylabel("Messages")


    fig.suptitle("The Great Carrot Cake Heist: case file", fontsize=15)
    fig.tight_layout()
    fig.savefig(filename)
    plt.show()
