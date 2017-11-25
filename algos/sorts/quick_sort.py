# QuickSort - recursive/divide and conquer - good for large data sets
# Worst Case is O(n^2)
# Average case is O(n log n)
# Performance depends largely on Pivot selection
# To choose a pivot its best to use median of three

def quick_sort(arr):
    
    quick_sort_help(arr, 0, len(arr)-1)

def quick_sort_help(arr, first, last):
    
    if first < last:

        splitpoint = partition(arr, first, last)

        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)

def partition(arr, first, last):
    
    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:

            leftmark += 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:

            rightmark -= 1

        if rightmark < leftmark:
            done = True

        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

arr = [2,5,6,3,7,8,0,11,10,12,16,14]
quick_sort(arr)
print(arr)