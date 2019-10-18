import sys

def is_even(i):
    if (i % 2 == 0):
        print ("I'm Even.")
    else:
        print ("I'm Odd.")

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print ("""Usage: python operations.py
Example:
    python operations.py 10 3""")
        sys.exit(0)
    if (len(sys.argv) > 3):
        print ("""InputError: too many arguments
Usage: python operations.py
Example:
    python operations.py 10 3""")
        sys.exit(0)
    if sys.argv[1].isnumeric() == False or sys.argv[2].isnumeric() == False:
        print ("""InputError: only integers
Usage: python operations.py
Example:
    python operations.py 10 3""")
        sys.exit(0)
    print("Sum:         ", sys.argv[1] + sys.argv[2])
    print("Difference:         ", int(sys.argv[1]) - int(sys.argv[2]))
    print("Product:         ", int(sys.argv[1]) * int(sys.argv[2]))
    if int(sys.argv[1]) == 0 or int(sys.argv[2]) == 0:
        print("ERROR (div by zero)")
    else :
        print("Quotient:         ", int(sys.argv[1]) / int(sys.argv[2]))
    if int(sys.argv[1]) == 0 or int(sys.argv[2]) == 0:
        print("ERROR (modulo by zero)")
    else :
        print("Remainder:         ", int(sys.argv[1]) % int(sys.argv[2]))
