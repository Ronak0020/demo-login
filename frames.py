# Demo Project by Ronak

import customtkinter
import functions
from pathlib import Path
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def LoginFrame(root, prev_frame):
    prev_frame.pack_forget()
    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=50, padx=150, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Berlin Sans FB", 35))
    label.pack(padx=15, pady=30)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", font=("Cascadia code", 10))
    entry1.pack(padx=15, pady=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", font=("Cascadia code", 10), show="*")
    entry2.pack(padx=15, pady=10)

    button = customtkinter.CTkButton(master=frame, text="Login", font=("Berlin Sans FB", 15), command=lambda: functions.login(root, entry1, entry2, button, frame))
    button.pack(padx=15, pady=10)


def RegisterFrame(root, prev_frame):
    prev_frame.pack_forget()
    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=50, padx=150, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Berlin Sans FB", 35))
    label.pack(padx=15, pady=30)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Username", font=("Cascadia code", 10))
    entry1.pack(padx=15, pady=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Password", font=("Cascadia code", 10), show="*")
    entry2.pack(padx=15, pady=10)

    button = customtkinter.CTkButton(master=frame, text="Register", font=("Berlin Sans FB", 15), command=lambda: functions.register(root, entry1, entry2, frame, button))
    button.pack(padx=15, pady=10)

def mainFrame(root):

    for e in root.winfo_children():
        if e != ".!ctkbutton":
            root.nametowidget(e).destroy()

    image = Image.open(relative_to_assets("home.png"))
    HomeImage = customtkinter.CTkImage(light_image=image, size=(50,50))
    
    home = customtkinter.CTkButton(master=root, width=50, height=50, corner_radius=10, image=HomeImage, fg_color="transparent", text="", command=lambda: mainFrame(root=root))
    home.place(x=10, y=10)

    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=50, padx=150, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Berlin Sans FB", 35))
    label.pack(padx=15, pady=30)

    label = customtkinter.CTkLabel(master=frame, text="What would you like to do?", font=("Berlin Sans FB", 25))
    label.pack(padx=15, pady=30)

    button = customtkinter.CTkButton(master=frame, text="Login", font=("Berlin Sans FB", 15), command=lambda: LoginFrame(root, frame))
    button.pack(padx=15, pady=10)

    button = customtkinter.CTkButton(master=frame, text="Register", font=("Berlin Sans FB", 15), command=lambda: RegisterFrame(root, frame))
    button.pack(padx=15, pady=10)

def WelcomeFrame(root, username, *argv):
    for arg in argv:
        try:
            arg.pack_forget()
        except:
            print(arg)
            print("Could not Forget")
    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=50, padx=150, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text=f"Welcome {username}!", font=("Berlin Sans FB", 35))
    label.pack(padx=15, pady=30)

    button = customtkinter.CTkButton(master=frame, text="Logout", font=("Berlin Sans FB", 15), command=lambda: mainFrame(root=root))
    button.pack(padx=15, pady=10)