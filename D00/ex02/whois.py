import sys

def is_even(i):
    if (i % 2 == 0):
        print ("I'm Even.")
    else:
        print ("I'm Odd.")

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        sys.exit(0)
    if (len(sys.argv) > 2):
        print ("ERROR")
        sys.exit(0)
    if sys.argv[1].isnumeric() == False:
        print ("ERROR")
        sys.exit(0)
    if int(sys.argv[1]) == 0:
        print ("I'm Zero.")
        sys.exit(0)
    is_even(int(sys.argv[1]))