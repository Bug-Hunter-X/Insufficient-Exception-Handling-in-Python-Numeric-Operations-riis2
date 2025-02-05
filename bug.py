def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Unsupported operand type(s) for /'"

#The bug lies in the fact that it doesn't handle other potential exceptions that can occur when operating with numbers, like OverflowError.
print(function_with_uncommon_error(10,0))
print(function_with_uncommon_error(10,"hello"))
print(function_with_uncommon_error(float('inf'),10))
print(function_with_uncommon_error(10,float('inf')))