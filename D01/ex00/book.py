from datetime import date

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = date.today()
        self.creation_date = date.today()
        self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for recipe in self.recipes_list[recipe_type]:
            print(recipe)
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.get_recipe_type()].append(recipe)
        self.last_update = date.today()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for recipe_name in self.recipes_list:
            for recipe in self.recipes_list[recipe_name]:
                if recipe.get_recipe_by_name() == name:
                    print(name)
                    return recipe
    #for each list, for each value of the list, if value = name