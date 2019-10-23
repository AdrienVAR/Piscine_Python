def ft_map(function_to_apply, list_of_inputs):
    res = []
    for item in list_of_inputs:
        res.append(function_to_apply(item))
    return res
#comment changer automatiquement le type tuple en float?

    
def fahrenheit(T):
        return ((float(9)/5)*T + 32)

def celsius(T):
        return (float(5)/9)*(T-32)

if __name__ == "__main__":
    temperatures = (36.5, 37, 37.5, 38, 39)
    #F = map(fahrenheit, temperatures)
    #C = map(celsius, F) 
    temperatures_in_Fahrenheit = list(ft_map(fahrenheit, temperatures))
    temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
    print(temperatures_in_Fahrenheit)
    print(temperatures_in_Celsius)


# usecase: The map() function applies a given function to each item of an 
# iterable (list, tuple etc.) and returns a list of the results.