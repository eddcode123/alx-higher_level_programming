#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None  # Return None if the dictionary is empty
    best_score = max(a_dictionary.values())  # Find the highest value
    best_key = None

    # Iterate through the dictionary to find the key associated with max value
    for key, value in a_dictionary.items():
        if (value == best_score):
            best_key = key
            break

    return (best_key)
