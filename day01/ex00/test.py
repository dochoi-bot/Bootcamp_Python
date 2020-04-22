from book import Book
from recipe import Recipe
from loading import ft_progress

if __name__ == "__main__":

    book = Book("bread")
    print(str(book))
    print(book.creation_date)

    tourte1 = Recipe("bread", 1, 5, ["milk" , "egg"], "starter")
    tourte2 = Recipe("bread2", 1, 5, ["milk" , "egg"], "lunch")
    tourte3 = Recipe("bread3", 1, 5, ["milk" , "egg"], "dessert")
    for i in ft_progress(range(0, 31111)):
        pass
    print()
    book.add_recipe(tourte1)
    book.add_recipe(tourte3)
    book.add_recipe(tourte2)
    # book.add_recipe(1)
    print(book.last_update)
    book.get_recipes_by_types("lunch")
    book.get_recipes_by_types("starter")
    book.get_recipe_by_name("bread")