# Libraries (psutil needed for the RAM/CPU performance readers)
import customtkinter as ctk
import psutil

# this is the file that will show you the CPU and RAM performance! 

class PerfGraph(ctk.CTkFrame): 
    def __init__(self, master, width = 300, height = 150, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = "#2B2B2B", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # create an instance of the class so that it can do
        
        # add a label 
        self.lbl = ctk.CTkLabel(master, text = "⏱️ RAM/CPU", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 0, column = 2, sticky = "n", pady = 50)
        
        # add a grid system for the labels 
        self.columnconfigure((0, 1), weight=1, uniform="hello")
        self.rowconfigure((0, 1), weight=1, uniform="hello")
        self.grid_propagate(False) # this will cause the frame to not shrink or change in any way
        
        # get the readings for ram and cpu
        self.ram = psutil.virtual_memory().percent 
        self.cpu = psutil.cpu_percent()
        
        # print to the screen now, starting with titles 
        self.lbl_cpu_title = ctk.CTkLabel(self, text = "CPU: ", font = ("Google Sans Flex", 20, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl_cpu_title.grid(row = 0, column = 0, sticky = "n", pady = 15)
        
        self.lbl_ram_title = ctk.CTkLabel(self, text = "RAM: ", font = ("Google Sans Flex", 20, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl_ram_title.grid(row = 1, column = 0, sticky = "n")
        
        # percentages 
        self.lbl_cpu = ctk.CTkLabel(self, text = f"{self.cpu}%", font = ("Google Sans Flex", 20, "normal"), text_color = "white", fg_color="#2B2B2B", bg_color="#2B2B2B")
        self.lbl_cpu.grid(row = 0, column =1, sticky = "n", pady = 15)

        self.lbl_ram = ctk.CTkLabel(self, text = f"{self.ram}%", font = ("Google Sans Flex", 20, "normal"), text_color = "white", fg_color="#2B2B2B", bg_color="#2B2B2B")
        self.lbl_ram.grid(row = 1, column = 1, sticky = "n") 
        
        # update this constantly 
        self.update_percentages() 
    
    # this function is to properly update the percentages so that they always show the realtime values 
    def update_percentages(self): 
        # get the readings for ram and cpu
        self.ram = psutil.virtual_memory().percent 
        self.cpu = psutil.cpu_percent()
        
        # config with new text 
        # the reason why I cannot just put the code of the percentages here is because it will constantly make a NEW label
        # this means there would be hundreds of labels at the same place! 
        self.lbl_cpu.configure(text = f"{self.cpu}%")
        self.lbl_ram.configure(text = f"{self.ram}%")
        
        self.after(2500, self.update_percentages)