import pandas as pd
import numpy as np

class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        dimension = data.shape
        print("Loading dataset of dimensions", dimension[0] , "x", dimension[1])
        return data



 