# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 01:26:45 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 03:23:38 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

nested_dict = { 'sandwich': {'ingredients': ['ham', 'bread', 'cheese'],
                            'meal': 'lunch',
                            'prep_time': 10},
                'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                         'meal': 'dessert',
                         'prep_time': 60},
                'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                          'meal': 'lunch',
                          'prep_time': 15}}
                
def print_menu():
    print("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")

def add_recipe():
    ing_list = []
    print("\nPlease enter your recipe name")
    name = input()
    print("\nPlease enter ingredients")
    ing = input()
    ing_list.append(ing)
    while True:
        print("\nPlease select an option by typing the corresponding number:\n1: add a ingredient\n2: Quit")
        ing = input()
        if (ing != '1' and ing != '2'):
            print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 2.")
        elif ing == '1':
            print("Please enter ingredients")
            ing = input()
            ing_list.append(ing)
        else :
            break
    print("\nPlease enter type of meal")
    meal = input()
    print("\nPlease enter preparation time in minutes")
    time = input()
    nested_dict[name] = {'ingredients': ing_list, 'meal': meal, 'prep_time': time}
    print("add complete\n")
    print_menu()

def del_recipe():
    print("\nPlease enter your recipe name")
    name = input()
    if name in nested_dict:
        del nested_dict[name]
        print("delete complete\n")
    else:
        print("not found\n")
    print_menu()

def show_recipe():
    print("\nPlease enter your recipe name")
    name = input()
    if name in nested_dict:
        print("\nRecipe for", name + "\nIngredients list:", nested_dict[name]['ingredients'], "\nTo be eatne for", nested_dict[name]['meal'] + ".\nTake", nested_dict[name]['prep_time'], "minutes of cooking.\n")
    else:
        print("not found\n")
    print_menu()

def show_cookbook():
    idx = 1

    print("\n---Show your cookbook---\n")
    for name in nested_dict.keys():
        print("[",idx,"]  ",name)
        idx += 1
    print("")
    print_menu()

if __name__ == "__main__":
    print_menu()
    while True:
        s = input()
        if (len(s) != 1 or '1' > s or '5' < s):
            print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.")
        if s == '5':
            print("\nCoolbook closed.")
            break
        if s == '1':
            add_recipe()
        if s == '2':
            del_recipe()
        if s == '3':
            show_recipe()
        if s == '4':
            show_cookbook()


