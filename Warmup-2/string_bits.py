#CodingBat - Python

#string_bits

#Given a string, return a new string made of every other char starting with the
#first, so "Hello" yields "Hlo".

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'


def string_bits(str):
  result = ''
  string = len(str)
  
  for i in range(string):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
