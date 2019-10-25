import pandas as pd
import numpy as np

class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print("Loading dataset of dimensions")# + data.shape(0))
        return data



 