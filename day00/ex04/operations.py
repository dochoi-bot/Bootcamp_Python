import sys 

argc = len(sys.argv)
a = 0
b = 0
if argc > 3:
    print("InputError: too many arguments\n")
if argc != 3:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit(1)
try:
    a = (int)(sys.argv[1])
    b = (int)(sys.argv[2])
    print("Sum:         ", a + b)
    print("Differnce:   ", a - b)
    print("Product:     ", a * b)
    try:
        print("Quotient:    ", a / b)
    except ZeroDivisionError:
        print("Quotient:    ", "ERROR (div by zero)")
    try:
        print("Remainder:   ", a % b)
    except ZeroDivisionError:
        print("Reaminder:   ", "ERROR (modulo by zero)")
except ValueError:
    print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")

