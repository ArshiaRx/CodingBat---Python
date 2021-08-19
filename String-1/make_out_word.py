#CodingBat - Python

#make_out_word

#Given an "out" string length 4, such as "<<>>", and a word, return a new 
#string where the word is in the middle of the out string, e.g. "<<word>>".

#make_out_word('<<>>', 'Yay') → '<<Yay>>'
#make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
#make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(out, word):
  
  half_length = len(out) // 2
  
  return out[:half_length] + word + out[half_length:]

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))