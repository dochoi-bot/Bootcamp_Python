# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi </var/mail/dochoi>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 06:08:45 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 07:20:29 by dochoi           ###   ########.fr        #
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
if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
