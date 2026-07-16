# this class is here for the automatic tab open slot.
# i will be using hte "web browser" module for this to work 
# i will also be using a json to SAVE the data from the web opener 
import webbrowser
import customtkinter as ctk 

"""

How to edit the actual buttons (Force a limit of 5). 
- When you click on them, it opens the window to be able to CHANGE the links of them! 
- I can save each button into its own json (well i mean together but ykwim)
- Wait, instead of this, I can make it so that there is only a single button there to edit each thing, 
and then there is one button to OPEN the screen to edit them all! If I have time of course to do this. 


"""

# this class is for the buttons that will be held here. 
# These buttons will be used to edit the links of the tab
# set the urls as a deeper property of it that is not shown (unless using the window)
class TabButton(ctk.CTkButton): 
    pass
    # figure out how to detect button state to launch window and change url 

class AutoTabOpen(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 50, corner_radius = 100, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

    # have a button in here to actually open all the tabs 
       
        