##CodingBat - Python

#diff21
#Given an int n, return the absolute difference between n and 21, except
#return double the absolute difference if n is over 21.

#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
  
  diff = abs(n-21)
  
  if n > 21:
    return diff * 2
  else:
    return diff
# =============================================================================
  
#def diff21(n):
  #diif = abs(n-21)
  #return  2 * diff if n > 21 else diff

