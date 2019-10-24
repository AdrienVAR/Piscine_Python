import numpy as np
import matplotlib
import matplotlib.pyplot
import matplotlib.image

class ImageProcessor:
    def __init__(self):
        pass
    def load(self, path):
        img = matplotlib.image.imread(path)
        print("Loading image of dimension" + str(len(img)) + "x" + str(len(img[0]))) 
        #list est un tableau de tableaux. img = row or col, img[0] = 1 row or 1 col
        #img = np.array(img, dtype='f')
        #img = np.dtype('f')
        # Print the dtype 
        #print(img.dtype) 
        print(img)
        return img
    def display(self, RGB_mat):
        RGB_img = matplotlib.pyplot.imshow(RGB_mat)
        matplotlib.pyplot.show()
        #print(RGB_img)

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("../resources/42AI.png")
    imp.display(arr)
