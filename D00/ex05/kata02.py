t = (3,30,2019,9,25)

def format_string():
    print (str(t[3]) + "/" + str(t[4]) + "/" + str(t[2]) + " " + "{:0>2d}".format(t[0]) + ":" + "{:0>2d}".format(t[1]))

if __name__ == "__main__":
    format_string()

#09/25/2019 03:30

#It's str.format function.

#In the format string "{:0>2d}":

#d means expecting an int:

#>>> "{:d}".format(3)
#'3'
#2d means formats to 2 characters using padding (whitespace by default)

#>>> "{:2d}".format(3)
#' 3'
#0> means using 0 as padding, and right adjust the result:

#>>> "{:0>2d}".format(3)
#'03'