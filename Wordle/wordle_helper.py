"""
Copyright (c) 2022 Ben

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

def check(word: str, compare: str) -> bool:
    """Marches a word vs a word, returns true or false"""
    for l1, l2 in zip(word, compare):
        if l1 == "_":
            pass
        elif l1 != l2:
            return False
    return True

def print_c(count: int):
    """print iterations"""
    if count % 100 == 0:
        print(f"Finished iterating {count} iterations")
    else:
        pass

def main():
    find = input("Enter the word using _ to represent unknown letters: ")
    find = find.lower()

    matches = []

    count = 0
    with open("Wordle/data/answerwordlist.txt", "r") as file:
        for word in file:
            print_c(count)
            match = check(find, word)
            if match:
                matches.append(word)
            count += 1

    print("Finished.")
    for match in matches:
        print(match)

if __name__ == "__main__":
    main()