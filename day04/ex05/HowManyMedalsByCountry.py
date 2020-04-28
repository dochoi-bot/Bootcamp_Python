# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 17:45:27 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 17:58:07 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader

def howManyMedalsByCountry(df, name):
    di = {}
    temp = df.loc[(df['Team']==name)][['Year', 'Medal','Sport']].dropna(axis=0).drop_duplicates(keep="first")
    medals = temp.groupby(['Year','Medal']).size().reset_index(name='Count')
    for i in range(medals.shape[0]):
        if medals['Year'][i] not in di.keys():
            di[medals['Year'][i]] = {
            "G": 0,
            "S": 0,
            "B": 0
            }
        di[medals['Year'][i]][medals['Medal'][i][0]] += medals['Count'][i]
    return di



# loader =FileLoader()
# data = loader.load("../resources/athlete_events.csv")
# print(howManyMedalsByCountry(data, "China"))
