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

    def __add__(self, other):
        if type(other) is Vector:
            val = other.values
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] + val[i])
            return Vector(res)
        elif type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] + other)
            return Vector(res)            

    def __radd__(self, other):
        if type(other) is Vector:
            val = other.values
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] + val[i])
            return Vector(res)
        elif type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] + other)
            return Vector(res) 
    # add : scalars and vectors, can have errors with vectors.

    def __sub__(self, other):
        if type(other) is Vector:
            val = other.values
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] - val[i])
            return Vector(res)
        elif type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] - other)
            return Vector(res)

    def __rsub__(self, other):
        if type(other) is Vector:
            val = other.values
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] - val[i])
            return Vector(res)
        elif type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] - other)
            return Vector(res)
    # sub : scalars and vectors, can have errors with vectors.

    def __truediv__(self, other):
        if type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] / other)
            return Vector(res)

    def __rtruediv__(self, other):
        if type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] / other)
            return Vector(res)

    # div : only scalars.

    def __mul__(self, other):
        if type(other) is Vector:
            val = other.values
            res = 0
            for i in range (self.lenght):
                res += self.values[i] * val[i]
            return res
        elif type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] * other)
            return Vector(res)

   
    def __rmul__(self, other):
        if type(other) is Vector:
            val = other.values
            res = 0
            for i in range (self.lenght):
                res += self.values[i] * val[i]
            return res
        elif type(other) is int:
            res = []
            for i in range (self.lenght):
                res.append(self.values[i] * other)
            return Vector(res)
    # mul : scalars and vectors, can have errors with vectors,
    # return a scalar is we perform Vector * Vector (dot product)

    def __str__(self):
        txt = ""
        txt += "Values: " + str(self.values)
        return txt

    def __repr__(self):
        txt = ""
        txt += "Values: " + str(self.values) + "\n"
        return txt
