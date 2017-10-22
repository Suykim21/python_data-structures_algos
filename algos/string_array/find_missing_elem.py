# Find the missing element
# finder([1,2,3,4],[3,1,4])
# expected output: 2

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    # zip([1,2,3], [4,5,6])
    # returns [(1,4), (2,5), (3,6)]
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]

# linear time solution

import collections

def finder2(arr1,arr2):

    # defaultdict - adds the key to the dict.
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        
        else:
            d[num] -= 1

arr1 = [5,5,7,7]
arr2 = [5,7,7]
finder2(arr1,arr2)

# XOR approach

def finder3(arr1, arr2):
    result = 0

    #perform an XOR between the numbers in the arrays
    for num n arr1+arr2:
        result^=num
        print result
    
    return result