#CodingBat - Python

#left2

#Given a string, return a "rotated left 2" version where the first 2 chars are
#moved to the end. The string length will be at least 2.

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
    if len(str) <= 1:
        return str
    else:
        return str[2:] + str[:2]
    
#To check:    
#print(left2('Hello'))
#print(left2('java'))
#print(left2('Hi'))
