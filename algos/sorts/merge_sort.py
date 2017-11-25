# MergeSort is recursive
# Divide and Conquer algorithm
# Very efficient for large data sets not so much on small data

# Merge Sort does log n merge steps because each merge step doubles the list size
# it does n work for each merge step because it must look at every item
# O(n log n)

def merge_sort(arr):

    if len(arr) > 1:

        # double slash to make half an int, to avoid float like 1.5
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        # keeps splitting until len(arr) < 1
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # left arr pointer
        i = 0

        # right arr pointer
        j = 0

        # merge arr pointer
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]

                i += 1

            else:
                arr[k] = righthalf[j]
                j += 1

            k += 1

        # if there are still remaining values on left arr, add it to arr[k]
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        # if there are still remaining values on right arr, add it to arr[k]
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    print('Merging', arr)

arr =[11,3,4,6,3,7,0,10,23,17]
merge_sort(arr)
