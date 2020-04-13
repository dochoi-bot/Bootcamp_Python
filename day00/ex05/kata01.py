# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 01:06:31 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 08:20:49 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {'Python': 'Guido van Rossum',
                       'Ruby': 'Yukihiro Matsumoto',
                       'PHP': 'Rasmus Lerdorf', }
for key in languages.keys():
    print(key, "was created by", languages[key])
