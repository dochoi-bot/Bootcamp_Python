# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/26 01:48:33 by dochoi            #+#    #+#              #
#    Updated: 2020/04/26 03:02:46 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class NumPyCreator(object):

    def from_list(self, lst, type=None):
        return np.array(lst, type)

    def from_tuple(self, tp, type=None):
        return np.array(tp, type)

    def from_iterable(self, it, type=None):
        return np.array(list(elem for elem in it), type)

    def from_shape(self, shape, value=0, type=None):
        return np.full(shape, value, type)

    def random(self, shape, type=None):
        return np.random.rand(*shape)

    def identity(self, n, type=None):
        return np.identity(n, type)
if __name__ == "__main__":

    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    shape=(3,5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))