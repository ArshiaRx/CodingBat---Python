#CodingBat - Python

#near_hundred

#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
#computes the absolute value of a number.

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

def near_hundred(n):
  return True if (90 <= n <= 110) or (190 <= n <= 210) else False 

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
# =============================================================================

#def near_hundred(n):
# return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
