#CodingBat - Python

#near_ten

#Given a non-negative number "num", return True if num is within 2 of a multiple
#of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.

# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True

def near_ten(num):
  last =  num % 10
  return last in (0, 1, 2, 8, 9)

#To Check:
#print(near_ten(12))
#print(near_ten(17))
#print(near_ten(19))
