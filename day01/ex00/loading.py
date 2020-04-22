# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 06:08:45 by dochoi            #+#    #+#              #
#    Updated: 2020/04/23 03:37:56 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import time, sleep
import sys

def ft_progress(lst):
    start = time()
    maximum = len(lst)
    for elem in lst:
        yield elem
        cur = time() - start
        elem += 1
        per = (elem / maximum * 100.0)
        eta = ((maximum * cur) / elem) - cur
        bar = "=" * int(elem / maximum * 24) + ">"
        print("\rETA: %.2fs [%3.0f%%][%-24s] %d/%d | elapsed time %.2fs" % (eta, per, bar, elem,maximum, cur),end = '')
