#!/usr/bin/python

class Solution:
    def __init__(self):
        pass
    def run(self):
        num = int(input("Please input a number: "))
        temp_list = list(range(2, (num // 2) + 1))
        print([item for item in temp_list if num % item == 0])

a = Solution()
a.run()