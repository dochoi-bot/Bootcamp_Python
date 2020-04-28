# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 19:58:03 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 20:23:47 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt

class Komparator(object):
    def __init__(self, dataset):
        self.dataset = dataset.drop_duplicates(subset="Name")
    def compare_box_plots(self, categorical_var, numerical_var):
        group_by = self.dataset.groupby(by=categorical_var)
        groups = group_by.groups
        len_groups = len(groups)
        i = 1
        for group in groups:
            subpopulation = group_by.get_group(group)
            plt.subplot(len_groups, 1, i)
            ax = subpopulation[numerical_var].plot.box()
            ax.set(title=group)
            i += 1
        plt.tight_layout()
        plt.show()

    def density(self, categorical_var, numerical_var):
        group_by = self.dataset.groupby(by=categorical_var)
        groups = group_by.groups
        for group in groups:
            subpopulation = group_by.get_group(group)
            subpopulation[numerical_var].plot.density(label=group)
        plt.legend()
        plt.title(numerical_var)
        plt.show()
    def compare_histograms(self, categorical_var, numerical_var):
        group_by = self.dataset.groupby(by=categorical_var)
        groups = group_by.groups
        len_groups = len(groups)
        i = 1
        for group in groups:
            subpopulation = group_by.get_group(group)
            plt.subplot(len_groups, 1, i)
            ax = subpopulation[numerical_var].hist()
            ax.set(title=f"{numerical_var} - {group}")
            i += 1
        plt.tight_layout()
        plt.show()

loader =FileLoader()
data = loader.load("../resources/athlete_events.csv")
ko = Komparator(data)
ko.density("Sex","Weight")