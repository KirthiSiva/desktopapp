# libraries 
# I use "time" to deal with the timer! 
import time 
import customtkinter as ctk 

# A pomodoro timer is a timer where you have 25 minutes of uninterupted work, followed by 5 minutes of breaks
# This keeps going as a cycle (I think technically it is supposed to take a larger break after 4 of these cycles, but I don't need that)
class Timer(ctk.CTkFrame):
    def __init__(self, master, width = 400, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # declare some variables for the time r
        self.default_time = 25 * 60 # to get seconds
        self.break_time = 5 * 60 # to get seconds of break
        self.timer_mode = "work" # work = 25 min, break = 5 min
        self.seconds_left =  self.default_time
        self.running = False # the timer currently isn't running 
        self.timer_id = None
        
        # create a label for the window 
        self.lbl = ctk.CTkLabel(master, text = "Pomodoro ⏳", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 2, column = 0, sticky = "ne", padx = 150, pady = 15)
        
        # create a grid system 
        self.grid_columnconfigure(0, weight = 3, uniform="hello")
        self.grid_columnconfigure(1, weight =1, uniform="hello")
        self.grid_rowconfigure(0, weight = 1, uniform="hello")
        self.grid_propagate(False)
        
        # Create 2 buttons, one for "start" and one for "stop"
        self.btn_stop = ctk.CTkButton(self, text = "Reset", font = ("Google Sans Flex", 20, "bold"), corner_radius = 20, text_color = "white", fg_color="gray", bg_color="transparent", hover_color = "black", command=self.stop_clicked)
        self.btn_stop.grid(column = 1, row = 0, sticky = "se", pady = 30, padx = 20)
        
        self.btn_start = ctk.CTkButton(self, text = "Start", font = ("Google Sans Flex", 20, "bold"), corner_radius = 20, text_color = "white", fg_color="gray", bg_color="transparent", hover_color = "black", command=self.start_clicked)
        self.btn_start.grid(column = 1, row = 0, sticky = "ne", pady = 30, padx = 20)
        
        # create the label for the clock 
        # start with text at 25 minutes
        self.timer = ctk.CTkLabel(self, text = "25:00", font = ("Google Sans Flex", 80, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.timer.grid(row = 0, column = 0)
    
    # function for stopping and resetting the timer 
    def stop_clicked(self): 
        # kill background loop so that it does not break when starting tiemr again
        if self.timer_id is not None: 
            self.after_cancel(self.timer_id) 
            self.timer_id = None
        
        # kill the loop, and refresh back to 25 minutes
        self.running = False 
        self.timer_mode = "work"
        self.seconds_left = self.default_time
        self.timer.configure(text = "25:00")
        
        # enable the start button again 
        self.btn_start.configure(state="normal")

    # function for actually starting the timer 
    def start_clicked(self): 
        # first make sure it currently is not running
        if not self.running: 
            self.running = True
            self.btn_start.configure(state="disabled") # no need for start button after clicking
            self.last_tick = time.time() # get current real-time time 
            self.countdown_loop()
            
    # function which actually deals with the timer 
    def countdown_loop(self): 
        # make sure that hte loop is running, otherwise return
        if not self.running: 
            return 
        
        # get the current time, then subtract with last tick to interate through the clock
        if self.seconds_left > 0: # make sure the timer isnt complete
            current_time = time.time()
            time_passed = current_time - self.last_tick

            # actually changing the time now 
            self.seconds_left -= int(time_passed)
            
            # prevent it from going negative
            if self.seconds_left < 0: 
                self.seconds_left = 0
                
            self.last_tick = current_time
            
            # using a divmod to properly allocate hours and seconds by finding remainder (modulo)
            minutes, seconds = divmod(self.seconds_left, 60)
            time_screen = f"{minutes:02d}:{seconds:02d}" #02d forces at least 2 ditis (e.g. turns 6:25 into 06:25)
            
            # update to screen
            self.timer.configure(text = time_screen)
            
            # keep doing this every second
            self._timer_id = self.after(1000, self.countdown_loop)
        
        # if the timer hits 0
        else:
            self.timer_id = None 
            self.swap_modes() # now, it will do a 5 minute timer, then a 25, and repeat.
        
    # this is the function that changes the time from 25 to 5 
    def swap_modes(self): 
        if self.timer_mode == "work": 
            # now switch to break mode 
            self.timer_mode = "break"
            self.seconds_left = self.break_time # make this the new default time
        else:
            self.timer_mode = "work"
            self.seconds_left = self.default_time
        
        # update the time on the clock immediately 
        minutes, seconds = divmod(self.seconds_left, 60)
        time_screen = f"{minutes:02d}:{seconds:02d}" #02d forces at least 2 ditis (e.g. turns 6:25 into 06:25)
        
        # add to screen
        self.timer.configure(text=time_screen)
        
        # keep the loop running again 
        self.last_tick = time.time() 
        self.after(10, self.countdown_loop)
        self._timer_id = self.after(1000, self.countdown_loop)