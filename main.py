# Demo Project by Ronak

from pathlib import Path
import customtkinter
from functions import *
from frames import *
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = customtkinter.CTk()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root.geometry("800x500")
root.resizable(False, False)
root.title("Login System")

mainFrame(root=root)

root.mainloop()