class Evaluator: 
    def __init__(self):
        pass

    #def zip_evaluate(coefs, words):
    #    res = 0
    #    if type (coefs) is list and type (words) is list:
    #        if len(coefs) != len(words):
    #            return -1
    #        for i in range(len(coefs)):
    #            res += coefs[i] * len(words[i])
    #        print (res)
    
    @staticmethod
    def zip_evaluate(coefs, words):
        res = 0
        if type (coefs) is list and type (words) is list:
            if len(coefs) != len(words):
                return -1
            tmp = list(zip(words))
            for i in range(len(coefs)):
                res += coefs[i] * len(tmp[i][0])
            return res

# The zip function in Python 3 returns an iterator. Iterators can only be exhausted (by something like making a list out of them) once.
# The purpose of this is to save memory by only generating the elements of the iterator as you need them, rather than putting it all into memory at once.
# Generator

    #def zip_and_multiply(coefs, words):
    #    res = 0
    #    for a, b in zip(coefs, words):
    #        res = a * b
    #    return res

    #def zip_evaluate(coefs, words):
    #    res = 0
    #    if type (coefs) is list and type (words) is list:
    #        if len(coefs) != len(words):
    #            return -1
    #    res = zip_and_multiply(coefs, words)
    #    print(res)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        res = 0
        if type (coefs) is list and type (words) is list:
            if len(coefs) != len(words):
                return -1
            for i, value in enumerate(words):
                res += len(value) * coefs[i]
            return res

        #should use yield:
        #https://docs.python.org/fr/3/library/functions.html#enumerate

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))

    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print (Evaluator.enumerate_evaluate(coefs,words))