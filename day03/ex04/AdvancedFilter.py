# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    AdvancedFilter.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/27 17:29:38 by dochoi            #+#    #+#              #
#    Updated: 2020/04/27 19:32:23 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# import matplotlib.pyplot as plt
import numpy as np

class AdvancedFilter(object):
    def mean_blur(self, array, kn_size=3):
        if kn_size % 2 != 1:
            print("must be a odd number")
            return None
        if kn_size == 1:
            return array.copy()
        kernel = np.ones((kn_size, kn_size), dtype=float) / (kn_size * kn_size)
        y, x = array.shape[:2]
        y = y - kn_size + 1
        x = x - kn_size + 1
        array_base = np.zeros((y,x,array.shape[2]))
        for i in range(y):
            for j in range(x):
                array_base[i,j,0] = np.sum(array[i:i+kn_size, j:j+kn_size, 0] * kernel)
                array_base[i,j,1] = np.sum(array[i:i+kn_size, j:j+kn_size, 1] * kernel)
                array_base[i,j,2] = np.sum(array[i:i+kn_size, j:j+kn_size, 2] * kernel)
        return (array_base)

    def median_blur(self, array, kn_size=3):# just made... using sort

        if kn_size % 2 != 1:
            print("must be a odd number")
            return None
        if kn_size == 1:
            return array.copy()
        kernel = np.ones((kn_size, kn_size), dtype=float)
        y, x = array.shape[:2]
        y = y - kn_size + 1
        x = x - kn_size + 1
        array_base = np.zeros((y,x,array.shape[2]))
        for i in range(y):
            for j in range(x):
                array_base[i,j,0] = np.sort(np.ravel(array[i:i+kn_size, j:j+kn_size, 0] * kernel))[int(kn_size / 2)]
                array_base[i,j,1] = np.sort(np.ravel(array[i:i+kn_size, j:j+kn_size, 1] * kernel))[int(kn_size / 2)]
                array_base[i,j,2] = np.sort(np.ravel(array[i:i+kn_size, j:j+kn_size, 2] * kernel))[int(kn_size / 2)]
        return (array_base)

    def gaussain_blur(self, array, kn_size=3, sigma=1):

        def get_gauss_kernel(size, sigma):
            center=(int)(size/2)
            kernel=np.zeros((size,size))
            for i in range(size):
                for j in range(size):
                    diff=np.sqrt((i-center)**2+(j-center)**2)
                    kernel[i,j]=np.exp(-(diff**2)/(2*sigma**2))
            return kernel/np.sum(kernel)

        if kn_size % 2 != 1:
            print("must be a odd number")
        if kn_size == 1:
            return array.copy()
        kernel = get_gauss_kernel(kn_size, sigma)
        y, x = array.shape[:2]
        y = y - kn_size + 1
        x = x - kn_size + 1
        array_base = np.zeros((y,x,array.shape[2]))
        for i in range(y):
            for j in range(x):
                array_base[i,j,0] = np.sum(array[i:i+kn_size, j:j+kn_size, 0] * kernel)
                array_base[i,j,1] = np.sum(array[i:i+kn_size, j:j+kn_size, 1] * kernel)
                array_base[i,j,2] = np.sum(array[i:i+kn_size, j:j+kn_size, 2] * kernel)
        return (array_base)


# te = AdvancedFilter()
# arr = plt.imread("../resources/test.png")
# arr =arr [:,:,:3]
# ar2 = te.median_blur(arr, 3,)
# plt.imshow(ar2)
# plt.show()
# plt.imshow(arr)
# plt.show()