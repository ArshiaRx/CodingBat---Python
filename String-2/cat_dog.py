#CodingBat - Python

#cat_dog

#Return True if the string "cat" and "dog" appear the same number of times in
#the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    count1, count2 = 0, 0
    
    for e in range(len(str)):
        if str[e:e+3] == "cat":
            count1 += 1
        elif str[e:e+3] == "dog":
            count2 += 1
            
    if count1 == count2:
        return True
    return False


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))