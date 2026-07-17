# this class is here for the automatic tab open slot.
# i will be using hte "web browser" module for this to work 
# i will also be using a json to SAVE the data from the web opener 
import webbrowser
import customtkinter as ctk 

# create a class for the buttons holding the url 
# why a new class: I want to be able to store the url on the backend, and a class would allow me to have back-end properties.
# this is something I learned through java, and I want to see if it works the same way here! It should
class SiteTab(ctk.CTkButton):
    # at the end, add "url" property to hold it 
    def __init__(self, master, width = 140, height = 35, corner_radius = None, border_width = None, border_spacing = 2, bg_color = "transparent", fg_color = None, hover_color = None, border_color = None, text_color = None, text_color_disabled = None, background_corner_colors = None, round_width_to_even_numbers = True, round_height_to_even_numbers = True, text = "CTkButton", font = None, textvariable = None, image = None, state = "normal", hover = True, command = None, compound = "left", anchor = "center", url = "", **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, border_spacing, bg_color, fg_color, hover_color, border_color, text_color, text_color_disabled, background_corner_colors, round_width_to_even_numbers, round_height_to_even_numbers, text=text, font=font, textvariable=textvariable, image=image, state=state, hover=hover, command=self.on_click, compound=compound, anchor=anchor, **kwargs)

        # declare vars
        self.url = url 
        self.custom_command = command

        # Set the properties of it that I have used everywhere else
        self.configure(font = ("Google Sans Flex", 15, "bold"), corner_radius = 20, text_color = "white", fg_color="gray", bg_color="transparent", hover_color = "black", text = "Empty")
    
    # this function is used as a middleman to make sure that the edit function only has 1 argument
    def on_click(self):
        if self.custom_command is not None: 
            self.custom_command(self)
        
# this class is for the buttons that will be held here. 
# These buttons will be used to edit the links of the tab
# set the urls as a deeper property of it that is not shown (unless using the window)
class AutoTabOpen(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 50, corner_radius = 100, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        # add a label 
        self.lbl = ctk.CTkLabel(master, text = "🚀 Quick Start", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 0, column = 1, sticky = "nw", padx = 120)

        # add a button that will instantly open up all the tabs 
        self.open_button = ctk.CTkButton(master, text = "Launch!", font = ("Google Sans Flex", 18, "normal"), corner_radius = 100, text_color = "white", fg_color="black", bg_color="transparent", command = self.open_all_pressed, hover_color="gray")
        self.open_button.grid(row = 0, column = 1, sticky = "ne", padx = 130, pady = 10)
        
        # create the grid system for this so that all the buttons look good 
        # make sure to set propogate grid as False this time so that it does not disappear 
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="hello")
        self.grid_rowconfigure(0,weight =1, uniform="hello")
        self.grid_propagate(False)
        
        # Make the 6 buttons that will hold the links of their choice 
        self.btn_1 = SiteTab(self, command = self.edit)
        self.btn_2 = SiteTab(self, command = self.edit)
        self.btn_3 = SiteTab(self, command = self.edit)
        self.btn_4 = SiteTab(self, command = self.edit)
        self.btn_5 = SiteTab(self, command = self.edit)
        self.btn_6 = SiteTab(self, command = self.edit)
        
        # set them up in the grid 
        self.btn_1.grid(row = 0, column = 0)
        self.btn_2.grid(row = 0, column = 1)
        self.btn_3.grid(row = 0, column = 2)
        self.btn_4.grid(row = 0, column = 3)
        self.btn_5.grid(row = 0, column = 4)
        self.btn_6.grid(row = 0, column = 5)
        
    # edit function works for all the buttons since the code is equivalent 
    def edit(self, button): 
        #1: get the url the button is currently holding (it is FINE if it is empty right now)
        current_url = button.url
        if current_url == None: 
            current_url = ""
        
        #2: open an input dialgue when the button is clicked to add a new link 
        # I am intentially not adding any "checks" or verifying anything because it does not matter for this
        # The user is allowed to do anything they want for this
        dialog =  ctk.CTkInputDialog(text = "Enter in a new link!", title = "Setting up YOUR links!")
        
        #3: get the user input, and set that as the new url! 
        # make sure this only happens if they click ok, so void results from clicking cancel or the x. 
        user_input = dialog.get_input()
        if user_input != None: 
            button.url = user_input.strip()
            
        #4: edit the button to show that the new url is there! 
        if user_input: 
            # this removes everything around the link (e.g. www.youtube.ca/fusdohf3498fds --> youtube.ca)
            # the "split" removes everything after the next period to leave a "clean" url
            link = user_input.replace("https://", "").replace("http://", "").replace("www.", "").split(".")[0] 
            button.configure(text = link.capitalize()) 
        else: 
            button.configure(text = "Empty")
        
    # this function is used to actually open everything in your browser. 
    # extremely simple, just open them all using the "webbrowser" library
    def open_all_pressed(self):
        webbrowser.open(f"{self.btn_1.url}") 
        webbrowser.open(f"{self.btn_2.url}") 
        webbrowser.open(f"{self.btn_3.url}") 
        webbrowser.open(f"{self.btn_4.url}") 
        webbrowser.open(f"{self.btn_5.url}") 
        webbrowser.open(f"{self.btn_6.url}") 