# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/23 19:35:19 by dochoi            #+#    #+#              #
#    Updated: 2020/04/23 21:56:18 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector(object):
    def __init__(self, values):
        try :
            if isinstance(values, int):
                self.values = list(range(values))
            elif isinstance(values, list):
                self.values = list(values)
            elif isinstance(values,tuple) and len(values) == 2:
                self.values = list(range(values[0], values[1]))
            self.size = len(self.values)
            for i in range(self.size):
                self.values[i] = float(self.values[i])
        except TypeError:
             print("The values must be able to convert to a float")

    def __add__(self, values2):
        try :
            if isinstance(values2, (int, float)):

                return Vector(list(a + float(values2) for a in self.values)) # list comprehension
            elif not isinstance(values2, Vector):
                raise ValueError
            if self.size != values2.size:
                raise ValueError
            else:
                return Vector(list(a + b for a,b in zip(self.values, values2.values))) # list comprehension
        except TypeError:
            print("The values must be able to convert to a float")
        except ValueError:
            print("They are different sizes.")

    def __radd__(self, values2):
        return (self + values2)

    def __sub__(self, values2):
        try :
            if isinstance(values2, (int, float)):
                return Vector(list(a - float(values2) for a in self.values)) # list comprehension
            elif not isinstance(values2, Vector):
                raise ValueError
            if self.size != values2.size:
                raise ValueError
            else:
                return Vector(list(a - b for a,b in zip(self.values, values2.values))) # list comprehension
        except TypeError:
            print("The values must be able to convert to a float")
        except ValueError:
            print("They are different sizes.")

    def __rsub__(self, values2):
        try :
            if isinstance(values2, (int, float)):
                return Vector(list(float(values2) - a for a in self.values)) # list comprehension
            elif not isinstance(values2, Vector):
                raise ValueError
            if self.size != values2.size:
                raise ValueError
            else:
                return Vector(list(b - a for a,b in zip(self.values, values2.values))) # list comprehension
        except TypeError:
            print("The values must be able to convert to a float")
        except ValueError:
            print("They are different sizes.")

    def __truediv__(self, values2):
        try :
            if isinstance(values2, (int, float)):
                return Vector(list(a / float(values2)for a in self.values)) # list comprehension
            else:
                raise ValueError
        except ValueError:
            print("only scalar")

    def __rtruediv__(self, values2):
        try :
            raise ValueError
        except ValueError:
            print("only scalar")

    def __mul__(self, values2):
        try :
            if isinstance(values2, (int, float)):
                return Vector(list(a * float(values2) for a in self.values)) # list comprehension
            elif not isinstance(values2, Vector):
                raise ValueError
            if self.size != values2.size:
                raise ValueError
            else:
                temp = 0.0
                for a,b in zip(self.values, values2.values):
                    temp += a * b
                return temp
        except TypeError:
            print("The values must be able to convert to a float")
        except ValueError:
            print("They are different sizes.")

    def __rmul__(self, values2):
        return (self * values2)

    def __repr__(self):
        return '<{0}.{1} object at {2}>'.format(
            self.__module__, type(self).__name__, hex(id(self)))

    def __str__(self):
        return (str(self.values))