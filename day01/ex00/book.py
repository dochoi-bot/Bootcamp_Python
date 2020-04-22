import traceback
import time
class Book:
    """ this is book """
    allowed = ["starter", "lunch", "dessert"]
    def __init__(self, name):
        """ init function"""
        try :
            self.name = str(name)
            self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}
            self.creation_date = time.strftime('%c', time.localtime(time.time()))
            self.last_update = self.creation_date
        except TypeError :
            lines = traceback.format_exc().strip().split('\n')
            print(lines[2])
            print(lines[3])
        if len(name) == 0:
            print("The name cannot be blank.")
            raise ValueError

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for i in Book.allowed:
            for recipe in self.recipes_list[i]:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe
        print("can't found")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in Book.allowed:
            print("The recipe_type can be one of ", allowed)
            raise ValueError
        for i in self.recipes_list[recipe_type]:
            print(i.name)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = time.strftime('%c', time.localtime(time.time()))

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ("name : [" + self.name +"]\nrecipes_list : " + str(self.recipes_list) )
        return txt