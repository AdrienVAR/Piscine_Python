class Vector:
    """I create vectors"""
    def __init__(self, param):
        if type(param) is list:
            self.values = []
            for i in param :
                if isinstance(i, float):
                    self.values.append(i)

        elif type(param) is int:
            self.values = []
            for i in range (param):
                self.values.append(float(i))

        elif type(param) is tuple:
            self.values = []
            for i in range (param[0], param[1]):
                self.values.append(float(i))
        self.lenght = len(self.values)
    #def print_values(self):
    #    print(self.values)

    def __add__(self, other):
        val = other.values
        res = []
        for i in range (self.lenght):
            res.append(self.values[i] + val[i])

    #__radd__
    # add : scalars and vectors, can have errors with vectors.
    #__sub__
    #__rsub__
    # sub : scalars and vectors, can have errors with vectors.
    #__div__
    #__rdiv__
    # div : only scalars.
    #__mul__
    #__rmul__
    # mul : scalars and vectors, can have errors with vectors,
    # return a scalar is we perform Vector * Vector (dot product)
    #__repr__

    def __str__(self):
        txt = ""
        txt += "Values: " + str(self.values) + "\n"
        txt += "Lenght: " + str(self.lenght) 
        return txt


if __name__ == "__main__":
    v1 = Vector([0.0, 1.0, 2.0, 3.0]) 
    print(str(v1))
    v2 = v1 + 5
    print(str(v2))
    v3 = Vector(3)
    print(str(v3))
    v4 = Vector((10, 15))
    print(str(v4))