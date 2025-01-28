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
    for i in range(n+1):
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
    std_list = []
    for key, value in students_dict.items():
        if value > 80:
            std_list.append(key)
    return std_list

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    com_elem = set()
    for num1 in list1:
        if num1 in list2:
            com_elem.add(num1)
    return com_elem

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    ops_dict = {}
    ops_dict['sum'] = a + b
    ops_dict['difference'] = a - b
    ops_dict['product'] = a * b
    if b != 0:
        ops_dict['quotient'] = a / b
    return ops_dict

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    log_dict = {}
    log_dict['and'] = x and y
    log_dict['or'] = x or y
    log_dict['not_or'] = not x 
    return log_dict

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    bit_ops = {}
    bit_ops['and'] = a & b
    bit_ops['or'] = a | b
    bit_ops['xor'] = a ^ b
    return bit_ops