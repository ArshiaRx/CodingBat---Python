#CodingBat - Python

#extra_end

#Given a string, return a new string made of 3 copies of the last 2 chars of
#the original string. The string length will be at least 2.

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
  return str[len(str)-2:] * 3    #return from 2nd last index up to end * 3

#To check
#print(extra_end('Hello')) 
#print(extra_end('ab'))
#print(extra_end('Hi'))
