#coin flip
import random


def do_choice ():
  print("Enter the corresponding number\n2 - coin flip\n6 - dice flip\n0 - exit\n")
  chc = input()

  if chc == '0':
    return
  elif chc == '2':

    try_luck(chc)
  elif chc == '6':
    try_luck(chc)
  else:
    print("Bad input! Try again!")

  do_choice()

def coin_output(str_res):
  if str_res == '1':
    return 'head'

  return 'tail'


def get_txt_input(str_max_num):

  if str_max_num == '2':
    txt_input = "Guess now! Enter \n1 - for head\n2 - for tail"
  else:
    txt_input = "Guess now! Enter any number from 1 to " + str_max_num

  return txt_input

def get_txt_output (max_num, str_random, str_user_inp):

  if str_random == str_user_inp:
    str_res = "Yes! You got it!\nTry again?"
  else:
    str_res = "You didn't guess...\nTry again!"

  if max_num == 2:
    str_random = coin_output(str_random)
    str_user_inp = coin_output(str_user_inp)

  print("Your choice -  " + str_user_inp + ", my answer - " + str_random + "\n" + str_res)

def try_luck(str_max_num):

  print(get_txt_input(str_max_num))

  str_user_inp = input()

  if str_user_inp.isnumeric():
     user_inp = int(str_user_inp)
     max_num = int(str_max_num)
     if user_inp >= 1 and user_inp <= max_num:
       str_random = str(random.randint(1, max_num))
       get_txt_output(max_num,  str_random, str_user_inp)
       return

  print("Oh... Try again!")
  try_luck (str_max_num)

print("Hi!")
res = do_choice()
print("Try again later. Good luck!")

