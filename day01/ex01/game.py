# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/23 18:57:52 by dochoi            #+#    #+#              #
#    Updated: 2020/04/23 19:33:52 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import traceback

class GotCharacter(object):
    def __init__(self, first_name, is_alive=True):
        try:
            self.first_name = str(first_name)
            self.is_alive = is_alive
        except TypeError:
             print("The name must be a string")

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

