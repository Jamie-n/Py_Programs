

import random
import string



def string_creator(string_len):
    letters = string.punctuation + string.ascii_letters
    print(''.join(random.choice(letters) for i in range(string_len)))


string_creator(int(input("How long does the password need to be?\n")))



