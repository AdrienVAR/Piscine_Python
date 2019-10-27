import pandas as pd
import numpy as np

class FileLoader:
    def load(self, path):
        data = pd.read_table(path)
        dimension = data.shape
        print("Loading dataset of dimensions", dimension[0] , "x", dimension[1])
        return data
    def display(self, df, n):
        pd.options.display.max_rows = 9
        #pd.set_option('display.max_rows', 999)
        print(df)
        #df = pd.DataFrame(np.random.randn(7,2))
        #pd.set_option('max_rows', 5)
        #print(df)

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../data/random.csv")
    loader.display(data, 5)


    #dans tuple: 1ere val = row pour nb lignes, 2e val nb colonnes
 
    #read_table != read)csv!!!