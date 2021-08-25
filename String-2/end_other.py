#CodingBat - Python

#end_other

#Given two strings, return True if either of the strings appears at the very end
#of the other string, ignoring upper/lower case differences (in other words, the
#computation should not be "case sensitive"). Note: s.lower() returns the lowercase
#version of a string.


# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    #varibale.lower()  --> Turns the string into lowercase
    a = a.lower()
    b = b.lower()
    
# variable.endswith(something)  --> Checks if string variable end with (something) 
        
    return a.endswith(b) or b.endswith(a)    


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))   