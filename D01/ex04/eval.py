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
            print (res)

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
    def enumerate_evaluate():
        pass

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    Evaluator.zip_evaluate(coefs, words)
