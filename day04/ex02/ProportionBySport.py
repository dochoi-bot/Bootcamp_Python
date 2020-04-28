# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 01:54:28 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 02:10:22 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# from FileLoader import FileLoader
import pandas as pd

def proportionBySport(df, year , sportname, gender):
    down = len(df.loc[(df['Year']==year) & (df['Sex']== gender)]['Name'].unique())
    up = len(df.loc[(df['Year']==year)  & (df['Sport']== sportname) & (df['Sex']== gender)]['Name'].unique())
    return up / down

# loader =FileLoader()
# data = loader.load("../resources/athlete_events.csv")
# print(proportionBySport(data, 2004, "Tennis","F"))