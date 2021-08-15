#CodingBat - Python

#string_splosion

#Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
  result = ""
  for i in range(1, len(str) + 1):
    result += str[:i]           # --> result = result + str[:i]
   
  return result

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
