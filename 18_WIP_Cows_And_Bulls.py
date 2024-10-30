#!/usr/bin/python


import random as r


target_number = [r.randint(0, 9) for num in range(0, 4) ]
target_number = [0, 5, 4, 8]
print(target_number)


# guess_list = input("Please make a guess of a 4 digit number: ")
hits = {'cow': 0, 'bull': 0}
guess_count = 0


while True:
    guess_list = [int(digit) for digit in input("Please make a guess of a 4 digit number: ")]
    guess_count += 1

    temp_target = target_number.copy()
    for i in range(0, 4):
        for j in range(0, 4):
            if guess_list[i] == temp_target[j] and i == j:
                hits['cow'] += 1
                temp_target[j] = -1
                break
            elif guess_list[i] == temp_target[j] and i != j:
                hits['bull'] += 1
    
    
    if hits['cow'] == 4:
        print(f'You guessed it in {guess_count} attempts')
        break
    else:
        if hits['cow'] == 1:
            print('1 cow')
        elif hits['cow'] > 1:
            print(f'{hits["cow"]} cows')
        else:
            pass
        if hits['bull'] == 1:
            print('1 bull')
        elif hits['bull'] > 1:
            print(f'{hits["bull"]} bull')
        else:
            pass
    
        hits = {'cow': 0, 'bull': 0}

