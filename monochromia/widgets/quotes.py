# this is the widget which will display quotes from an API!  
# This will be done very similarily to the weather API, as I will be using the same libararies
# 
import urllib.request
import json
import threading
import customtkinter as ctk

class QuoteGen(ctk.CTkFrame):
    def __init__(self, master, width = 400, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # define a grid (only 1 text, quote! super simple)
        self.grid_columnconfigure(0, weight = 1, uniform="hello")
        self.grid_rowconfigure(0, weight = 1, uniform="hello")
        self.grid_propagate(False)
        
        # create a label for the window 
        self.lbl = ctk.CTkLabel(master, text = "📜 Quotes", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 2, column = 2, sticky = "nw", padx = 230, pady = 15)
        
        # create a label placeholder for the quotes 
        # I also want the quote to "wrap around", so I will be using a property of CTkLabels called "wraplength"
        # "justify = left" basically just forces all the text to "spawn" from the left
        self.quote_msg = ctk.CTkLabel(self, text = "Loading Quote...", font = ("Google Sans Flex", 25, "italic"), text_color = "white", fg_color="transparent", bg_color="transparent", wraplength = 450, justify = "left")
        self.quote_msg.grid(row = 0, column = 0, sticky = "n", pady = 25)
        
        # create the thread again 
        threading.Thread(target=self.fetch_quotes, daemon=True).start()
    
    # function that will actually get teh quotes using an API 
    # The api that I will be using is zenquotes, a keyless API that is free and public 
    def fetch_quotes(self): 
        try: 
            url = "https://zenquotes.io/api/random"
            quote_req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

            # now just read through the data the same way as the weather! 
            with urllib.request.urlopen(quote_req) as response: 
                data = json.loads(response.read().decode())
                
                # get the quote data 
                quote_data = data[0]
                quote = quote_data["q"]
                author = quote_data["a"]
            
            # format then send to setter method 
            full_quote = f'"{quote}"\n- {author}'
            self.set_quote(full_quote)
            
        except Exception: 
            pass

    # setter method to set the quote text! 
    def set_quote(self, quote): 
        self.quote_msg.configure(text = quote)