import customtkinter as ctk

# this is the file that will hold the way to change the colour 
"""

Have a list of colours (maybe 5) prechosen, and be able to cycle through them
- Within the frame, It should have a label of "Theme," then 5 circles under it to change! 
- 

"""

class ColourSwap(ctk.CTkFrame): 
    def __init__(self, master, width = 300, height = 150, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        