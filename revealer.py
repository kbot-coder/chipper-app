from string import printable
from termcolor import colored
from getpass import getpass
from os import sys


def encrypt_decrypt_line(key, words, mode):
    # Mode 1: Encrypt, Mode -1: Decrypt
    return ''.join(characters[(shifts[words[i]] + shifts[key[i % len(key)]] * mode) % len(shifts)]
                                                                        for i in range(len(words)))
if __name__ == "__main__":
    characters = printable[:-3] # create a list of printable characters
    # assign each character to have a specific index value
    shifts = {characters[i]: i for i in range(len(characters))}
    filename = sys.argv[1]
    try:
        with open(filename) as file:
            print("Do you want to encrypt or decrypt this file? Enter ", colored('e', 'yellow', attrs=['bold']), \
                " for encrypt, or ", colored('d', 'yellow', attrs=['bold']), " for decrypt", sep = '')

            validInput = False  # valid input flag
            while not validInput:
                mode = input().strip().lower()
                if mode == 'e':
                    validInput = True
                    key = getpass("Please enter your key:\n")

                    out_filename = "encrypted.txt"
                    f = open(out_filename, "w")
                    for line in file:
                        f.write(encrypt_decrypt_line(key, line.rstrip('\n'), 1))
                        f.write('\n')
                    f.close()
                    print("Encrypted file called", colored("%s" % out_filename, "yellow", attrs=["bold"]),
                    "has been created.")

                elif mode == 'd':
                    validInput = True
                    key = getpass("Please enter your key:\n")

                    out_filename = "decrypted.txt"
                    f = open(out_filename, "w")
                    for line in file:
                        f.write(encrypt_decrypt_line(key, line.rstrip('\n'), -1))
                        f.write('\n')
                    f.close()
                    print("Decrypted file called", colored("%s" % out_filename, "yellow", attrs=["bold"]),
                    "has been created.")
                else:
                    print("Invalid input! ", "Enter ", colored('e', 'yellow', attrs=['bold']), \
                    " for encrypt, or ", colored('d', 'yellow', attrs=['bold']), " for decrypt", sep = '')

            for line in file:
                pass
    except IOError:
        # print error
        print(colored("IOError", "red"), ": No such file called ", \
              colored("%s" % filename, "red"), " in the directory", sep = "")
