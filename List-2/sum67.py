#CodingBat - Python

#sum67

#Return the sum of the numbers in the array, except ignore sections of numbers
#starting with a 6 and extending to the next 7 (every 6 will be followed by at
#least one 7). Return 0 for no numbers.


# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4


def sum67(nums):
  total, deep_sixed = 0, False
  for e in nums:
    if e == 6:
      deep_sixed = True
    elif deep_sixed and e == 7:
      deep_sixed = False
    elif not deep_sixed:
      total += e
  return total


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
