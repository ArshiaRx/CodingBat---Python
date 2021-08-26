#CodingBat - Python

#big_diff

#Given an array length 1 or more of ints, return the difference between the
#largest and smallest values in the array. Note: the built-in min(v1, v2) and
#max(v1, v2) functions return the smaller or larger of two values.

# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8


def big_diff(nums):
  big, small = nums[0], nums[0]
  for e in nums:
    if e > big:
      big = e
    elif e < small:
      small = e
  return big - small
      

#To check
#print(big_diff([10, 3, 5, 6]))
#print(big_diff([7, 2, 10, 9]))
#print(big_diff([2, 10, 7, 2]))
