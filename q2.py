
# ******************************
# Make your Code
longest = 0
shortest = 100
while True:
    ustr = input('input a string: ')
    if ustr == 'stop' or ustr == 'STOP':
        break
    if len(ustr) > longest:
        longest = len(ustr)
        longword = ustr
    if len(ustr) < shortest:
        shortest = len(ustr)
        shortword = ustr
print(f'Longest word: {longword}, Shortest word: {shortword}')
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
