# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 00:18:57 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 01:37:35 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

def youngestFellah(df, year):
    youngest_male = df.loc[(df['Year']==year) & (df['Sex']=="M")]['Age'].min()
    youngest_female = df.loc[(df['Year']==year) & (df['Sex']=="F")]['Age'].min()
    return {'f' : youngest_male, 'm': youngest_female}


    # f = 1000.0
    # m = 1000.0
    # for i in range(0, df.shape[0]):
    #     if int(df['Year'][i]) == year and f > float(df['Age'][i]) and df['Sex'][i] == "F":
    #         f = float(df['Age'][i])
    #     if int(df['Year'][i]) == year and m > float(df['Age'][i]) and df['Sex'][i] == "M":
    #         m = float(df['Age'][i])
    # return {'f': f, 'm': m}
    # is possible, but very slow , so using lib function