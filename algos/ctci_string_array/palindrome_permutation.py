# Write a function to check if a string is a permutation of a palindrome
import string

# O(n)
def permutationPali(str):

    # dict.fromkeys(seq[, value])
    # a : false, b : false...etc.
    d = dict.fromkeys(string.ascii_lowercase, False)
    count = 0

    for char in str:
        # lowercase letters are between 96 to 123
        if(ord(char) > 96 and ord(char) < 123):
            # Toggle between True and False
            d[char] = not d[char]
    print(d)

    for key in d:
        if d[key] is True:
            count += 1
            # if count is greater than one, it means it cannot be palindrome 
            # ex: 'abc' False 'aa bb cc eeeee' => 'abceeeeecab' - True
            if count > 1:
                return False

    return True

print (permutationPali('aabbccdde'))