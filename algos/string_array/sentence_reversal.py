# Given a string of words, reverse all the words and remove trailing whitespace.
# 'This is the best' => 'best the is This'

# Python's methods using split(), slicing or use of reversed

def rev_word1(s):
    return " ".join(reversed(s.split()))

def rev_word2(s):
    return " ".join(s.split()[::-1])


# Basic algorithm

def rev_word3(s):

    words = []
    length = len(s)
    spaces = [' ']

    #Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # if element isn't a space
        if s[i] not in spaces:

            # the word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:

                # get index where word ends
                i += 1
            
            # append that word to the list
            words.append(s[word_start:i])

        #add to index
        i += 1
    
    # join the reversed words
    return " ".join(reversed(words))