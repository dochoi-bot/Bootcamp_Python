# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/23 21:58:34 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 02:31:51 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

def cmp(a):
    return [int(ord(i)) % 95 for i in a]

def randNum(x):
    return ((x * 1103515245) + 123456 )% 2147483648

def getRandomNumbers(a):
    randCount = 1
    initial = int(time.time() * 10000000)
    i = 0
    while i < randCount:
        i += 1
        initial += randNum(initial)
    return(int(initial) % 2147483648)

def generator(text, sep=" ", option=None):
    if not isinstance(text, (str)):
        return ("ERROR")
    if option == "ordered":
        temp = sorted(text.split(sep=sep), key=cmp)
        for i in temp:
            yield i
    elif option == "shuffle":
        temp = sorted(text.split(sep=sep), key=getRandomNumbers)
        for i in temp:
            yield i
    elif option == "unique":
        temp = text.split(sep=sep)
        temp2 = []
        for i in temp:
            if i not in temp2:
                temp2.append(i)
                yield i
    else:
        temp = text.split(sep=sep)
        for i in temp:
            yield i

text = "Le Lorem Ipsum est simplement du faux texte. tExte a a b b A B B"
for word in generator(text, sep=" "):
    print(word)
print()
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print()
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print()
for word in generator(text, sep=" ", option="unique"):
    print(word)