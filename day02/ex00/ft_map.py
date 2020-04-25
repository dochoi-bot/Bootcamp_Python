# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 16:34:47 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 16:58:31 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, list_of_inputs):
    m = list(function_to_apply(i) for i in list_of_inputs)
    return m