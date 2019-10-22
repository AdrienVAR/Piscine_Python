from vector import Vector

if __name__ == "__main__":
    v1 = Vector([0.0, 1.0, 2.0, 3.0]) 
    print(str(v1))
    v2_1 = v1 + 1
    print(str(v2_1))
    v2_2 = v1 + v1
    print(str(v2_2))
    v3 = Vector(3)
    print(str(v3))
    v4 = Vector((10, 14))
    print(str(v4))
    v5 = v2_2 - v1
    print(str(v5))
    v6 = v2_2 * v1
    print(str(v6))
    v6_2 = v4 * 5
    print(str(v6_2))
    v7 = Vector((5, 9))
    print(str(v7))
    v8 = v7 / v4
    print (v8)
    v9 = v7 / 2
    print (v9)