#!/usr/bin/python


def higher_lower(word):
    """Takes a word and returns the first letter lowercase"""
    return word.lower()[0]


def search(num_seq, count):
    """Binary search througha a sequence of numbers"""
    midpoint = len(num_seq) // 2
    answer = higher_lower(input(f"Is the number: {num_seq[midpoint]} (y)es?, if not is it (h)igher or (l)ower?"))
    

    if answer == 'y':
        return "Yay", count
    elif len(num_seq) == 1:
        return "Narrowed down to 1 digit", count
    elif answer == 'h':
        return search(num_seq[midpoint:], count + 1)
    elif answer == 'l':
        return search(num_seq[0:midpoint], count + 1)

    
num_seq = [number for number in range(0, 101)]
print("Think of a number between 0 and 100 (inclusive), I will try and guess it")
found_string, num_guesses = search(num_seq, 1)


print(f'{found_string}, it took {num_guesses} guess attempts')