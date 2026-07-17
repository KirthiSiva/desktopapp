# All the libraries that I will be using for the dashboard
import customtkinter as ctk
import getpass 
from pathlib import Path
import json
import os

# this library is important to stop any crashing from the threading
# I have in the APIs 
import multiprocessing 

if __name__ == '__main__':
    multiprocessing.freeze_support()

# All the classes/modules that I am using for my project 
from widgets.clock import DateTimeWidget 
from widgets.to_do import ToDoList
from widgets.tab_set import AutoTabOpen
from widgets.cpu_gpu_perf import PerfGraph
from widgets.quotes import QuoteGen 
from widgets.weather import Weather 
from widgets.pc_display import PCDisplay
from widgets.pomodoro import Timer 
from widgets.fractal_tree import Fractal

# import fonts 
DIR = Path(__file__).resolve().parent
google_font_dir = DIR / "widgets" / "assets" / "GoogleSansFlex-VariableFont_GRAD,ROND,opsz,slnt,wdth,wght.ttf"
ctk.FontManager.load_font(str(google_font_dir))

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

# make a function to load in the json from the 

# define all the widgets to add to the program
fractal = Fractal(master = app)
clock = DateTimeWidget(master = app)
to_do = ToDoList(master = app, fractal = fractal)
tab = AutoTabOpen(master = app) 
hardware = PerfGraph(master = app)
quotes = QuoteGen(master = app) 
weather = Weather(master = app)
pc_display = PCDisplay(master = app)
timer = Timer(master = app)

# add all the widgets to the grid 
# rowspan and columnspan make it able to "leave" its own quadrant! perfect for what I want 
fractal.grid(row = 0, column = 0, rowspan=3, columnspan=3) # it starts at the center 

clock.grid(row = 1, column = 1, sticky = "new", pady = 30)
clock.lift() # it is getting cut off right now so make it the top of the screen
to_do.grid(row = 1, column = 2, sticky = "nsew", padx = 40)
tab.grid(row = 0, column = 1, sticky = "nwe", pady = 60)
hardware.grid(row = 0, column = 2, sticky = "ne", padx = 200, pady= 100)
quotes.grid(row = 2, column = 2, sticky = "we", padx = (70))
weather.grid(row = 0, column = 0)
pc_display.grid(row = 1, column = 0)
timer.grid(row = 2, column = 0, sticky = "we", padx = (100, 0))

# start the main loop 
app.mainloop()