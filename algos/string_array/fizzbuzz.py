# Fizz Buzz
# if value is divisible by 3, print fizz
# if value is divisible by 5, print buzz
# if value is divisible by both 3 and 5, print fizzbuzz

for num in range(101):
    if num % 3 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
