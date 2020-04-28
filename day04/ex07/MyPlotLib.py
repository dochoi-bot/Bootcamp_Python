# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 17:59:37 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 19:56:41 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd
from matplotlib import pyplot as plt

class MyPlotLib(object):

    def histogram(self, data, features):
        data.drop_duplicates(subset="Name").hist(column=features)
        plt.show()
        plt.show()
    def density(self, data, features):
        data.drop_duplicates(subset="Name")[features].plot.density()
        plt.show()
    def pair_plot(self, data, features):
        pd.plotting.scatter_matrix(data.drop_duplicates(subset="Name")[features])
        plt.show()

    def box_plot(self, data, features):
        data.drop_duplicates(subset="Name")[features].plot.box()
        plt.show()

loader =FileLoader()
data = loader.load("../resources/athlete_events.csv")
ml = MyPlotLib()
ml.box_plot(data, ["Height", "Weight"])