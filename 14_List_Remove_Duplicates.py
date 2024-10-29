#!/usr/bin/python


import random as r


class SolutionSets:
    def run(self, input_list):
        """Function that executes solution using sets"""
        return set(input_list)


class SolutionLists:
    def run (self, input_list):
        """Function that executes solution using lists"""
        result_list = []
        for item in input_list:
            if item not in result_list:
                result_list.append(item)
        return result_list


def generate_random_list():
    """Generate a list of random length and random numbers"""
    return [r.randint(1,10) for num in range(1, r.randint(3, 50))]


random_list = generate_random_list()
print(f'This is the original random list: {random_list}')


set_solution = SolutionSets()
print(f'Solution using sets: {set_solution.run(random_list)}')


list_solution = SolutionLists()
print(f'Solution using sets: {list_solution.run(random_list)}')