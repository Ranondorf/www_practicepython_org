#!/usr/bin/python
# Basically exercise 5 again, but will try and code it in a different way


import random

# In one line finding the overlap of two randomly generated "lists"
print(list(set([random.randint(1, 30) for num in range(1, random.randint(1, 100))]).intersection(set([random.randint(1, 30) for num in range(1, random.randint(1, 100))]))))