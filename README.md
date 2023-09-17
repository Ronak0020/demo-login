# Demo Login system GUI
This project was made just as a demo testing project to test the python library *tkinter* [customtkinter has been used]. It took approx 15 minutes to make it so don't expect too much out of it :p

# Key Features
- User Friendly UI
- Multiple Frames (login, register, main screen, welcome screen)
- Details saved in a local dictionary (will be cleared on closing the application)
- Included .exe file (inside the *app* folder) to test the application
- A HOME button to go back to the main screen frame

# How to run
To run the code, simply download and extract the code from github or clone this repository
Then inside the code folder, open terminal
in terminal, type `python3 main.py`
The GUI will be launched.

# Files
- `main.py` - File for the initial launching of the application
- `functions.py` - File that includes the functions to login, register, etc. Also has the dictionary to save new details in there.
- `frames.py` - File that includes functions to apply each frame.

# Frames Available
- Main Frame [the initial screen you see on launching the application, containint login and register button]
- Login Frame [the frame where you get 2 entries to input your password and username and a button to login]
- Register Frame [the frame where you get 2 entries to input your password and username and a button to register]
- Welcome Frame [on successfully logging in, welcome screen is shown]
Other frame includes:
- Incorrect password frame [over the login screen]
- Incorrect account frame [over the login screen if username is not found in the dictionary]
- Successfully Logged in Frame [over the login screen if successfully logged in]
- Registered frame [over the register frame once you have registered]

### I have used `pyinstaller` to convert these python scripts into exe file (found inside the **app** folder) 

#### You are free to edit this however you want or use it as a reference to understand how customtkinter works
**By:** Ronak Khandelwal
**Purpose:** Just for fun :p Was testing out customtkinter library
