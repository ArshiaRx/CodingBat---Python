#CodingBat - Python

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears
#in the array somewhere.

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
    array_list = [1, 2, 3]
    if len(nums) < len(array_list):
        return False
    
    for e in range(len(nums) - len(array_list) + 1):
        
        if nums[e:e+len(array_list)] == array_list:
            return True
    
    return False
    

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
