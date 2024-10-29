#!/usr/bin/python


input_string = "My name is Donkey Kong and I am really big"


temp_list = ' '.join(input_string.split()[::-1])
print(temp_list)