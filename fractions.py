import math

def remainder(number, denominator):
    solution = math.floor(number / denominator)
    numerator = number % denominator


    if(numerator % denominator != 0):
        newNum = numerator
        newDen = denominator
        while newNum != 0:
            (newDen, newNum) = (newNum, newDen % newNum)
            print(newDen, newNum)
        gcd = newDen
        
        fraction = f'{math.floor(numerator / gcd)}/{math.floor(denominator / gcd)}'
        print(f'The answer is {solution} and {fraction}')
    else:
        print(f'The answer is {solution}')




remainder(16783593, 14)
