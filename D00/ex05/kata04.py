t = ( 0, 4, 132.42222, 10000, 12345.67)

def format_string():
    print ("#day"+ "{:0>2d}".format(t[0]) + ", ex" + "{:0>2d}".format(t[1]) + " : " + "{:.2f}".format(t[2]), end = '')
    print (",", "{:.2e}".format(t[3]) + ", " + "{:.2e}".format(t[4]))

if __name__ == "__main__":
    format_string()

    #day_00, ex_04 : 132.42, 1.00e+04, 1.23e+04