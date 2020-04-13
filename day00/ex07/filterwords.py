# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi </var/mail/dochoi>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 06:09:55 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 06:09:57 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from string import punctuation
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        if sys.argv[2].isdecimal() and not sys.argv[1].isdecimal():
            s = sys.argv[1].strip(punctuation).split()
            s2 = []
            for part in s:
                if len(part) > (int)(sys.argv[2]):
                    s2.append(part)
            print(s2)
        else:
            print("ERROR")
