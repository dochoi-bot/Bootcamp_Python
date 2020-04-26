# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/26 19:49:59 by dochoi            #+#    #+#              #
#    Updated: 2020/04/26 20:53:35 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# import matplotlib.pyplot as plt
import numpy as np

class ScrapBooker(object):
    def crop(self, array, dimensions, position= (0, 0)):
        if dimensions[0] + position[0] > array.shape[0] or dimensions[1] + position[1] > array.shape[1]:
            print("Error")
            return None
        return array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]]
    def thin(self, array, n ,axis):
        return np.delete(array, slice(0, array.shape[axis], n), axis)
    def juxtapose(self ,array, n, axis):
        # return np.concatenate([array] * n, axis) if 1D error else good
        if axis == 0:
            return np.vstack([array] * n)
        elif axis == 1:
            return np.hstack([array] * n)
        else :
            print("Error")
            return None
    def mosaic(self, array, dimensions):
        return np.concatenate([np.concatenate([array] * dimensions[0], 0)] * dimensions[1], 1)

# te = ScrapBooker()
# arr = plt.imread("../resources/42AI.png")
# ar2 = te.mosaic(arr, (3, 2))
# plt.imshow(ar2)
# plt.show()
# plt.imshow(arr)
# plt.show()