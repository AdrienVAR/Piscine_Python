

class CsvReader():
    def __init__(self, sep=',', headers=False, skip_top=0, skip_bottom=0):
        pass
    def __enter__(self):
        pass
    def __exit__(self):
        pass

#from csvreader import CsvReader  
if __name__ == "__main__":
    with Loadjson('good.csv') as file:
        data = file.getdata()
        headers = file.getheader()