# libraries
from random import choice
from colorama import Fore
import colorama
import argparse
import random

# initialize colorama
colorama.init()

# define arguements for argparse
parser = argparse.ArgumentParser(description='A password generator\nexample: main.py 10')
parser.add_argument('password_length', type=int, help='Enter the the desired password length')
args = parser.parse_args()

password_length = args.password_length

# the characters that can be used in the password
ALL_CHARACTERS = "abcdefghijklmnopqsrtuvqxyzABCDEFGHIJKLMNOPQSRTUVQXYZ1234567890!@#$%^&*()-_+={}[]|;:'<>,./?"
# these characters will go used to go first in the password
NORMAL_CHARACTERS = 'abcdefghijklmnopqsrtuvqxyzABCDEFGHIJKLMNOPQSRTUVQXYZ1234567890'
# special characters
SPECIAL_CHARACTERS = '!@#$%^&*()-_+={}[]|;:"<>,./?'

# these characters will go first in the password
FIRST_CHARACTER = random.choice(NORMAL_CHARACTERS)

# print [0] of the password
print(f'{Fore.WHITE}{FIRST_CHARACTER}', end='')
# generate the rest of the password
for _ in range(int(password_length) - 1):
    REST = random.choice(ALL_CHARACTERS)
    print(REST, end='')

print()
