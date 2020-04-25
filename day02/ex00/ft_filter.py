# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 16:34:44 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 17:06:02 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, list_of_inputs):
    m = []
    if (function_to_apply is None):
        function_to_apply = lambda x: x
    for i in list_of_inputs:
        if function_to_apply(i) == False:
            continue
        m.append(i)
    return m


# print(list(filter(lambda x: x > 0, range(-5,10))))
# print(list(ft_filter(lambda x: x > 0, range(-5,10))))

# print(list(filter(None,range(-5,10))))
# print(list(ft_filter(None, range(-5,10))))

