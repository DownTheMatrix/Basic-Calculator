import time                           # This library is required for using the time.sleep() method.

def welcome_alert():
    print('''
Welcome to Basic Calculator 2017!
''')

def calc():                     # As I didn't use the Math library here, I couldn't find a way to implement the square root operation.
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')

    number1 = int(input('Please enter your first number: '))
    number2 = int(input('Please enter your second number: '))

    if operation == '+':
        print('{} + {} = '.format(number1, number2))
        print(number1 + number2)

    elif operation == '-':
        print('{} - {} = '.format(number1, number2))
        print(number1 - number2)

    elif operation == '*':
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)

    elif operation == '/':
        print('{} / {} = '.format(number1, number2))
        print(number1 / number2)

    elif operation == '**':
        print('{} ** {} = '.format(number1, number2))
        print(number1 ** number2)

    elif operation == '%':
        print('{} % {} = '.format(number1, number2))
        print(number1 % number2)

    else:
        print('You have not typed a valid operator, please run the program again.')

def again():
    print("Do you want to perform another calculation? Y/N")
    more = input("")
    if more.lower() == "y":                                    
        time.sleep(0.5)
        calc()
    elif more.lower() == "n":
        print("Thank you for using Basic Calculator 2017!")
        time.sleep(1)
        exit()
    else:
        print("Please enter Y for yes or N for no.")
        time.sleep(1)
        again()

welcome_alert()
calc()
x = 0               # This allows the user to perform more calculations in a row.
while True:
    again()
