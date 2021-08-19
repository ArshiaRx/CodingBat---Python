#CodingBat - Python

#sum2

#Given an array of ints, return the sum of the first 2 elements in the array.
#If the array length is less than 2, just sum up the elements that exist, 
#returning 0 if the array is length 0.

# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

def sum2(nums):
    result = 0
    
    if len(nums) == 0:
        return result
    
    elif len(nums) < 2:
        for e in nums:
            result += e         #result = result + e
    
    else:
        result = nums[0] + nums[1]
    
    return result

#To check:
#print(sum2([1, 2, 3]))
#print(sum2([1, 1]))
#print(sum2([1, 1, 1, 1]))   
