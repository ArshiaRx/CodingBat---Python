#CodingBat - Python

#double_char

#Given a string, return a string where for every char in the original, there
#are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
    
  return result


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
# =============================================================================

# def double_char(str):
#   str2 = ""
#   for i in str:
#     str2 = str2 + i + i
#   return str2

  
# def double_char(str):
#   str2 = ""
#   for e in str:
#     str2 += (e * 2)
#   return str2
