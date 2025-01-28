def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f'My name is {name} and I am {age} years old'

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return 'Greater'
    elif number < 10:
        return 'Lesser'
    elif number == 10:
        return 'Equal'

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for i in range(n):
        sum += i
    return sum


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum = 0
    max = numbers[0]
    min = numbers[0]
    for i in numbers:
        sum += i
        if i > max:
            max = i
        if i < min:
            min = i
    return (sum, max, min)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    stdList = []
    for key, value in students_dict:
        if value > 80:
            stdList.append(key)
    return stdList

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    comElem = set()
    for num1 in list1:
        if num1 in list2:
            comElem.add(num1)
    return comElem

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    opsDict = {}
    opsDict['sum'] = a + b
    opsDict['difference'] = a - b
    opsDict['product'] = a * b
    if b != 0:
        opsDict['quotient'] = a / b
    return opsDict

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    logDict = {}
    logDict['and'] = x and y
    logDict['or'] = x or y
    logDict['xor'] = x ^ y
    return logDict

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    bitOps = {}
    bitOps['and'] = a & b
    bitOps['or'] = a | b
    bitOps['xor'] = a ^ b
    return bitOps