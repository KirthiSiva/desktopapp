import customtkinter as ctk  
import tkinter.font as tkfont
import json # for file storage 
import os # also for file storage 

class ToDoList(ctk.CTkScrollableFrame):
    def __init__(self, master, fractal, width = 200, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, scrollbar_fg_color = None, scrollbar_button_color = None, scrollbar_button_hover_color = None, label_fg_color = None, label_text_color = None, label_text = "", label_font = None, label_anchor = "center", orientation = "vertical"):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, scrollbar_fg_color, scrollbar_button_color, scrollbar_button_hover_color, label_fg_color, label_text_color, label_text, label_font, label_anchor, orientation)
       
        # add the fractal here 
        self.fractal = fractal 
       
        # create a grid for the checkboxes 
        self.grid_columnconfigure(0, weight = 1)
       
        # declare some variables for the checkboxes (to-do "items")
        self.checkboxes = []
        
        # create a "strike through" font when it is completed
        base_font = ("Google Sans Flex", 20, "normal")
        self.stc = ctk.CTkFont(family=base_font[0], size=base_font[1], overstrike=True)
        
        # create a label for the to do list 
        self.header = ctk.CTkLabel(master, text = "📝 To - Do", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.header.grid(row = 0, column = 2, sticky = "sw", padx = 180)
        
        # create a button on the to do list 
        self.button = ctk.CTkButton(master, text = "Add Items", font = ("Google Sans Flex", 18, "normal"), corner_radius = 100, text_color = "white", fg_color="black", bg_color="transparent", command = self.button_pressed, hover_color="gray")
        self.button.grid(row = 0, column = 2, sticky = "se", padx = 150, pady = 7)

        # load from JSON
        self.load_to_do()
    
    # function to form a dictionary of all the current items 
    # this is convient for constantly reprinting the list of to_do items! 
    def dict_sort(self): 
        # clear the current used dict 
        all_to_do = {}
        
        for _ in self.checkboxes: 
            if _.get() == 1: # if the checkbox is filled 
                all_to_do[_] = True 
            else:
               all_to_do[_] = False 
            _.grid_forget()
        
        return all_to_do
            
    # function used to count number of completed items in the to-do list
    def get(self): 
        checked_counter = 0
        for _ in self.checkboxes: 
            if _.get() == 1: # if the checkbox is filled 
                checked_counter += 1

        # return the value for the "on_completed" function 
        return checked_counter
            
    # this function will run when the checkbox is clicked
    # DIRECTLY updates fractal tree! 
    def on_completed(self): 
        #1: refresh the list 
        # the way that I want to achieve this is to add to a dictionary
        # a: dictionary used to diffrienciate between complete and incomplete tasks
        dict_to_sort = self.dict_sort() 
        
        # clear the checkboxes stuff now 
        self.checkboxes = []
        
        #b: create a counter for printing it (to know the row #)
        count = 0 
        
        # c: create a for loop to add the incomplete items 
        for i, j in dict_to_sort.items(): 
            if j == False: 
                i.grid(row=count, column=0, padx=10, pady=(10, 0), sticky="w")
                i.configure(text_color = "white", font = ("Google Sans Flex", 20, "bold")) 
                self.checkboxes.append(i)
                count += 1
        
        # d: do the same thing for complete
        for i, j in dict_to_sort.items(): 
            if j == True: 
                i.grid(row=count, column=0, padx=10, pady=(10, 0), sticky="w")
                i.configure(text_color = "gray", font = self.stc)
                self.checkboxes.append(i)
                count += 1
        
        #update the fractal 
        self.fractal.update_progress(
            self.get(),
            self.return_total()
        )
        
        # save to the JSON
        self.save_to_do()
    
    # function to return the total length of the checkboxes (how many there are total)
    def return_total(self): 
        return len(self.checkboxes)
    
    # function for when the "add" button is clicked (open the input)
    def button_pressed(self): 
        #1: Create the dialogue box to get user input 
        # put this all in a loop so that it does not move on until it is done/not a dupe!  
        while True:
            # Create a variable to save state of dupe, and if it's empty 
            isDupe = False
            isEmpty = True
            
            dialog =  ctk.CTkInputDialog(text = "Enter a new goal! *cannot add duplicates!*", title = "New To-Do List Item")
            raw_input = dialog.get_input()

            # Give the user a pathway to leave (Cancel button or x)
            if raw_input != None: 
                user_input = raw_input.strip() # strip to get rid of white space
            else: 
                return # break out of the function 
            
            #2: Make sure this is not a duplicate 
            for _ in self.checkboxes: 
                if _.cget("text") == user_input: 
                    isDupe = True 
                    break
            
            #3: Make sure it is not empty 
            if user_input != "": 
                isEmpty = False
            
            if not isDupe and not isEmpty: 
                break
        
        #4: Now that it is good, add it to the list! 
        index_to_add = len(self.checkboxes)
        
        new_item = ctk.CTkCheckBox(self, text = user_input, font = ("Google Sans Flex", 18, "bold"), text_color = "white", command = self.on_completed, checkmark_color="black", fg_color= "white", hover_color="white")
        self.checkboxes.insert(0, new_item) # this is done so that it actually adds to the TOP, not the bottom! 
        self.on_completed() # call on_completed() so that it refreshes for me!
        
        # add to fractal 
        self.fractal.update_progress(
            self.get(),
            self.return_total()
        )
        
    
    # FILE STORAGE: 
    # There are 2 different functions needed: save, load
    def save_to_do(self): 
        todo_data = [] # empty list to hold everything 
        
        # use a for loop to add everything 
        for _ in self.checkboxes: 
            todo_data.append({
                "text": _.cget("text"),
                "completed": bool(_.get()) # get() gives the status of if its clicked or not, and the bool changes it from "1" to True!
            })
            
        # save it to the json
        # I am saving it with os path to make it cross compatible 
        save_path = os.path.join("saves", "to_do.json")
        with open(save_path, "w") as f: 
            json.dump(todo_data, f, indent = 4)
            
    # create a load function 
    def load_to_do(self):
        save_path = os.path.join("saves", "to_do.json")
        
        # In case the file is not found, make it 
        if not os.path.exists(save_path): 
            # use a try and except in case it fails to make the file 
            try: 
                # write in the file to make it 
                # same logic as java!
                with open(save_path, "w") as f: 
                    json.dump([], f, indent = 4)
                    
            except Exception: 
                return # if it still fails then just exit the function
        
        # now, read from the file 
        try: 
            # use read instead of write ("w")
            # load in all the data
            with open(save_path, "r") as f:
                todo_data = json.load(f)
                
            # use a for loop to add all the items back
            for item in todo_data:     
                new_item = ctk.CTkCheckBox(self, text  = item["text"], font=("Google Sans Flex", 18, "bold"), text_color="white", command=self.on_completed, checkmark_color="black", fg_color="white", hover_color="white")
                
                # set them as selected or deselected
                # (the checkboxes)
                if item["completed"]: 
                    new_item.select()
                else: 
                    new_item.deselect()
                
                # add this back to the list now 
                self.checkboxes.append(new_item)
                
            self.on_completed() # refresh the list
            
        except Exception: 
            return # if this doesnt work return