#CodingBat - Python

#first_half

#Given a string of even length, return the first half. So the string "WooHoo" 
#yields "Woo".

#first_half('WooHoo') → 'Woo'
#first_half('HelloThere') → 'Hello'
#first_half('abcdef') → 'abc'


def first_half(str):
  half = len(str) // 2
  return str[:half]

#To check
#print(first_half('WooHoo'))
#print(first_half('HelloThere'))
#print(first_half('abcdef'))
