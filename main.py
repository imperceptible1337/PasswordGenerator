# libraries
from random import choice
from colorama import Fore
import colorama
colorama.init()
import random

# continue generating a new password
while True:
    # the characters that can be used in the password
    ALL_CHARACTERS = 'abcdefghijklmnopqsrtuvqxyzABCDEFGHIJKLMNOPQSRTUVQXYZ1234567890!@#$%^&*()-_+={}[]|;:"<>,./?'
    # these characters will go used to go first in the password
    NORMAL_CHARACTERS = 'abcdefghijklmnopqsrtuvqxyzABCDEFGHIJKLMNOPQSRTUVQXYZ1234567890'
    # special characters
    SPECIAL_CHARACTERS = '!@#$%^&*()-_+={}[]|;:"<>,./?'

    # these characters will go first in the password
    FIRST_CHARACTER = random.choice(NORMAL_CHARACTERS)

    # get the password length
    PASSWORD_LENGTH = input(f'{Fore.CYAN}[ {Fore.WHITE}- {Fore.CYAN}] {Fore.LIGHTBLUE_EX} Password length > {Fore.RED}')

    # if the user enters nothing for the length, cut the script short
    if PASSWORD_LENGTH == '':
        break
    else:
        continue
    
    # print [0] of the password
    print(f"{Fore.WHITE}{FIRST_CHARACTER}", end="")
    # generate the rest of the password
    for _ in range(int(PASSWORD_LENGTH - 1)):
        REST = random.choice(ALL_CHARACTERS)
        print(REST, end="")

    print()
