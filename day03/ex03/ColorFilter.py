# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/26 20:54:08 by dochoi            #+#    #+#              #
#    Updated: 2020/04/26 21:55:20 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import numpy as np

class ColorFilter(object):
    def invert(self, array):
        return 1.0 - array
    def to_blue(self, array):
        array_copy = np.zeros(array.shape)
        array_copy[:, :, 2] = array[:, :, 2]
        return array_copy
        # return np.zeros((array.shape[0],array.shape[1], array.shape[2]))
    def to_green(self, array):
        array_copy = array * 1.0
        array_copy
    def to_red(self ,array):
        pass
    def celluloid(self, array):
        pass
    def to_grayscale(self, array, fileter):
        pass
te = ColorFilter()
arr = plt.imread("../resources/42AI.png")
ar2 = te.to_blue(arr)
plt.imshow(ar2)
plt.show()
plt.imshow(arr)
plt.show()