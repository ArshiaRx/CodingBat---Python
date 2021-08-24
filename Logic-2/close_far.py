#CodingBat - Python

#close_far

#Given three ints, a b c, return True if one of b or c is "close" (differing 
#from a by at most 1), while the other is "far", differing from both other
#values by 2 or more. Note: abs(num) computes the absolute value of a number.


# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True


def close_far(a, b, c):
  
  b_close = abs(a-b) < 2
  c_close = abs(a-c) < 2
  b_far = abs(a-b) > 1 and abs(c-b) > 1
  c_far = abs(a-c) > 1 and abs(b-c) > 1
  
  return b_close and c_far or b_far and c_close


print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))