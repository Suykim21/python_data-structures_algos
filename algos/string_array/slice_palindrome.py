# Slicing Notation - Python

# a[start:end] items starttrhough end -1
# a[start:] items start through the rest of the array
# a[:end] items from the beginning through end -1
# a[:] a copy of the whole array

# a[start:end:step] start trhough not past end, by step

a = [1,2,3,4,5,6]

# [2,3] prints index 1 and 2 - start at index 1 and end before index 3
print(a[1:3])

# [3,4,5,6] starts at index 2 onwards
print(a[2:])

# [1,2,3,4] prints upto index 3
print(a[:4])

# prints whole array
print(a[:])

# [2,4] start at index 1 ends at index 4, printing every two indexes
print(a[1:5:2])

# [5,6] prints last two indexes
print(a[-2:])

# [1,2,3,4,5] prints eveything but the last one index
print(a[:-1])

# [6,5,4,3,2,1] reverses the list
print(a[::-1])

# Check if the string is palindrome or not


def isPalindrome(s):
    if s[::-1] == s:
        # print(True)
        return True
    else:
        # print(False)
        return False


isPalindrome('radar')
isPalindrome('client')

