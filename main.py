# coin / dice flip game

# User may guess the outcome of a random coin flip(heads/tails) or dice flip (from 1 to 6)
# User may clearly see the result of the coin/dice flip.
# User may see whether or not he/she guessed correctly.

import random


def do_choice():
    # game selection with recursion

    print("Enter the corresponding number\n2 - coin flip\n6 - dice flip\n0 - exit")
    chc = input()

    if chc == '0':
        return
    elif chc == '2':
        try_luck(chc, icoin)
    elif chc == '6':
        try_luck(chc, idice)
    else:
        print("Bad input! Try again!")

    do_choice()


def get_txt_input(str_max_num):
    if str_max_num == '2':
        txt_input = "Guess now! Enter "
        for out in coin_output.keys():
            txt_input += "\n{} - for {}".format(out, coin_output[out])
    else:
        txt_input = "Guess now! Enter any number from 1 to " + str_max_num
    return txt_input


def get_txt_output(max_num, str_random, str_user_inp, igame):

    total_num[igame] += 1
    if str_random == str_user_inp:
        str_res = "Yes! You got it!"
        guessed_num[igame] += 1

    else:
        str_res = "You didn't guess..."

    if max_num == 2:
        str_random = coin_output[str_random]
        str_user_inp = coin_output[str_user_inp]

    print("Your choice -  " + str_user_inp + ", my answer - " + str_random + "\n" + str_res)
    print("Your progress\n   Coin flip: {} guessed / {} total\n   Dice flip: {} guessed / {} total".format(guessed_num[icoin],
                  total_num[icoin], guessed_num[idice], total_num[idice]))

    print("Try again?")


def try_luck(str_max_num, igame):


    print(get_txt_input(str_max_num))
    str_user_inp = input()

    if str_user_inp.isnumeric():
        user_inp = int(str_user_inp)
        max_num = int(str_max_num)
        if (user_inp >= 1) and (user_inp <= max_num):
            str_random = str(random.randint(1, max_num))
            get_txt_output(max_num,  str_random, str_user_inp, igame)
            return

    print("Oh... Try again!")
    try_luck(str_max_num, igame)


# some statistic values initialization...
icoin = 0
idice = 1
total_num = [0, 0]
guessed_num = [0, 0]
coin_output = {'1': 'head', '2': 'tail'}

# start of the game
print("Hi!")
do_choice()
print("Try again later. Good luck!")
# end of the game
