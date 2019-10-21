class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time , ingredients ,recipe_type, description="Unknown"):
        self.name = name
        try:
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
        except:
            exit("cooking_lvl and cooking_time must be integers")
        if isinstance(ingredients, list):
            self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "name :" + self.name + "\n"
        txt += "cooking level :" + str(self.cooking_lvl) + "\n"
        txt += "cooking time :" + str(self.cooking_time) + "\n"
        txt += "ingredient :" 
        for ingredient in self.ingredients:
            txt += ingredient + ' '
        txt += "\n"
        txt += "description :" + self.description + "\n"
        txt += "recipe_type :" + self.recipe_type
        return txt

    def get_recipe_type(self):
        return self.recipe_type
    
    def get_recipe_by_name(self):
        return self.name