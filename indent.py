# x = 0
# while x < 10:
#     print(x)
#     x = x + 1

def get_summ(one, two, delimeter = '&'):
    result = (f'{one}{delimeter}{two}')
    return result

print(get_summ('Learn','Python').upper())
