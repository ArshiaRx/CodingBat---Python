#CodingBat - Python

#xyz_there

#Return True if the given string contains an appearance of "xyz" where the xyz
#is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does
#not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    dot = False
    count = 0
    
    for e in range(len(str)):
        if not dot and str[e:e+3] == "xyz":
            return True
        dot = str[e] == "." 
    return count > 0


print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))