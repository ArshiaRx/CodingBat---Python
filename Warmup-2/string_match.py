#CodingBat - Python

#string_match

#Given 2 strings, a and b, return the number of the positions where they contain
#the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx",
#"aa", and "az" substrings appear in the same place in both strings.


# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
    count = 0
    
    a_length, b_length = len(a), len(b)
    shorter_length = min(a_length, b_length)  #shorter_length = min(len(a), len(b)) 
                                              #returns the shorter length value
    for e in range(shorter_length-1):   #from shorter length count until 2nd 
                                        #last index
        sub_a = a[e:e+2]
        sub_b = b[e:e+2]
        if sub_a == sub_b:
            count += 1
    return count

#To check:
#print(string_match('xxcaazz','xxbaaz'))
#print(string_match('abc', 'abc'))
#print(string_match('abc', 'axc'))
