#CodingBat - Python

#sum3

#Given an array of ints length 3, return the sum of all the elements.

# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

def sum3(nums):
    result = 0
    
    for e in nums:
        result += e       #result = result + e
        
    return result

#To check:
#print(sum3([1, 2, 3]))
#print(sum3([5, 11 , 2]))
#print(sum3([7, 0, 0]))
