# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 17:06:09 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 17:20:57 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
    for i, input in enumerate(list_of_inputs):
        if i == 0:
            re = input
        else:
            re = function_to_apply(re, input)
    return re

# sum_value = reduce((lambda x,y : x+y), [x for x in range(1,101)])
# print(sum_value)
# sum_value2 = ft_reduce((lambda x,y : x+y), [x for x in range(1,101)])
# print(sum_value2)