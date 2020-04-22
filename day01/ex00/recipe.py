import traceback

class Recipe:
    """ this is Recipe """
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type,  description=""):
        """ init function"""
        allowed = ["starter", "lunch", "dessert"]
        try :
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)
        except TypeError :
            lines = traceback.format_exc().strip().split('\n')
            print(lines[2])
            print(lines[3])
        if len(name) == 0:
            print("The name cannot be blank.")
            raise ValueError
        if recipe_type not in allowed:
            print("The recipe_type can be one of ", allowed)
            raise ValueError
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ("name : [" + self.name +"]\ndescription : [" + self.description + "]" )
        return txt

if __name__ == "__main__":

    tourte = Recipe("bread", 1, 5, ["milk" , "egg"], "lunch")
    print(str(tourte))
    print(tourte.name)