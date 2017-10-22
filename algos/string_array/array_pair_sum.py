# Given an interger Array, output all the unique pairs that sum up to a specific value k.

# pair_sum([1,3,2,2] 4)
# returns (1,3) and (2,2)

def pair_sum(arr, k):

    if len(arr)<2:
        return False

    # set() - an unordered collection with no duplicate elements
    seen = set()
    output = set()

    for num in arr:

        # pair_sum([1,3,2,2],4)
        # for every number in an array, we are looking for 4-1 or index of 0 = 3.
        target = k-num

        if target not in seen:
            # add 3 to seen set.
            seen.add(num)

        else:
            # find min and max between num and target ex: (1,3) = 4
            output.add( ( (min(num, target)), (max(num, target)) ) )

    print '\n'.join(map(str,list(output)))

    return len(output)