# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 17:30:24 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 17:48:50 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def what_are_the_vars(*args, **kwargs):
    """Your code"""
    obj = ObjectC()
    count = 0
    for elem in args:
        setattr(obj, "var_" + str(count), elem)
        count += 1
    for elem in kwargs:
        if not hasattr(obj, elem):
            setattr(obj, elem, kwargs[elem])
        else :
            return None
    return obj

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)