# Find Triplet with given Sum in an Array
# Given an unsorted array of integers, find a triplet with given sum in it.

# Input:
# arr = [2,7,4,0,9,5,1,3] sum = 6
# Output:
# (0 1 5), (0 2 4), (1 2 3)

def three_sum(arr):
    arr = sorted(arr)
    output = set()
    for k in range(len(arr)):
        target = -s[k]
        i = k+1
        j = len(s) - 1
        while i < j:
            sum_two = s[i] + s[j]
            if sum_two < target:
                i += 1
            elif sum_two > target:
                j -= 1
            else:
                output.add((s[k], s[i], s[j]))
                i += 1
                j -= 1
    return output