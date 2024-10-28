#!/usr/bin/python


class Solution:
    def __init__(self):
        pass


    def run(self):
        print(f'Is the string a palindrome: {self.core()}')


    def core(self):
        word = input("Please enter a string to check if it is a palindrome: ")
        
        
        # Case for 0 and 1 length string
        if word == "" or len(word) == 1:
            return True
        

        for i in range(len(word) // 2):
            if word[i] != word[-(i + 1)]:
                return False
        return True
    

a = Solution()
a.run()