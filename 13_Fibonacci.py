#!/usr/bin/python


class Solution:
    def fibonacci(self):
        """Initial query for number from user"""
        number = int(input("Please enter the number of Fibonacci sequence numbers you want: "))

        list_numbers = [1, 1]

        if number == 1:
            return list_numbers.pop()
        elif number == 2:
            return list_numbers
        
        for i in range(2, number):
            list_numbers.append(list_numbers[i - 1] + list_numbers[i - 2])

        return list_numbers

        
answer = Solution()
print(answer.fibonacci())