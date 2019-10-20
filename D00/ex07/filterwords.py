import sys

def filter_string(string, max_size):
    filter_list = []
    filter_list = string.split()
    i = 0
    #for i in filter_list :
    while i < len(filter_list):
        len_word = len(filter_list[i])
        if len_word <= max_size :
            #filter_list.remove(i)
            filter_list.pop(i)
            i -= 1
        i += 1
    print (filter_list)


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print ("ERROR")
        sys.exit(0)
    if sys.argv[1].isnumeric() == True:
        print ("ERROR")
        sys.exit(0)
    if sys.argv[2].isnumeric() == False:
        print ("ERROR")
        sys.exit(0)
    if int(sys.argv[2]) == 0:
        print ("No words is zero charachters")
        sys.exit(0)
    filter_string((sys.argv[1]), int(sys.argv[2]))