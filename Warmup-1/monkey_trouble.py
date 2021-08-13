#CodingBat - Python

#monkey_trouble

#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
#if each is smiling. We are in trouble if they are both smiling or if neither
#of them is smiling. Return True if we are in trouble.

#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
    return True if a_smile == b_smile else False

print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
# =============================================================================

# def monkey_trouble(a_smile, b_smile):
#    if (a_smile and b_smile) or (not a_smile and not b_smile):
#        return True
#    else:
#        return False


# def monkey_trouble(a_smile, b_smile):
#   if a_smile and b_smile:
#     return True
#   if not a_smile and not b_smile:
#     return True
#   if a_smile and not b_smile:
#     return False
#   if not a_smile and b_smile:
#     return False


# def monkey_trouble(a_smile, b_smile):
#     both_smile = a_smile and b_smile
#     neither_smile = not (a_smile or b_smile)
#     return both_smile or neither_smile


# def monkey_trouble(a_smile, b_smile):
#     if a_smile:
#         return b_smile
#     else:
#         return not b_smile


# def monkey_trouble(a_smile, b_smile):
#     if b_smile:
#         return a_smile
#     else:
#         return not a_smile
