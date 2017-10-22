# Anagram - ex: dog is anagram of god

# def anagram(s1, s2):
#     # replace takes in two arguments
#     # replace space with no space
#     s1 = s1.replace(' ','').lower()
#     s1 = s2.replace(' ','').lower()

#     # sorted() - puts in alphabetical order
#     # return sorted(s1) == sorted(s2)

# anagram('dog', 'god')

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge Case Check - to check if both strings has equal number of letters
    if len(s1) != len(s2):
        return False

    # to check to see if it equals out to 0.
    count = {}

    for letter in s1:
        # if the letter exist on dict already, add one in addition to default one.
        if letter in count:
            count[letter] += 1
        # if its new letter, add one
        else:
            count[letter] = 1

    for letter in s2:
        # if the existing letter shows up again, substract one
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        # to be considered anagram it needs to equal to 0.
        if count[k] != 0:
            return False

    return True
