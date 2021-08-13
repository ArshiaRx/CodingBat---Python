#CodingBat - Python By Arshia Rahim

#Sleep_in
#The parameter weekday is True if it is a weekday, and the parameter vacation 
#is True if we are on vacation. We sleep in if it is not a weekday or we're 
#on vacation. Return True if we sleep in.

#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  if weekday and vacation or not weekday or vacation:
    return True
  else:
    return False

#Expected
#sleep_in(False, False) --> True
#sleep_in(True, False)  --> False
#sleep_in(False, True)  --> True
#sleep_in(True, True)   --> True
# ===========================================================================
  
#def sleep_in(weekday, vacation):
  #return not weekday or vacation

  
#def sleep_in(weekday, vacation):
  #if vacation:
    #return True
  #else:
    #return not weekday

    
#def sleep_in(weekday, vacation): 
  #if not weekday:
    #return True
  #else:
    #return vacation
    
    

  
