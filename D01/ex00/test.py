from book import Book
from recipe import Recipe

cookbook = {
    "sandwich" : {
        "type" : "lunch",
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "prep_time" : 10
    },
    "cake" : {
        "type" : "dessert",
        "ingredients" : ["flour", "sugar", "eggs"],
        "prep_time" : 60
    },
    "salad" : {
        "type" : "lunch",
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "prep_time" : 15
    }
}

my_cookbook = Book("my_cookbook")

for key, value in cookbook.items():
   tmp = Recipe(key, 2, value["prep_time"], value["ingredients"], value["type"], "tres bon")
   my_cookbook.add_recipe(tmp)
   #print(str(tmp))

my_cookbook.get_recipes_by_types("dessert")
my_cookbook.get_recipes_by_types("starter")
my_cookbook.get_recipes_by_types("lunch")

my_cookbook.get_recipe_by_name("salad")