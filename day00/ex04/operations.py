# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 01:06:10 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 07:43:47 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def five_value(a, b):

    if b == 0:
        div = "ERROR (div by zero)"
        mod = "ERROR (modulo by zero)"
    else:
        div = a / b
        mod = a % b
    return (a + b, a - b, a * b, div, mod)


if __name__ == "__main__":
    argc = len(sys.argv)
    a = 0
    b = 0
    if argc > 3:
        print("InputError: too many arguments\n")
    if argc != 3:
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
        sys.exit(1)
    try:
        a = (int)(sys.argv[1])
        b = (int)(sys.argv[2])
        f_value = five_value(a,b)
        print("Sum:         ", f_value[0])
        print("Differnce:   ", f_value[1])
        print("Product:     ", f_value[2])
        print("Quotient:    ", f_value[3])
        print("Remainder:   ", f_value[4])
    except ValueError:
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")

