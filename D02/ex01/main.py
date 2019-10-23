def what_are_the_vars(*args, **kwargs):
    res = ObjectC()
    for i, elem in enumerate(args):
        setattr(res, "var_" + str(i) , elem)
        #print (elem)
    for key, values in kwargs.items():
            if getattr(obj, key, False) != False: #in object, is there the key? if no name found, return False.
                return None                       #if a name is found (!= False), return None
            #print("Key =" + key)
            setattr(res, key, values)
        #print (key, values)
    #getattr(res, args)
    return res

class ObjectC(object):
    #attributs de res sur le 4e appel de what are the vars
    #var_0 = 12
    #var_1 = "yes"
    #var_2 = []
    #a = 10
    #hello = World

    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)

#The getattr() method returns:

#value of the named attribute of the given object
#default, if no named attribute is found
#AttributeError exception, if named attribute is not found and default is not defined