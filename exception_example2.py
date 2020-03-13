'''
Write a function  that asks for an integer and prints the square of it.
Use a while loop with a try, except block to account for incorrect inputs.
Sample Output:
Enter the number whose square is needed: xyz
The value you entered doesn't look like an int, Try Again:
Enter the number whose square is needed: 5
Square of 5 is 25
'''
def ask_and_square():
      while True:
         try:
            n = int(input('Enter the number whose square is needed:'))
            square = n**2
            print('Square of %s is %s' %(n, square))
            break
         except ValueError:
            print("The value you entered doesn't look like an int, Try Again:")

ask_and_square()

