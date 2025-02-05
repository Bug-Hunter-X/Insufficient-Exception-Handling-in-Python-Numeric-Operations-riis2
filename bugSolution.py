def function_with_uncommon_error_solution(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Unsupported operand type(s) for /'"
    except OverflowError:
        return "Overflow occurred during calculation"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

#The improved function now handles OverflowError and any other unexpected exceptions.
print(function_with_uncommon_error_solution(10,0))
print(function_with_uncommon_error_solution(10,"hello"))
print(function_with_uncommon_error_solution(float('inf'),10))
print(function_with_uncommon_error_solution(10,float('inf')))