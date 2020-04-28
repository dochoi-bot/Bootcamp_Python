# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 02:10:59 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 02:19:25 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def howManyMedals(data, name):
    di = {}
    down = len(df.loc[(df['Year']==year) & (df['Sex']== gender)]['Name'].unique())
    up = len(df.loc[(df['Year']==year)  & (df['Sport']== sportname) & (df['Sex']== gender)]['Name'].unique())
    return up / down


# loader =FileLoader()
# data = loader.load("../resources/athlete_events.csv")
# print(proportionBySport(data, 2004, "Tennis","F"))
