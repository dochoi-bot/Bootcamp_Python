# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/26 20:54:08 by dochoi            #+#    #+#              #
#    Updated: 2020/04/27 04:43:44 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# import matplotlib.pyplot as plt
import numpy as np

class ColorFilter(object):
    def invert(self, array):
        """Authorized function : None
           Authorized operator: """
        return 1.0 - array

    def to_blue(self, array):
        """Authorized function : .zeros, .shape
           Authorized operator: None"""

        array_copy = np.zeros(array.shape)
        array_copy[:, :, 2:] = array[:, :, 2:] # if they have alpha..
        return array_copy

    def to_green(self, array):
        """Authorized function : None
           Authorized operator: *"""

        array_copy = array * 1.0
        array_copy[:,:,:3:2] = 0
        return array_copy

    def to_red(self ,array):
        """Authorized function : green, blue
           Authorized operator: -, +"""

        array_copy_b = self.to_blue(array)
        array_copy_g = self.to_green(array)
        return (array[:,:,:3] - array_copy_b[:,:,:3] - array_copy_g[:,:,:3]) ## idx 3 can be alpha..

    def celluloid(self, array, n_thresholds=4):
        """Authorized function: arange, linspace
        bonus : (Authorized function : .vectorize, (.arange?)
        Authorized operator: None)"""
        if n_thresholds < 2:
            n_thresholds = 2
        base_thresholds = np.linspace(0, 1, n_thresholds)
        base_thresholds_standard = base_thresholds[1] / 2
        def myfunc(a):
            for thr in base_thresholds:
                if thr >= a + base_thresholds_standard:
                    return thr
            return 1.0
        vfunc = np.vectorize(myfunc)
        return vfunc(array)
    def to_grayscale(self, array, filter='w'):

        if filter == 'm' or 'mean':
            """Authorized function : .sum, .shape, reshape, broadcast_to, (as_type?)
           Authorized operator: """
            return np.sum(array[:,:,:3],axis=2) / 3
        elif filter == 'w' or 'weigthed':
            """Authorized function : .sum, .shape, .tile
            Authorized operator: *"""
            base = np.tile([0.299,0.587, 0.114], (200, 200, 1))
            return np.sum((array[:,:,:3] * base),axis=2)
        return None
# te = ColorFilter()
# arr = plt.imread("../resources/test.png")
# arr =arr [:,:,:3]
# print(arr.shape)
# print(*arr.shape)
# ar2 = te.to_grayscale(arr, filter='mean')
# plt.imshow(ar2, cmap='gray')
# # plt.imshow(ar2)
# plt.show()
# plt.imshow(arr)
# plt.show()