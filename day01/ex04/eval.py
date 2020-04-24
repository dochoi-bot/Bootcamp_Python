# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 02:32:12 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 03:05:48 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator(object):
    """docstring"""
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words) or not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        else:
            return sum(list(coef * len(word) for coef, word in zip(coefs, words)))

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words) or not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        else:
            return sum(list(coef * len(words[i]) for i, coef in enumerate(coefs)))

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.enumerate_evaluate(coefs, words))
print(Evaluator.zip_evaluate(coefs, words))
words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))
print(Evaluator.zip_evaluate(coefs, words))