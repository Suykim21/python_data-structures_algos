# Given two strings, write a method to decide if one is permutation of the other.

# O(n)
# collections are built-in high performance container datatypes
from collections import Counter

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for char in str1:
        counter[char] += 1

        # prints Counter({'y':2,'o':2, ' ':3 })
        print(counter)
    for char in str2:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True

check_permutation('yoyo   ', 'oyoy   ')



# ****************************
# Generate the all possible permutation in a given string
# def permutation(string):

#     if len(string) == 0:
#         return False

#     if len(string) == 1:
#         return [string]

#     l = []

#     # iterate the input(1st) and calculate the permutation
#     for i in range(len(string)):
#         m = string[i]

#         # extract string[i] pr m from the list.
#         # remString is remaining list

#         # string[:end] - items from the beginning through end - 1
#         # string[start:] - items start through the rest of the array
#         remString = string[:i] + string[i+1:]
#         print(remString)

#         # Generating all permutations where m is first element
#         for p in permutation(remString):
#             l.append([m] + p)
#     return len

# # testing
# data = list('123')
# for p in permutation(data):
#     print(p) 