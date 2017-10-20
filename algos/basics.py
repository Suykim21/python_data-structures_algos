# Print 1-255

# for x in range(1,256):
    # print(x)

#  Print odd numbers from 1 to 10

# for x in range(1,11):
    # if(x%2==1):
        # print(x)

# Print the sumof al the odd numbers from 1 to 10

# sum = 0

# for x in range(1, 11):
    # if(x%2==1):
        # sum = sum + x
# print(sum)

# def addOddNumbers(numbers):
#     total = 0
#     for num in numbers:
#         if (num%2==1):
#             total += num
#     print(total)

# addOddNumbers([1,2,3,4,5,6,7,8,9])

# Iterating through the list

# x = [1,3,5,7,9,13]

# for i in x:
#     print(i)

# Find Max, given an list with multiple values

# x = [-3,3,5,4]
# print (max(x))

# Find average, given a list with multiple values

# x=[2,3,5,6,17]
# average = sum(x)/len(x)
# print(average)

# Array with odd numbers

# def appendOdd(numbers):
#     odd = []
#     for number in numbers:
#         if(number%2==1):
#             odd.append(number)
#     print(odd)

# appendOdd([1,2,3,4,5,6,7,8,9])

# Greater than Y
# x=[1,3,5,7]
# y=3
    #utilize list comprehensions!!
# print (sum(i > y for i in x))

#Square the values

# def square(list):
#     print([i ** 2 for i in list])
# square([1,5,10,-2])

# Eliminate Negative Numbers

# def remove_odd(x):
#     print([i for i in x if i>0])

# remove_odd([-1,-3,-4,4,5,6])

# Max, min, and average in a list

# x = [-3,3,5,4]
# print (max(x))
# print (min(x))
# average = sum(x)/len(x)
# print(average)

# Shifting the values in the list

# def rotate(l, n):
    # rotates to the left
    # print(l[n:] + l[:n])

# list = [1,2,3,4,5]

# prints values at index of 2 - [3,4,5]
# print(list[2:])
# prints first two indices [1,2]
# print(list[:2])
# rotate(list, 4)

# Number to string, replace negative numbers with string
# x = [-1,4,-1,2]
# for i in x:
#     if(x[i]<0):
#         x[i] = "Dojo"
# print(x)

# Create random list(10 values)
# import random
# my_randoms = random.sample(range(1,101),10)
# print(my_randoms)

# Swapping two values
# list = [-3,5,1,3,2,10]
# temp = list[2]
# list[2] = list[0]
# list[0] = temp

# Reverse the list by swapping two values 
def reverse(seq):
    # Reverses elements of a list
    for i in range(len(seq)/2):
        x = seq[i]
        y = seq[-i-1]
        seq[i] = y
        seq[-i-1] = x

l = ['a', 'b', 'c', 'd', 'e']
reverse(l)
print(l)


# Removing Negatives

list = [0,-1,2,-3,4,-5,6]

def removeNegatives(list):
    # I want 'i' for each 'i' in list if 'i' is more than 0
    num_list = [i for i in list if i>=0]
    print(num_list)
removeNegatives(list)

# Long version:
my_list = []
for i in list:
    if i>=0:
        my_list.append(i)
print (my_list)