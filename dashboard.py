import customtkinter as ctk
from datetime import DateTimeWidget 
from to_do import ToDoList
from tab_set import AutoTabOpen
from colour_swap import ColourSwap
from goal import Goal 
from weather import Weather 
from pc_display import PCDisplay
from prod_graph import ProdGraph
import json 
import csv 

# should probably turn this all into a class soon 

# import fonts 
ctk.FontManager.load_font("GoogleSansFlex-VariableFont_GRAD,ROND,opsz,slnt,wdth,wght.ttf")

# create a ton of csv files for each thing (reading)
#speudocode for the csv
"""

    3 paramatars, name, completion status, and if it is the current thing 
    - if you complete a thing then close the app, when you open the app, it will be removed
    - when i do the productivity graph, it will add itself there
    

"""

# start the dashboard 
app = ctk.CTk() 

# find a scale factor so that this looks good at any resolution 
# first, find the dimensions of the application, then divide by 1080 to get the factor 
# the scale factor will be exactly 1 when you are at
screen_height = app.winfo_screenheight()
scale_factor = screen_height / 1080

# If i cannot figure this out, then I force a certain resolution. 

# define the grid 
app.columnconfigure((0, 1, 2), weight=1, uniform="hello")
app.rowconfigure((0, 1, 2), weight=1, uniform="hello")

app.title("Dashboard 3000")
# used to make it maximize to show task bar and nothing else 
# how does this work on mac? 
app.after(0, lambda: app.state('zoomed'))
app.minsize(1368, 768)

# define all the widgets to add to the program
clock = DateTimeWidget(master = app)
to_do = ToDoList(master = app)
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

# add a label for the auto open tab setting 


# start the main loop 
app.mainloop()