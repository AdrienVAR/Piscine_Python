def ft_filter(function_to_apply, list_of_inputs):
    res = []
    for i in list_of_inputs:
        if function_to_apply(i) is True:
            res.append(i)
    return res

if __name__ == "__main__":
    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print(less_than_zero)
    less_than_zerotest = list(ft_filter(lambda x: x < 0, number_list))
    print(less_than_zerotest)