# Implement an algorithm to determine if a string has all unique characters. What f you cannot use additional data structures?

# O(n)
# defines unique characters
def unique(string):
    uchars = list(set(string))
    # print(uchars)

# prints ['h', 'e', 'l', 'o']
unique('hello')



# O(n) - we have to check every character in the input string to check for unique characters
def is_unique(string):
    char_seen = []
    for char in string:
        if char in char_seen:
            # print('not unique')
            return False
        char_seen.append(char)
    # print ('unique')
    return True

is_unique('hello')


# O(1) - usng hash tables to avoid having to iterate through the list
# however, we'll be using more memory space as we have to store booleans to each characters
def is_unique(string):
    
    # Every key has value of False
    # prints {'h':False, 'e':False ...}
    char_seen = {key: False for key in string}

    for char in string:
        if char_seen[char] == False:
            char_seen[char] = True
        else:
            print('not unique')
            return False
    print('unique')
    return True

is_unique('hello')
is_unique('paul')
