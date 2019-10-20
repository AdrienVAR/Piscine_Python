cookbook = {
    'sandwich' : 
    {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal' : 'lunch', 'prep_time' : 10},
    'cake' :
    {'ingredients': ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : 60},
    'salad' :
    {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' : 'lunch', 'prep_time' : 15}
}

def print_recipe(name_of_the_recipe):
    print   (cookbook[name_of_the_recipe])

def delete_recipe(name_of_the_recipe):
    if name_of_the_recipe in cookbook:
        del   (cookbook[name_of_the_recipe])

def add_recipe(name_of_the_recipe, ingredients, meal, prep_time):
    cookbook[name_of_the_recipe] = ingredients,  meal, prep_time


if __name__ == "__main__":
    print("1.")
    print   (cookbook.keys())
    print   (cookbook.values())
    print   (cookbook)

    print("2.")
    print_recipe('cake')

    print("3.")
    delete_recipe('cake')
    print   (cookbook)

    print("4.")
    add_recipe('tiramisu', ['sugar', 'milk', 'chocolate'], 'dessert', 45)
    print   (cookbook) # pb here

    print("5.")
    print   (cookbook.keys())
