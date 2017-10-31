# Assume you have method isSubstring which checks if one string is a substring of another.
# Given two strings, s1 and s2, write code to check if s3 is a rotation of s1 using only one call to isSubstring.

# 'abcdefg' 
# 'abc' => is a substring of 'abcdefg'

s1 = 'waterbottle'
s2 = 'erbottlewat'

def isSubstring(s1,s2):
    return True if s2 in s1 else False

def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        # 'waterbottlewaterbottle' => allows us to find substring of s2 regardless of which direction it rotates
        s1 += s1
        return isSubstring(s1,s2)

print(isRotation(s1,s2))