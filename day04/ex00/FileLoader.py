# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/27 23:52:43 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 01:53:46 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

class FileLoader(object):
    def load(self, path):
        data = pd.read_csv(path)
        print("Loading dataset of dimesion", data.shape[0],"x", data.shape[1])
        return data
    def display(self, df, n):
        print(df[:n])
