# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 01:05:55 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 08:17:02 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def text_analyzer(s=""):
    '''
    This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text.
    '''
    ul_n = 0
    ll_n = 0
    pm_n = 0
    space_n = 0
    if s == "":
        print("What is the text to analyse?")
        s = input()
    try:
        for c in s:
            if c >= 'A' and c <= 'Z':
                ul_n += 1
            elif c >= 'a' and c <= 'z':
                ll_n += 1
            elif c == ' ':
                space_n += 1
            elif (c >= '!' and c <= '/')
            or (c >= ':' and c <= '@') or
            (c >= '[' and c <= "'") or (c >= '{' and c <= '~'):
                pm_n += 1
        print("The text contatins", str(len(s)), "characters:\n")
        print("-", str(ul_n), "upper letters\n")
        print("-", str(ll_n), "lower letters\n")
        print("-", str(pm_n), "punctuation marks\n")
        print("-", str(space_n), "spaces")
    except notvalue:
        print("ERROR")
