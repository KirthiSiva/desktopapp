# this is the widget which will hold the information of the current device. 
# this widget has a LOT of libraries because there are many libaries which have different components that they can bring. 
import customtkinter as ctk 
import socket
import psutil 
import platform
from PIL import Image 
from pathlib import Path

# use to deal with assets from different devices
DIR_OF_FILE = Path(__file__).resolve().parent
PC_DARK = DIR_OF_FILE / "assets" / "pc_dark.png"
PC_LIGHT = DIR_OF_FILE /  "assets" / "pc_light.png"
LAP_LIGHT = DIR_OF_FILE / "assets" / "lap_light.png"
LAP_DARK = DIR_OF_FILE / "assets" / "lap_dark.png"

class PCDisplay(ctk.CTkFrame):
    def __init__(self, master, width = 400, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # create a heading for this widget 
        self.lbl = ctk.CTkLabel(master, text = "About PC 💻", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 1, column = 0, sticky = "n", pady = 15)
        
        # Placeholder to detect if system is PC or Laptop
        self.isDesktop = False
        
        # get all the data required 
        self.pc_name = socket.gethostname() # get the PC name 
        
        # use psutil for battery stuff
        # add icon here for desktop vs PC, and whether it is needed to add battery
        battery = psutil.sensors_battery() 
        self.time_left = "∞ :)"
        if battery == None: 
            self.isDesktop = True 
        else: 
            # calculate battery life left 
            secs_left = battery.secsleft
            hours = secs_left // 3600 
            minutes = (secs_left % 3600) // 60
            self.time_left = f"Battery left: {hours} hours and {minutes} minutes!"
            
            # set as current battery percentage 
            self.percent = f"{int(battery.percent)}%" 
        
        # use platform for system os, and os version #
        self.pc_platform = platform.platform() 
        
        # actually print it all (display on GUI I mean)
        if self.isDesktop: 
            # icon
            pc_img = ctk.CTkImage(light_image=Image.open(PC_LIGHT), dark_image=Image.open(PC_DARK), size = (90, 115))
            img_lbl = ctk.CTkLabel(master, image=pc_img, text="", bg_color = "#2B2B2B", fg_color = "#2B2B2B")
            img_lbl.grid(row = 1, column = 0, sticky = "w", padx = 135)
        
        else: 
            # icon
            lap_img = ctk.CTkImage(light_image=Image.open(LAP_LIGHT), dark_image=Image.open(LAP_DARK), size = (90, 115))
            img_lbl = ctk.CTkLabel(master, image=lap_img, text="", bg_color = "#2B2B2B", fg_color = "#2B2B2B")
            img_lbl.grid(row = 1, column = 0, sticky = "w", padx = 135)
            
            # battery % (not needed for pc)
            percent_lbl = ctk.CTkLabel(master, bg_color = "#2B2B2B", fg_color = "#2B2B2B", text = self.percent, font = ("Google Sans Flex", 20, "normal"), text_color = "white")
            percent_lbl.grid(row = 1, column = 0, sticky = "s", pady = 80, padx = 100)
            
            # battery life 
            life_lbl = ctk.CTkLabel(master, bg_color = "#2B2B2B", fg_color = "#2B2B2B", text = self.time_left, font = ("Google Sans Flex", 17, "normal"), text_color = "white")
            life_lbl.grid(row = 1, column = 0, sticky = "s", pady = 120, padx = 100)
            
        # pc name 
        pc_lbl = ctk.CTkLabel(master, bg_color = "#2B2B2B", fg_color = "#2B2B2B", text = f"{self.pc_name}", font = ("Google Sans Flex", 20, "normal"), text_color = "white")
        pc_lbl.grid(row = 1, column = 0, rowspan = 2, sticky = "ne", pady = 80, padx = 230)
        
        # pc version 
        pc_lbl = ctk.CTkLabel(master, bg_color = "#2B2B2B", fg_color = "#2B2B2B", text = f"Version: {self.pc_platform}", font = ("Google Sans Flex", 14, "normal"), text_color = "white")
        pc_lbl.grid(row = 1, column = 0, sticky = "ne", pady = 120, padx = 170)
            
       