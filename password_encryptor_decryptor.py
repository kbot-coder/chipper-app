from string import printable
from os import sys
from tkinter import *
from tkinter import messagebox
import pyperclip

maximum_key_length = 30
maximum_password_length = 30
characters = printable[: -3]
shifts = {characters[i]: i for i in range(len(characters))}

class myGui:
    def __init__(self, master):

        self.var = IntVar()
        frame = Frame(master)

        def callback():
            # print('Button is clicked!')
            password = self.password_entry.get()
            key = self.key_entry.get()
            mode = self.var.get()

            input = True
            if len(key) > maximum_key_length:
                messagebox.showerror('Error', 'Key is too long. Try to input shorter key.')
                input = False
            if len(password) > maximum_password_length:
                messagebox.showerror('Error', 'Password is too long. Try to input shorter password.')
                input = False
            if len(password) == 0 or len(key) == 0:
                messagebox.showerror('Error', 'Password and Key cannot be empty.')
                input = False

            if input == True:
                if mode == 1:
                    encrypted_password = encrypt_decrypt_password(key, password, mode)
                    text_result = 'The encrypted password is:\t' + encrypted_password +\
                            '\nYour password has been copied to the clipboard'
                    pyperclip.copy(encrypted_password)
                    messagebox.showinfo('Result', text_result)

                else:
                    decrypted_password = encrypt_decrypt_password(key, password, mode)
                    text_result = 'The decrypted password is:\t' + decrypted_password +\
                            '\nYour password has been copied to the clipboard'
                    pyperclip.copy(decrypted_password)
                    messagebox.showinfo('Result', text_result)


        frame.pack()
        self.title = Label(frame, text='Enter your password and key below and select mode (encrypt/decrypt).')
        self.title.grid(columnspan=2, padx=20)

        self.label_1 = Label(frame, text='Password:')
        self.label_1.grid(row=1, sticky=E, padx=20, pady=10)

        self.label_2 = Label(frame, text='Key:')
        self.label_2.grid(row=2, sticky=E, padx=20)

        self.password_entry = Entry(frame, width=30)
        self.password_entry.grid(row=1, column=1, padx=20, pady=10)

        self.key_entry = Entry(frame, width=30)
        self.key_entry.grid(row=2, column=1, padx=20)

        self.rb1 = Radiobutton(frame, text = 'Encrypt', variable = self.var, value = 1)
        self.rb1.grid(row=3, column=0, pady=10, sticky = E)
        self.rb2 = Radiobutton(frame, text = 'Decrypt', variable = self.var, value = -1)
        self.rb2.grid(row=3, column=1,pady=10)

        self.var.set(1)

        self.run_button = Button(frame, text = 'Generate', command=callback, width=10, height = 2)
        self.run_button.grid(row=4, columnspan=2)

def encrypt_decrypt_password(key, password, mode):
    # Mode 1: Encrypt, Mode -1: Decrypt
    return ''.join(characters[(shifts[password[i]] + shifts[key[i % len(key)]] * mode) % len(shifts)]
                                                                        for i in range(len(password)))

if __name__ == '__main__':

    root = Tk()
    root.resizable(width=False, height=False)
    w = 450 # width for the Tk root
    h = 200 # height for the Tk root

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    b = myGui(root)

    root.mainloop()
