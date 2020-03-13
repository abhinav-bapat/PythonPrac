# divisor example
try:
    x = int(input('Enter numerator:'))
    y = int(input('Enter denominator:'))
    result = x/y
    print(result)
except ZeroDivisionError:
    print('Denominator cannot be zero')
except ValueError:
    print('Only numbers are allowed')