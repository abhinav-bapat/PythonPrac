"""
Write a program that prints the integers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five
print "FizzBuzz".
For the rest, print the actual number
"""
for x in range(101):
    if x%3==0 and x%5==0:
        print('FizzBuzz')
    elif x%3==0:
        print('Fizz')
    elif x%5==0:
        print('Buzz')
    else:
        print(x)



