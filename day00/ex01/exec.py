# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 01:07:07 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 08:12:20 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

index = len(sys.argv) - 1
while index > 0:
    s = sys.argv[index].swapcase()
    print(s[::-1], end='')
    if (index != 1):
        print(end=' ')
    index -= 1
