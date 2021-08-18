#CodingBat - Python

#Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    count = 0
    for e in range(len(nums)):
        if nums[e] == 9:
            count += 1
    return count

#To Check
#print(array_count9([1, 2, 9]))
#print(array_count9([1, 9, 9]))
#print(array_count9([1, 9, 9, 3, 9]))
