#!/usr/bin/python


import random as r


def main():
    target_list = []
    
    
    while len(target_list) < 4:
        new_number = r.randint(0,9)
        if new_number not in target_list:
            target_list.append(new_number)


    # guess_list = input("Please make a guess of a 4 digit number: ")
    digit_seen_count = [{'cow': 0, 'bull': 0} for n in range(10)]
    guess_count = 0
    bull_count = 0
 

    while bull_count != 4:
        guess_list = [int(digit) for digit in input("Please make a guess of a 4 digit number (Each digit must be unique): ")]
        guess_count += 1
        bull_count = 0
        cow_count = 0


        for i in range(4):
            for j in range(4):
                if guess_list[i] == target_list[j] and i == j:
                    digit_seen_count[guess_list[i]]['bull'] += 1
                    digit_seen_count[guess_list[i]]['cow'] = 0
                elif guess_list[i] == target_list[j] and i != j and digit_seen_count[guess_list[i]]['bull'] != 1:
                    digit_seen_count[guess_list[i]]['cow'] += 1
                else:
                    # Do nothing
                    pass


        for i in range(10):
            bull_count += digit_seen_count[i]['bull']
            cow_count += digit_seen_count[i]['cow']


        print(f'bull count : {bull_count} and cow count : {cow_count}')
        digit_seen_count = [{'cow': 0, 'bull': 0} for n in range(10)]


    print(f'Well done, it took you {guess_count} guesses to guess the correct answer')
        


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))