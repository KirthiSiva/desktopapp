# All the libraries that I will be using for the dashboard
import json 
import csv 
import customtkinter as ctk
import getpass 
from pathlib import Path

# All the classes/modules that I am using for my project 
from clock import DateTimeWidget 
from to_do import ToDoList
from tab_set import AutoTabOpen
from cpu_gpu_perf import PerfGraph
from goal import Goal 
from weather import Weather 
from pc_display import PCDisplay
from pomodoro import Timer 

# import fonts 
DIR = Path(__file__).resolve().parent
google_font_dir = DIR / "assets" / "GoogleSansFlex-VariableFont_GRAD,ROND,opsz,slnt,wdth,wght.ttf"
ctk.FontManager.load_font(str(google_font_dir))

# function to read from the to_do list json
def save_read_todo(): 
    pass

ctk.set_default_color_theme("blue")
# start the dashboard 
app = ctk.CTk() 

# define the grid 
app.columnconfigure((0, 1, 2), weight=1, uniform="hello")
app.rowconfigure((0, 1, 2), weight=1, uniform="hello")

# Detect the user profile name, and set that as the app title  
name = getpass.getuser()
app.title(f"Welcome, {name}!") # use the "getpass" library to get the username of the device 

# maximize the screen 
app.after(0, lambda: app.state('zoomed'))

# set a minimum size that the screen can be 
app.minsize(1920, 1050)

# define all the widgets to add to the program
clock = DateTimeWidget(master = app)
to_do = ToDoList(master = app, values = [])
tab = AutoTabOpen(master = app) 
hardware = PerfGraph(master = app)
goal = Goal(master = app) 
weather = Weather(master = app)
pc_display = PCDisplay(master = app)
timer = Timer(master = app)

# add all the widgets to the grid 
clock.grid(row = 1, column = 1, padx = 20, pady = 20)
to_do.grid(row = 1, column = 2, sticky = "nsew", padx = 40)
tab.grid(row = 0, column = 1, sticky = "nwe", pady = 60)
hardware.grid(row = 0, column = 2, sticky = "ne", padx = 200, pady= 100)
goal.grid(row = 2, column = 2, sticky = "we", padx = (70))
weather.grid(row = 0, column = 0)
pc_display.grid(row = 1, column = 0)
timer.grid(row = 2, column = 0, sticky = "we", padx = (100, 0))

ctk.set_default_color_theme("blue")

# start the main loop 
app.mainloop()