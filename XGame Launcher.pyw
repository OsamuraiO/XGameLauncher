import os
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# ================================================= #
configfile = open("Data\\theme.json", "r")
theme_object = json.load(configfile)
configfile.close()

# ================================================= #
GAMESFILE = open("Data\\config.json","r")
GAMES_NAME = json.load(GAMESFILE)
GAMESFILE.close()

# ================================================= #
root = Tk()
root.title("XGame Launcher")
root.iconbitmap("Data\\icon.ico")
root.geometry("287x55")
root.resizable(width=False,height=False)
# ================================================= #

selected = StringVar()
Combo = ttk.Combobox(root,values=list(GAMES_NAME['Games'].keys()),background=None,width = 27,state="readonly",textvariable=selected)
Combo.set("Select Game")
Combo.place(x=5,y=5)

def play():
    SELECTED_GAME = selected.get()
    gg = GAMES_NAME['Games'].keys()
    if SELECTED_GAME in list(gg):
        try:
            os.startfile(GAMES_NAME['Games'].get(SELECTED_GAME))
        except:
            messagebox.showerror(title="Error",message=f"Can't open")
    elif SELECTED_GAME == "Select Game":
        messagebox.showinfo(title=" ",message="Please select a game")
    else:
        messagebox.showerror(title="Error",message=f"can't find {SELECTED_GAME}")


Play = Button(root,text="Play",width=10,background=None,foreground=None,command=play)
Play.place(x=200,y=3)

# ================================================= #
def theme_change():
    if theme_object["theme"] == "light":
        theme_object["theme"] = "dark"
    else:
        theme_object["theme"] = "light"

    configfile = open("Data\\theme.json", "w")
    json.dump(theme_object, configfile)
    configfile.close()
    os.startfile("XGame Launcher.pyw")
    root.destroy()

# ================================================= #  
mainmanu = Menu(root)

FILE_MANU = Menu(mainmanu, tearoff=0,background=None,foreground=None)
mainmanu.add_cascade(label="File", menu=FILE_MANU)
FILE_MANU.add_command(label="Add Game (not work)")
FILE_MANU.add_command(label="Remove Game (not work)")
FILE_MANU.add_separator()
FILE_MANU.add_command(label="System Details", command=lambda: os.startfile("Data\\System Info.nfo"))
FILE_MANU.add_separator()
FILE_MANU.add_command(label="Change Theme",command=theme_change)
FILE_MANU.add_command(label="Close", command=root.destroy)

root.config(menu=mainmanu)

# ================================================= #
if theme_object["theme"] == "light":
    root.configure(background='white')
    root['background'] = 'white'
    Combo['background'] = 'white'
    Play['background'] = 'white'
    FILE_MANU['background'] = 'white'
    FILE_MANU['foreground'] = 'black'
else:
    root.configure(background='black')
    root['background'] = 'black'
    Combo['background'] = 'black'
    Play['background'] = 'black'
    Play['foreground'] = 'white'
    FILE_MANU['background'] = 'black'
    FILE_MANU['foreground'] = 'white'



# ================================================= #
root.mainloop()
