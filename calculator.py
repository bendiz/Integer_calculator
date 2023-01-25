# Task: CREATE INTEGER CALCULATOR

# 1. Have a function magic_function(num1: int, num2: int, op: str)
#     2. Checks which op is incl in str and access value matching our func name
#        in dict to run correct function.

# 2. Define a function for each operator that your calculator provides.
#   1. All these functions will recieve two parameters: num1, num2.
#   2. All these functions return sum in the end.
#   3. Make sum variable, so input doesn't change, and avoid repeated code.
#   4. Create docstring following PEP-257 conventions

#     User input:
#         - Trim whitespace
#         - Require 3 int numbers and 2 string operators
#         - "Error" on operator which is not included in calculator
#         - "Error" on float

#     Functions:
#          Addition (activates on key "+" inside magic_function)
#             return num1 + num2

#         Subtraction (activates on key "-" inside magic_function)
#             return num1 - num2

#         Division (activates on key "//" inside magic_function)
#             return num1 // num2 (because we want an int as output).

#         Modulo (activates on key "%" inside magic_function)
#             return num1 % num2

#         Multiplication (activates on key "*" inside magic_function)
#             return num1 * num2

#         Exponentiation (activates on key "**" inside magic_function)
#             return num1 ** num2

# 3. Num3 and op2 input goes in magic_function with int from first calculation.
#     1. magic_function(num1, num2, op1) return int to be used in calculation2.
#     2. magic_function(num1, num2) runs again with return of
#     magic_function as num1 and num3 input as num2.

# 4. End with a string that displays the entire calculation.

# <---------- END OF DESIGN STEPS ---------->

# <---------- START OF PROGRAM ---------->


# Functions
def add(num1: int, num2: int) -> int:
    """
    Adds num1 and num2 together and returns the integer sum.

    Args:
        num1 (int): First operand
        num2 (int): Second operand

    Returns:
        int: The sum of num1 added together with num2.
    """
    return num1 + num2


def sub(num1: int, num2: int) -> int:
    """
    Subtracts num2 from num1 and returns the int sum.

    Args:
        num1 (int): First operand
        num2 (int): Second operand

    Returns:
        int: The sum of num1 subtracted by num2.
    """
    return num1 - num2


def int_div(num1: int, num2: int) -> int:
    """
    Integer division of num1 and num2, returns the integer sum.

    Args:
        num1 (int): First operand
        num2 (int): Second operand

    Returns:
        int: The sum of num1 integer divided by num2
    """
    return num1 // num2


def modulo(num1: int, num2: int) -> int:
    """
    Finds the remainder when num1 is divided by num2 and returns the int sum.

    Args:
        num1 (int): First operand
        num2 (int): Second operand

    Returns:
        int: The sum of the remainder after num1 is integer divided by num2.
    """
    return num1 % num2


def mult(num1: int, num2: int) -> int:
    """
    Multiplies num1 by num2 and returns the integer sum.

    Args:
        num1 (int): First operand
        num2 (int): Second operand

    Returns:
        int: The sum of the multiplication of num1 and num2.
    """
    return num1 * num2


def exponentiation(num1: int, num2: int) -> int:
    """
    Exponentiates num1 by num2 and returns the integer sum.

    Args:
        num1 (int): First operand
        num2 (int): Second operand

    Returns:
        int: The sum the exponentiation of num1 by num2.
    """
    return num1**num2


def magic_function(num1: int, num2: int, op: str) -> int:
    """
    Calls the function that implements the operation op and returns the result
    Assumes that functions add, sub, int_div, modulo exist, receive 2 integer
    params and return an integer.

    Args:
        num1 (int): First operand
        num2 (int): Second operand
        op (str): Operator

    Returns:
        int: The result of the operation
    """
    options = {
        "+": add,
        "-": sub,
        "//": int_div,
        "%": modulo,
        "*": mult,
        "**": exponentiation,
    }
    return options[op](num1, num2)


def calculation(num1: int, num2: int, num3: int, op1: str, op2: str) -> str:
    """
    Calculates the first math expression by calling the magic_function,
    then it calculates the result of our first math expression with
    the last number and finally returns a string with our full calculation.

    Args:
        num1 (int): First operand
        num2 (int): Second operand
        num3 (int): Third operand
        op1 (str): Operator
        op2 (str): Operator

    Returns:
        str: The full result of the calculation in a formatted string.
    """
    first_calculation = magic_function(num1, num2, op1)
    combined_calculation = magic_function(first_calculation, num3, op2)
    calc_msg = f"(({num1} {op1} {num2}) {op2} {num3}) = {combined_calculation}"
    return calc_msg


# Error checking and correcting user input
def calculator_on() -> tuple:
    """
    Runs our calculator by asking the user for 5 inputs and error checks them.
    Prints a string in the console forcing the user to re-enter details
    if the input is not valid. When all inputs are valid, the function
    returns a tuple with the user inputs num1, num2, num3, op1, op2.
    Turns our num1-3 inputs from str to int.

    Returns:
        tuple: Error-checked, stripped user inputs: num1, num2, num3, op1, op2.
    """
    VALID_OPERATOR = ["+", "-", "//", "%", "*", "**"]
    msg = "Please input "
    while True:
        try:
            # Checks if num are of type int and that the operand match valid op
            num1 = int(input(f"{msg}first integer: "))
            op1 = input(f"{msg}first operator {VALID_OPERATOR}:").strip()
            num2 = int(input(f"{msg}second integer: "))
            op2 = input(f"{msg}second operator {VALID_OPERATOR}:").strip()
            if op1 not in VALID_OPERATOR or op2 not in VALID_OPERATOR:
                raise ValueError
            num3 = int(input(f"{msg}third integer: "))
            break
        except ValueError:
            # To prevent KeyError in our magic_function.
            print(f"Wrong input type! Int and {VALID_OPERATOR} only...")
    return num1, num2, num3, op1, op2


# Makes function only run when file is run directly and not imported
if __name__ == "__main__":
    num1, num2, num3, op1, op2 = calculator_on()
    result = calculation(num1, num2, num3, op1, op2)
    print(result)
