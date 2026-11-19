"""
detective.py  -  catch the cake thief

STEP 4  sets                        senders_between(), who_mentioned(), find_culprit()
STEP 5  arguments + scope           search(), count_words(), add_drama()
"""


# -------------------------------------------------------------------
# STEP 4: sets
# -------------------------------------------------------------------

def senders_between(messages, start, end):
    """Return a SET of critters who sent a message between start and end (both included).

    start and end are (hour, minute) tuples, e.g. (15, 0) and (15, 30).
    """
    # TODO 4a: ONE line with a SET comprehension.
    # Keep the sender of every message whose time is between start and end.
    return {sender for time, sender, text in messages if start <= time <= end}

def who_mentioned(messages, phrase):
    """Return a SET of critters whose message contains phrase (ignore upper/lower case)."""
    # TODO 4b: ONE line with a set comprehension.
    # Keep the sender if phrase appears in the text.
    # Ignore upper/lower case.
    return {sender for time, sender, text in messages if phrase.lower() in text.lower()}


def find_culprit(online, knew_secret, alibis):
    """Return the set of critters who were online AND knew the secret, minus anyone with an alibi."""
    # TODO 4c: ONE line with set operators.
    # & keeps names that are in BOTH sets.
    # - removes names that are in the second set.
    return (online & knew_secret) - alibis


# -------------------------------------------------------------------
# STEP 5: arguments
# -------------------------------------------------------------------

def search(messages, word, sender=None, ignore_case=True):
    """Return a list of message tuples whose text contains word."""
    results = []
    for time, who, text in messages:
        # Check if the sender matches
        if sender is not None and who != sender:
            continue
        # Check if the word appears in the text
        if ignore_case:
            match = word.lower() in text.lower()
        else:
            match = word in text
        if match:
            results.append((time, who, text))
    return results


def count_words(messages, *words):
    """Return a dictionary counting how many messages contain each word."""
    counts = {}
    for word in words:
        counts[word] = len(search(messages, word))
    return counts
# -------------------------------------------------------------------
# STEP 5: scope
# -------------------------------------------------------------------
total_drama = 0
def add_drama(text):
    """Add drama points for one message to the global total_drama. Return the points."""
    global total_drama
    points = text.count("!")
    if text.isupper():
        points += 5
    total_drama = total_drama + points
    return points