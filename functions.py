# Demo Project by Ronak

import customtkinter
from frames import *

details = {}


def createPopMessage(frame, *argv):
    frame.pack_forget()
    for arg in argv:
        arg.configure(state="normal")
        arg.configure(state="normal")
        arg.configure(state="normal")
        arg.configure(state="normal")

def login(root, entry1, entry2, pbutton, pframe):
    username = entry1.get()
    password = entry2.get()
    entry2.delete(0, 'end')
    if details.get(username) == None:
        entry1.configure(state="disabled")
        entry2.configure(state="disabled")
        pbutton.configure(state="disabled")
        frame = customtkinter.CTkFrame(root)
        frame.pack(pady=5, padx=5, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Incorrect Details! You are not registered!", font=("Berlin Sans FB", 15))
        label.pack(padx=5, pady=5)

        button = customtkinter.CTkButton(master=frame, text="Retry", font=("Berlin Sans FB", 10), command=lambda: createPopMessage(frame, pbutton, pframe, entry1, entry2))
        button.pack(padx=5, pady=5)
    else:
        if password != details.get(username):
            entry1.configure(state="disabled")
            entry2.configure(state="disabled")
            pbutton.configure(state="disabled")
            frame = customtkinter.CTkFrame(root)
            frame.pack(pady=5, padx=5, fill="both", expand=True)

            label = customtkinter.CTkLabel(master=frame, text="Incorrect Password!", font=("Berlin Sans FB", 15))
            label.pack(padx=5, pady=5)

            button = customtkinter.CTkButton(master=frame, text="Retry", font=("Berlin Sans FB", 10), command=lambda: createPopMessage(frame, pbutton, pframe, entry1, entry2))
            button.pack(padx=5, pady=5)
        else:
            entry1.configure(state="disabled")
            entry2.configure(state="disabled")
            pbutton.configure(state="disabled")
            frame = customtkinter.CTkFrame(root)
            frame.pack(pady=5, padx=5, fill="both", expand=True)

            label = customtkinter.CTkLabel(master=frame, text="Successfully Logged in! Press Continue.", font=("Berlin Sans FB", 15))
            label.pack(padx=5, pady=5)

            button = customtkinter.CTkButton(master=frame, text="Continue", font=("Berlin Sans FB", 10), command=lambda: WelcomeFrame(root, username, button, frame, pframe, entry1, entry2, pbutton, label))
            button.pack(padx=5, pady=5)


def register(root, entry1, entry2, pframe, pbutton):
    username = entry1.get()
    password = entry2.get()

    details[username] = password
    entry2.delete(0, 'end')
    entry1.configure(state="disabled")
    entry2.configure(state="disabled")
    pbutton.configure(state="disabled")
    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=5, padx=5, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="You have successfully registered! Log in now.", font=("Berlin Sans FB", 15))
    label.pack(padx=5, pady=5)

    button = customtkinter.CTkButton(master=frame, text="Ok!", font=("Berlin Sans FB", 10), command=lambda: createPopMessage(frame, pbutton, pframe, entry1, entry2))
    button.pack(padx=5, pady=5)