#CodingBat - Python

#front_back

#Given a string, return a new string where the first and last chars have been
#exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  
  if len(str) <= 1:
    return str
    
  else:    #back          #middle        #front
    return str[-1] + str[1:len(str)-1] + str[0]
    
print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
# =============================================================================
#This code below works on any platform, except on CodingBat. 

#def front_back(str):
   #front = str[0]
   #mid = str[1:len(str)-1]
   #back = str[-1]
    
   #if len(str) == 1:
       #return str
   #elif len(str) > 1:
       #return back + mid + front
# =============================================================================

# def front_back(str):
#     return str[-1] + str[1:-1] + str[0] if len(str) > 1 else str
