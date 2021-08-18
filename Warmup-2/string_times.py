#CodingBat - Python

#Given a string and a non-negative int n, return a larger string that is n 
#copies of the original string.

# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

def string_times(str, n):
    if n < 0:
        return False
    elif n >= 0:
        return str * n
 
#To Check
#print(string_times('Hi', 2))
#print(string_times('Hi', 3))
#print(string_times('Hi', 1))    
# =============================================================================

# def string_times(str, n):
#     result = ""
#     for e in range(n):
#         result += str     # --> result = result + str
#     return result
