# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/26 17:58:23 by dochoi            #+#    #+#              #
#    Updated: 2020/04/26 20:08:48 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt

class ImageProcessor(object):

    def load(self, path):
        arr = plt.imread(path)
        print("Loading image of dimensions %d x %d" % (arr.shape[0], arr.shape[1]))
        return (arr)
    def display(self, array):
        plt.imshow(array)
        plt.show()