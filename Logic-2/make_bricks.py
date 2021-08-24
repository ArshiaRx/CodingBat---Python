#CodingBat - Python

#make_bricks

#We want to make a row of bricks that is goal inches long. We have a number of
#small bricks (1 inch each) and big bricks (5 inches each). Return True if it is
#possible to make the goal by choosing from the given bricks. This is a little
#harder than it looks and can be done without any loops.


# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

#NOTE:  Most of the time try to solve for False statement first then, True Booleans

def make_bricks(small, big, goal):
    return False if goal > (big * 5) + (small * 1) or (goal % 5) > small else True


print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
# =============================================================================

# def make_bricks(small, big, goal):
#     if small < (goal % 5) or (small + big * 5) < goal:
#        return False
#     else:
#        return True


# def make_bricks(small, big, goal):
#     if small < (goal % 5):
#         return False
#     elif goal > (big * 5 + small * 1):
#         return False
#     else:
#         return True


    
  