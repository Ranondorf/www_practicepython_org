#!/usr/bin/python


import random

class Solution:
    def __init__(self):
        pass
    def create_list(self):
        list_1 = [random.randint(0,30) for num in list(range(random.randint(0,31)))]
        print(f'Created: {list_1}')
        return list_1



    def run(self):
        set_1 = set(self.create_list())
        set_2 = set(self.create_list())
        
        print(f'Common items are: {set_1.intersection(set_2)}')





a = Solution()
a.run()