# this is the widget which will hold the weather of the current location 
import customtkinter as ctk 
import json 
import urllib.request #used for the apis 
import threading # this library is very important for running many processes at the same time 

class Weather(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # Create a grid
        self.rowconfigure(0, weight = 2, uniform="hello") # the reason why I made it 2 is because I want this to hold the icon, which will take a lot of space
        self.rowconfigure((1,2), weight = 1, uniform="hello")
        self.columnconfigure(0, weight= 1, uniform= "hello")
        
        # Create the labels for the 
        