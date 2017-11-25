'''

Assignment: String and List Practice
Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:

• .find()

• .replace()

• min()

• max()

• .sort()

• len()

Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

'''

#find and replace
string = "If monkeys like bananas, then I must be a monkey!"
print string
print string.find("monkey")
string = string.replace("monkey", "alligator")
print string

#min and max
x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list


'''

Assignment: Multiples, Sum, Average
This assignment has several parts. All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!

Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

'''

#multiples A
for count in range(1, 1001, 2):
    print count

#multiples B
for count in range(5,1000001,5):
    print count

#sum list
my_numbers = [1, 2, 5, 10, 255, 3]
sum = 0
for i in my_numbers:
    sum += i
print sum

#average list
print sum/len(my_numbers)

'''

Assignment: Filter by Type
Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

Integer
If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

String
If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

List
If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

Test your program using these examples:

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
Copy
Hint: You might want to read about the type and isinstance functions

'''

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# set one of the above variables as the current one I'm testing
current_tester = lL

curr_type = type(current_tester)
if curr_type is int:
    if current_tester >= 100:
        print "That's a big number!"
    else:
        print "That's a small number!"
elif curr_type is str:
    if len(current_tester) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."
elif isinstance(current_tester, list):
    if len(current_tester) >= 10:
        print "Big list!"
    else: 
        print "Short list."            


'''

Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
Copy
# input
l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"
Copy
# input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"

'''

mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]

def identify_list_type(lst):
    new_string = ''
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is of string type"
        print "String:",new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)

'''

Assignment: Compare Lists
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
Copy
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
Copy
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
Copy
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']


'''

def compare_lists(list_one, list_two):
    if list_one == list_two:
        print "The lists are the same"
    else:
        print "The lists are not the same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]


compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare_lists(list_one, list_two)

'''

Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

Here's an example:

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
Copy
Hint: how many loops will you need to complete this task?


'''

def find_character(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):

        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])

    print new_list

test_list = ['hello','world','my','name','is','Anna']
find_character(test_list, 'o')


'''

Assignment: Checkerboard
Write a program that prints a 'checkerboard' pattern to the console.

Your program should require no input and produce console output that looks like so:

* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
Copy
Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. In our case we will alternate stars and spaces. The goal is to repeat a process several times. This should make you think of looping.


'''

def checkerboard():
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4


'''

Optional Assignment: Multiplication Table
Create a program that prints a multiplication table in your console.



Your table should look like the following example:

x   1  2  3  4  5  6  7  8   9  10  11  12
1   1  2  3  4  5  6  7  8   9  10  11  12
2   2  4  6  8 10 12 14 16  18  20  22  24
3   3  6  9 12 15 18 21 24  27  30  33  36
4   4  8 12 16 20 24 28 32  36  40  44  48
5   5 10 15 20 25 30 35 40  45  50  55  60
6   6 12 18 24 30 36 42 48  54  60  66  72
7   7 14 21 28 35 42 49 56  63  70  77  84
8   8 16 24 32 40 48 56 64  72  80  88  96
9   9 18 27 36 45 54 63 72  81  90  99 108
10 10 20 30 40 50 60 70 80  90 100 110 120
11 11 22 33 44 55 66 77 88  99 110 121 132
12 12 24 36 48 60 72 84 96 108 120 132 144
Copy
What is the most efficient way to produce the above output? 

Hint: Don't worry about getting it perfectly spaced, just ensure all the values are properly output!

'''

"""
Create a program that prints multiplication table in your console.
"""

print ' x 1 2 3 4 5 6 7 8 9 10 11 12'
for row in range(1, 12 + 1): 
    display_string  = ''
    for column in range(0, 12 + 1):
        if column is 0:
            display_string += ' ' + str(row)
        else:    
            display_string += ' ' + str(column * row)
    print display_string   


'''

Assignment: Fun with Functions
Create a series of functions based on the below descriptions.

Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

Your program output should look like below:

Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.
Copy
Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:

a = [2,4,10,16]
Copy
Then:

b = multiply(a, 5)
print b
Should print [10, 20, 50, 80 ].

Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:

def layered_multiples(arr):
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


'''

def odd_even():
    for x in range(1, 2001):
        if x % 2 == 0:
            print x, " this is an even number."
        else:
            print x, " this is an odd number."

odd_even()

def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

numbers_array = [3, 6, 8, 10, 67]

print multiply(numbers_array, 5)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x

'''

Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
The result should be like this:

Scores and Grades
Score: 87; Your grade is B
Score: 67; Your grade is D
Score: 95; Your grade is A
Score: 100; Your grade is A
Score: 75; Your grade is C
Score: 90; Your grade is A
Score: 89; Your grade is B
Score: 72; Your grade is C
Score: 60; Your grade is D
Score: 98; Your grade is A
End of the program. Bye!
Copy
Hint: Use the python random module to generate a random number

import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
random_num = random.randint()


'''

import random

def grade(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is A"
        else:
            print "You failed"
    print "End of the program.  Bye!"

grade(10)

'''

Assignment: Coin Tosses
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
Hint: Use the python built-in round function to convert that floating point number into an integer

x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1

'''


import random

def toss(reps):
    # print new_toss
    attempt_count = 1
    head_count = 0
    tail_count = 0
    result = ""
    result_string_complete = ""

    for x in range(1, reps):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            head_count += 1
            result = "head"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
        else:
            tail_count += 1
            result = "tail"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
        attempt_count += 1

toss(5001)


'''

Assignment: Stars
Write the following functions.

Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]
Copy
draw_stars(x) should print the following when invoked:

****
******
*
***
*****
*******
*************************
Copy
Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

For example:

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x) should print the following in the terminal:

****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj



'''

def stars(arr):
    for x in arr:
        print "*" * x


nums = [6,2,5,7,9]
stars(nums)

def stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars2(x)


'''


Assignment: Making and Reading from Dictionaries
Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

Write a function that will print something like the following as it executes:

My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python
Copy
There are two steps to this process, building a dictionary and then gathering all the data from it. Write a function that can take in and print out any dictionary keys and values.

Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.


'''


def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)
        
        # alternate method:
        # concatenating variables to strings commonly done with the .format() method (can be used on any string, or variable that
            # contains a string
        
        #print "My {} is {}".format(some_key, some_value)

'''

Assignment: Names
Write the following function.

Part I
Given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Copy
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
Copy
Part II
Now, given the following dictionary:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
Copy
Create a program that prints the following format (including number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
Copy
Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.


'''

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def show_students(arr):
    for student in students:
        print student['first_name'], student['last_name']

def show_all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)

show_students(students)
show_all(users)

'''

Assignment: Dictionary in, tuples out
Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

'''

def making_tupes(the_dict):
    the_list = []
    # here, k and v will parse each tuple of key,value pairs returned by .iteritems()
    for k, v in the_dict.iteritems():
        the_list.append((k,v))
    return the_list


'''

Assignment: Making Dictionaries
Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

Your first function will take in two lists containing some strings. Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
Copy
Here's some help starting your function.

def make_dict(list1, list2):
  new_dict = {}
  # your code here
  return new_dict
Copy
Hacker Challenge:
If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.


'''

def making_dictionaires(list1, list2):
    the_dict = {}
    for i in range(0, len(list1)):
        the_dict[list1[i]] = list2[i]
    return the_dict