# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi </var/mail/dochoi>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 06:09:03 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 07:07:13 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import sys

if __name__ == "__main__":
    answer = random.randint(1,99)
    n = 0
    cnt = 0

    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!\n")
    while True:
        cnt += 1
        print("What's your guess between 1 and 99?")
        n = input()
        if n == 'exit':
            print("Goodbye!")
            break
        if not n.isdecimal():
            print("That's not a number.")
            continue
        n_int = int(n)
        if (n_int < 1 or n_int > 99):
            print("The number must be between 1 and 99.")
        elif answer > n_int:
            print("Too low!")
        elif answer < n_int:
            print("Too high!")
        elif answer == n_int:
            if n_int == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if cnt == 1:
                print("Congratulations! You got it on your first try!")
            else :
                print("Congratulations, you've got it! You won in",cnt ,"attempts!")
            break
