# All the libraries that I will be using for the dashboard
import json 
import csv 
import customtkinter as ctk
import getpass 

# All the classes/modules that I am using for my project 
from datetime import DateTimeWidget 
from to_do import ToDoList
from tab_set import AutoTabOpen
from colour_swap import ColourSwap
from goal import Goal 
from weather import Weather 
from pc_display import PCDisplay
from prod_graph import ProdGraph
from pathlib import Path


# import fonts 
ctk.FontManager.load_font("GoogleSansFlex-VariableFont_GRAD,ROND,opsz,slnt,wdth,wght.ttf")

# create a ton of csv files for each thing (reading)
#speudocode for the csv
"""

    3 paramatars, name, completion status, and if it is the current thing 
    - if you complete a thing then close the app, when you open the app, it will be removed
    - when i do the productivity graph, it will add itself there
    

"""

# set a value for "values" for the to-do list checklists
to_do_values = ["hello"]

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
to_do = ToDoList(master = app, values = to_do_values)
tab = AutoTabOpen(master = app) 
colour = ColourSwap(master = app)
goal = Goal(master = app) 
weather = Weather(master = app)
pc_display = PCDisplay(master = app)

# add all the widgets to the grid 
clock.grid(row = 1, column = 1, padx = 20, pady = 20)
to_do.grid(row = 1, column = 2, sticky = "nsew", padx = 40)
tab.grid(row = 0, column = 1, sticky = "nwe", pady = 50)
colour.grid(row = 0, column = 2, sticky = "ne", padx = 200, pady= 100)
goal.grid(row = 2, column = 2, sticky = "e", padx = 40)
weather.grid(row = 0, column = 0)
pc_display.grid(row = 1, column = 0)

# start the main loop 
app.mainloop()