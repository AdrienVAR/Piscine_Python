from contextlib import contextmanager
class CsvReader():
    def __init__(self, sep=',', headers=False, skip_top=0, skip_bottom=0):
        pass
    def __enter__(self):
        pass
    def __exit__(self):
        pass

# Using these magic methods (__enter__, __exit__) allows you to implement objects which can be used easily
# with the with statement.
# The idea is that it makes it easy to build code which needs some 'cleandown' 
# code executed (think of it as a try-finally block).

    def getdata():
        pass
    def getheader():
        pass
    def Loadjson():
        pass

#from csvreader import CsvReader  
if __name__ == "__main__":
    with Loadjson('good.csv') as file:
        data = file.getdata()
        headers = file.getheader()

# https://docs.python.org/3/library/contextlib.html