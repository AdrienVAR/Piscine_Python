import sys

def reverse(string): 
    string = string[::-1] 
    return string

def swapcase(string):
    return string.swapcase()


if __name__ == "__main__":
    i = len(sys.argv) - 1
    string = ""
    while i > 0:
        string += (swapcase(reverse(sys.argv[i])) + " ")
        i -= 1
    print (string)