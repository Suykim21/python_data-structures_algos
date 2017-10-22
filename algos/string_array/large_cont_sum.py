# Given an array of integers (positive and negative) find the largest continuous sum.
# large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
# expected output: 29

def large_cont_sum(arr):

    #Check to see if array is length 0
    if len(arr) ==0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = max(current_sum+num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum