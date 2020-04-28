# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 17:06:13 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 17:44:03 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

class SpatioTemporalData(object):
    def __init__(self,df):
        self.df = df
    def when(self, location):
        return list(self.df.loc[self.df['City']==location]['Year'].unique())
    def where(self, date):
        return list(self.df.loc[self.df['Year']==date]['City'].unique())

# loader =FileLoader()
# data = loader.load("../resources/athlete_events.csv")
# sp = SpatioTemporalData(data)
# print(sp.where(1896))
# print(sp.where(2016))
# print(sp.when('Athina'))
# print(sp.when('Paris'))
# # print(howManyMedals(data, "Kjetil Andr Aamodt"))
