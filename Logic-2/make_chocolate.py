#CodingBat - Python

#make_chocolate

#We want make a package of goal kilos of chocolate. We have small bars 
#(1 kilo each) and big bars (5 kilos each). Return the number of small bars to
#use, assuming we always use big bars before small bars. Return -1 if it cant
#be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2


def make_chocolate(small, big, goal):

  if goal >= 5 * big:
        remainder = goal - 5 * big
  else:
        remainder = goal % 5
        
  if remainder <= small:
      return remainder
        
  return -1


print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
