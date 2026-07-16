# this is the widget which will hold the information of the current device. 
import customtkinter as ctk 
import json 
import socket
import psutil 
import platform
from PIL import Image 
from pathlib import Path

# use to deal with assets from different devices
DIR_OF_FILE = Path(__file__).resolve().parent

class PCDisplay(ctk.CTkFrame):
    def __init__(self, master, width = 400, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # create a heading for this widget 
        self.lbl = ctk.CTkLabel(master, text = "About PC", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 1, column = 0, sticky = "n", pady = 15)
        
        # Placeholder to detect if system is PC or Laptop
        self.isDesktop = False
        
        # get all the data required 
        self.pc_name = socket.gethostname() # get the PC name 
        
        # use psutil for battery %, CPU, 
        # add icon here for desktop vs PC, and whether it is needed to add battery
        battery = psutil.sensors_battery() 
        self.percent = battery.percent
        self.time_left = "∞ :)"
        if battery == None: 
            self.isDesktop = True 
        else: 
            self.time_left = f"Battery left: {battery.power_plugged() * 3600} hours!"

        
        # use platform for system os, and os version #
        self.pc_platform = platform.platform() 
        
        # actually print it all (display on GUI I mean)
        if 
        