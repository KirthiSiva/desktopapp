import customtkinter as ctk 
import time

class DateTimeWidget(ctk.CTkFrame):      
    def __init__(self, master, width = 400, height = 400, corner_radius = 100, border_width = None, bg_color = "transparent", fg_color = "#2B2B2B", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.is_24hr = True # gather the state of the clock 
        
        self.grid_propagate(False)
        
        # placeholder for the time 
        self.clock_lbl = ctk.CTkLabel(self, text = "00:00:00", font = ("Google Sans Flex", 96, "bold"))
        self.clock_lbl.pack(pady=(0, 0))
        
        # placeholder for the date 
        self.date_lbl = ctk.CTkLabel(self,  text = "Loading Date...", font = ("Google Sans Flex", 18, "normal"),text_color = "gray")
        self.date_lbl.pack(pady=(0, 5))
        
        # toggle button for 24 hrs and 12 hr 
        self.tgl_btn = ctk.CTkButton(self, text = "12 hr", font = ("Google Sans Flex", 14, "bold"), fg_color = "gray", bg_color= "transparent", hover_color= "black", text_color="white", command=self.toggle_format)
        self.tgl_btn.pack(pady=5)
        
        self.configure(corner_radius = 50)
        
        # start the loop of the clock
        self.tick()
    
    # if statement used to change between 12 and 24 hour formats
    def toggle_format(self): 
        if self.is_24hr: 
            self.is_24hr = False 
            self.tgl_btn.configure(text = "24 hr")
        else: 
            self.is_24hr = True 
            self.tgl_btn.configure(text = "12 hr")
        
        self.update_display()
        
    def update_display(self): 
        # show the time on the screen
        if self.is_24hr: 
            current_time = time.strftime("%H:%M:%S")
        else: 
            current_time = time.strftime("%I:%M:%S %p")
        self.clock_lbl.configure(text = current_time) # change the time 
        
        # show the date on the screen  
        current_date = time.strftime("%A, %B %d, %Y")
        self.date_lbl.configure(text = current_date)
        
    def tick(self): 
        self.update_display()
        self.after(1000, self.tick) # this runs the program every second! 