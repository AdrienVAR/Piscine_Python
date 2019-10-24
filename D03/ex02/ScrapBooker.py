import numpy as np
import matplotlib.pyplot as plt

class ScrapBooker:
    def crop(self, array, dimensions, position = (0, 0)):
        return array[position[0]:position[0]+dimensions[0]:1, position[1]:position[1]+dimensions[1]:1]
        #a[start:stop:step] -> start through not past stop, by step
    def thin(self, array, n, axis):
        to_delete = [] # on peut envoyer une liste de choses à supprimer dans delete
        if axis == 0:
            for i in range(len(array)): # i ne peut pas itérer sur un int, avec range il itère sur une liste d'int
                if (i % n == 0 and i > 0):
                    to_delete.append(i - 1)
                i += n
            #while n < len(array):
            print(to_delete)
            array = np.delete(array, to_delete, axis)
        elif axis == 1:
            for i in range(len(array[0])):
                if (i % n == 0 and i > 0):
                    to_delete.append(i - 1)
                i += n
            #while n < len(array):
            print(to_delete)
            array = np.delete(array, to_delete, axis)
        return array


if __name__ == "__main__" :
    scr = ScrapBooker()
    array = ([[88, 93, 42, 25, 36, 14, 59, 46, 77, 13, 52, 58],
            [43, 47, 40, 48, 23, 74, 12, 33, 58, 93, 87, 87],
            [54, 75, 79, 21, 15, 44, 51, 68, 28, 94, 78, 48],
            [57, 46, 14, 98, 43, 76, 86, 56, 86, 88, 96, 49],
            [52, 83, 13, 18, 40, 33, 11, 87, 38, 74, 23, 88],
            [81, 28, 86, 89, 16, 28, 66, 67, 80, 23, 95, 98],
            [46, 30, 18, 31, 73, 15, 90, 77, 71, 57, 61, 78],
            [33, 58, 20, 11, 80, 25, 96, 80, 27, 40, 66, 92],
            [13, 59, 77, 53, 91, 16, 47, 79, 33, 78, 25, 66],
            [22, 80, 40, 24, 17, 85, 20, 70, 81, 68, 50, 80]])
    #print (scr.from_list(array))
    #print (array)
    array = np.array(array)
    array = scr.crop(array, (6, 7), (1,1))
    print (array)
    array = scr.thin(array, 3, 1)
    print (array)


#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array

    #array2 =    ([[ABCDEFGHIJQL],
    #            [ABCDEFGHIJQL],
    #            [ABCDEFGHIJQL],
    #            [ABCDEFGHIJQL],
    #            [ABCDEFGHIJQL]])