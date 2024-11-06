#!/usr/bin/python


import random


def create_weak(filename):
    word_list = []


    with open(filename, 'r') as word_file:
        line = word_file.readline().rstrip()
        word_list.append(line)


        while line:
            line = word_file.readline().rstrip()
            word_list.append(line)


    return random.choice(word_list)


def random_symbol():
    return chr(random.choice([i for i in range(33, 48)] + [i for i in range(58, 65)] + [i for i in range(91, 97)] + [i for i in range(123, 127)]))


def create_strong(length):
    """Create strong password"""
    

    password_list = [chr(random.randint(65, 90)), chr(random.randint(97, 122)), str(random.randint(0, 9)), random_symbol()]


    for i in range(0, length - 4):
        password_list += [chr(random.randint(33, 126))]

    
    return password_list


def main():
    print("Welcome to the password generator\n\n")
    pass_type = input("Do you want a strong password: Yes or No? ")
    

    if pass_type.lower()[0] == 'y':
        password = "".join(create_strong(15))
    else:
        password = create_weak('30_sowpods.txt')


    print(f'The generated password is : {password}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))