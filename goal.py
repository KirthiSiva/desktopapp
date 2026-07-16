# this is the widget which will hold the current goal that is being achieved. 
import customtkinter as ctk 
import json 

# use a dropdown to select a goal 
class Goal(ctk.CTkFrame):
    def __init__(self, master, width = 400, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        