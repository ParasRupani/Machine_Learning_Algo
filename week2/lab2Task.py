# TODO: write your name and ID below
# You need to make sure that whatever the price and tax is,
# Your code will never break (throw an error)!

# Name: Paras Rupani
# ID: 8961758

def total_price(price, tax):
    # 3 marks
    # TODO: write the functionality of the code where
    #  you are taking as an input a price of an item and the
    #  tax in decimal (13% tax will be given as 0.13),
    #  you should return the taxedPrice of that item
    #  which will be the total price after tax a customer must pay
    if isinstance(price, (float, int)) and isinstance(tax, (float, int)):
        taxedPrice = price + (price*tax)
        return taxedPrice
    else:
        return "error"


def divisible_by(x, y):
    # 3 marks
    # TODO: write a function that returns True if x is divisible by y,
    #  and returns False OTHERWISE.
    if x%y == 0:
        return True
    else:
        return False


def basic_calculator(x, y, operator):
    # 6 marks
    # TODO: write the functionality of the code where you are
    #  coding a basic calculator that performs basic addition "+", subtraction "-",
    #  multiplication "*", division "/", modulus "%" and integer division "//"
    #  the function must apply the operator to x and y for example:
    #  basicCalculator(10, 15, "*") should apply 10*15 and save it to the result variable
    #  NOTE: YOU NEED TO HANDLE DIVISION ERRORS BY RETURNING A STRING WITH THE WORD "error"
    #  NOTE: YOU NEED TO HANDLE AN INVALID OPERATOR BY RETURNING A STRING HAVING THE WORD "invalid"

    if isinstance(x, str) or isinstance(y, str):
        return "error"
    
    if operator not in ['+', '-', '*', '/', '//', '%']:
        return "invalid"
    
    if operator == '/' and y==0:
        return 'error'
    
    if operator == '//' and y==0:
        return 'error'
    
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y
    elif operator == '*':
        return x*y
    elif operator == '/':
        return x/y
    elif operator == '//':
        return x//y



def sum_of_even(numbersList):
    # 3 marks
    # TODO: write the functionality of the code where you are
    # taking as an input a list of numbers
    # returning the sum of even numbers in the list
    # NOTE: YOU NEED TO HANDLE ERRORS OF GIVING LIST OF STRINGS OR/and
    #  STRINGS WITH NUMBERS by returning "invalid"
    # sum_of_even([1,2,3,4,5,6]) = 12

    if not isinstance(numbersList, list):
        return "invalid" 

    # initiate sum to 0
    sum = 0
    for i in numbersList:
        if not isinstance(i, int):
            return "invalid"
        else:
            if i%2 == 0:
                sum += i
    return sum
    


def reverse_string(inputString):
    # 3 marks
    # TODO: write the functionality of the code where you are
    # taking as an input a string
    # returns the reverse of the string
    # reverse_string("hello") = "olleh"
    # NOTE: Numbers should be handled as strings ex: 123 returns "321"
    
    # convert input into string, to consider numbers
    inputString = str(inputString)
    return inputString[::-1]


def diamond_string(length):
    # 5 marks
    # TODO: write the functionality of the code where you are
    # taking as an input a POSITIVE ODD length
    # saves in a string the diamond as follows:
    # diamond_string(5)
    #   *
    #  ***
    # *****
    #  ***
    #   *
    # NOTE: The input must be positive odd, if not return empty string "" 

    if length % 2 == 0 or length < 0:
        return ""
    
    diamond = ''

    #Upper half
    for i in range(1, length + 1, 2):
        spaces = " " * ((length - i) // 2)
        diamond += f"{spaces}{'*' * i}\n"

    #Lower Half
    for i in range(length - 2, 0, -2):
        spaces = " " * ((length - i) // 2)
        diamond += f"{spaces}{'*' * i}\n"

    diamond = diamond.rstrip('\n')

    return diamond


def longest_consecutive_subarray(numberArray):
    # 5 marks
    # TODO: write the functionality of the code where you are
    # taking as an input an array of REAL NUMBERS
    # return the length of the longest subarray that could be
    # built using the input
    # longest_consecutive_subarray([100, 4, 200, 1, 3, 2]) = 4
    # Function should return 4 which represents in this case
    # the longest_consecutive_subarray that could be built [1,2,3,4]
    # You can't use Built in Sorting!
    # Note: - If any error exists in the input, "error" should be returned
    #       - The difference between any 2 consecuetive numbers is 1.

    # If array is not a list, return error
    if not isinstance(numberArray, list):
        return "error"
    
    longest = 0

    for i in numberArray:
        # If any number is not int, return error
        if not isinstance(i, int):
            return "error"
        
        cur_len = 1
        cur_num = i

        # When next number is in the array, increase the length
        while cur_num + 1 in numberArray:
            cur_num += 1
            cur_len += 1

        # set the longest number between the current longest, length found
        longest = max(longest, cur_len)

    return longest
