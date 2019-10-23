#import functools
from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
    res = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for i in range (len(list_of_inputs)):
        if i > 1:
            res = function_to_apply(res, list_of_inputs[i])
    return res

if __name__ == "__main__":
    print(reduce(lambda x,y: x+y, [47,11,42,13]))
    print(ft_reduce(lambda x,y: x+y, [47,11,42,13]))

#The function reduce(func, seq) continually applies the function func() to the sequence seq.
#It returns a single value. 

#If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
#At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
#In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
#The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
#Continue like this until just one element is left and return this element as the result of reduce()