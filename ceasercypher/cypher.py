# By _Leg3ndary#5759
from math import trunc

CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
RCAPS = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
RLOWER = "zyxwvutsrqponmlkjihgfedcba"

def encode(raw_string: str, shift: int) -> str:
    """
    Encode a string using a ceaser cypher shift
    """
    final = ""
    shift = int(shift)
    
    for char in raw_string:
        # Upper case
        if char in CAPS:
            letter_index = CAPS.find(char)
            index = shift + letter_index

            if index >= 25:
                index -= trunc(index / 25) * 25

            final += CAPS[index]

        # Lower case
        elif char in LOWER:
            letter_index = LOWER.find(char)
            index = shift + letter_index

            if index >= 25:
                index -= trunc(index / 25) * 25

            final += LOWER[index]

        # Anything that isn't alphabetical~
        else:
            final += char

    return final

def decode(raw_string: str, shift: int) -> str:
    """
    Decode a string using a ceaser cypher shift, essentially goes backwards
    """
    final = ""
    shift = int(shift)
    
    for char in raw_string:
        # Upper case
        if char in RCAPS:
            letter_index = RCAPS.find(char)
            index = shift + letter_index

            if index >= 25:
                index -= trunc(index / 25) * 25

            final += RCAPS[index]

        # Lower case
        elif char in RLOWER:
            letter_index = RLOWER.find(char)
            index = shift + letter_index

            if index >= 25:
                index -= trunc(index / 25) * 25

            final += RLOWER[index]

        # Anything that isn't alphabetical~
        else:
            final += char

    return final

# Testing
print(encode(input("Put something here encode : "), input("Shift: ")))

print(decode(input("Put something here decode : "), input("Shift: ")))