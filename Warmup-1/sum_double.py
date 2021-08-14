#CodingBat - Python

#sum_double

# Given two int values, return their sum. Unless the two values are the same, 
# then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 

def sum_double(a, b):
  sum = (a + b)               #store the sum in a local variable
  if a == b:                  #double the sum if a and b are the same
    return sum * 2
  else:
    return sum 

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2)) 
# =============================================================================

#def sum_double(a, b):
    #sum = a + b
    #return 2 * sum if a == b else sum
    
    
#def sum_double(a, b):
    #return (a + b) * 2 if a == b else (a + b)
