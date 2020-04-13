# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 01:07:01 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 08:12:52 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

index = len(sys.argv) - 1
if len(sys.argv) == 1:
    sys.exit()
if len(sys.argv) > 2:
    print("ERROR")
else:
    try:
        if (int)(sys.argv[1]) == 0:
            print("I'm Zero.")
        elif (int)(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("ERROR")
