#CodingBat - Python

#has22

#Given an array of ints, return True if the array contains a 2 next to a 2
#somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
    
  prev_two = False               #Generally prev_two is False
  
  for e in nums:
    this_two = e == 2
    
    if prev_two and this_two:      #when we say if something that makes it True
                      #this means if prev_two is True and this_two element is 2
      return True                   #return us True
  
    prev_two = this_two       #then prev_two element becomes 2
    
  return False                            #if otherwise return False


print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))


