MIN = -2**31
MAX = (2**31) - 1
#This function reverses every number between MIN and MAX values
import math
class Solution:
    def reverse(self, x: int) -> int:
        number = x
        negative = False
        reverse_num = []


        #transform int into list
        if (number < 0):
            number  = abs(number)
            negative = True
        while(number >= 10):
            reverse_num.append(number % 10)
            number = math.floor(number/10)
        reverse_num.append(number)
        result_str = ''.join(map(str,reverse_num))
        result = int(result_str)

        if((number >=  MAX) or (number <= MIN)):
            return 0

        if(negative):
            result = - result
        return result