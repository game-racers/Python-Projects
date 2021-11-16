__author__ = 'guinnc'

def removeSpaces(s):
    if len(s) == 1:
        return s
    if s[0] == ' ':
        return removeSpaces(s[1:])
    else:
        return s[0] + removeSpaces(s[1:])


t = "A man, a plan, a canal, Panama!"
print(t)
print(removeSpaces(t))
