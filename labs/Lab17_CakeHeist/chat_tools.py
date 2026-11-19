"""
chat_tools.py  -  read and explore the group chat

STEP 1  strings + tuples         parse_line()
STEP 2  lists + comprehensions   messages_from(), shouts()
STEP 3  dictionaries             count_messages()

Every message is a TUPLE:  (time, sender, text)
and time is itself a tuple:  (hour, minute)
    example:  ((15, 18), "Tina", "zzz... still asleep in my shell")
"""

from pathlib import Path

CHAT_FILE = Path(__file__).parent / "chat.txt"


# -------------------------------------------------------------------
# STEP 1: strings + tuples
# -------------------------------------------------------------------

def parse_line(line):
    """Turn one line of the chat into a tuple."""
    # Step 1: Split the line into three parts
    parts = line.split("|")
    # Step 2: Remove extra spaces
    time = parts[0].strip()
    sender = parts[1].strip()
    text = parts[2].strip()
    # Step 3: Separate hour and minute
    hour, minute = time.split(":")
    # Step 4: Convert to integers
    hour = int(hour)
    minute = int(minute)
    # Step 5: Return the tuple
    return ((hour, minute), sender, text)
# Test the function
result = parse_line("15:18 | Tina | zzz... still asleep")

print(result)


def load_chat(filename=CHAT_FILE):
    """Read the whole chat file and return a LIST of message tuples. (Already done!)"""
    messages = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "" or line.startswith("#"):      # skip blank lines and comments
                continue
            messages.append(parse_line(line))
    return messages


# -------------------------------------------------------------------
# STEP 2: lists + list comprehensions
# -------------------------------------------------------------------
def messages_from(messages, sender):
    """Return a list with the TEXT of every message sent by one critter."""
    # TODO 2a: ONE line with a list comprehension.
    #   Loop over the messages with   for time, who, text in messages
    #   and keep text only if who == sender
    return [text for time, who, text in messages if who == sender]
def shouts(messages):
    """Return a list with the text of every message written in ALL CAPS."""
    # TODO 2b: ONE line with a list comprehension.
    # Keep the text of each message only if the text is ALL CAPS.
    # Tip: .isupper() returns True for "CAKE!" and False for "Cake!"
    return [text for time, who, text in messages if text.isupper()]



# -------------------------------------------------------------------
# STEP 3: dictionaries
# -------------------------------------------------------------------

def count_messages(messages):
    """Return a dictionary: how many messages each critter sent.
    {"Biscuit": 8, "Mochi": 4, ...}
    """
    # TODO 3: build a dictionary that counts messages per sender.
    # Step 1: Start with an empty dictionary
    counts = {}
    # Step 2: Loop through each message
    for time, sender, text in messages:
        # Step 3: Add 1 to the sender's count
        counts[sender] = counts.get(sender, 0) + 1
    # Step 4: Return the dictionary
    return counts



def top_talker(counts):
    """Return a TUPLE (name, number) for the critter who sent the most messages. (Already done!)"""
    best_name = max(counts, key=counts.get)
    return (best_name, counts[best_name])


def drama_scores(messages):
    """Dictionary comprehension: total exclamation marks per critter. (Already done!)"""
    senders = {sender for time, sender, text in messages}
    return {name: sum(text.count("!") for time, who, text in messages if who == name)
            for name in senders}
