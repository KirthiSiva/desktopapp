# this is the widget which will hold the weather of the current location 
import customtkinter as ctk 
import urllib.request #used for the apis 
import json #This is required for reading the API 
import threading # this library is very important for running many processes at the same time 

class Weather(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # Create a grid
        self.rowconfigure(0, weight = 2, uniform="hello") # the reason why I made it 2 is because I want this to hold the icon, which will take a lot of space
        self.rowconfigure((1,2), weight = 1, uniform="hello")
        self.columnconfigure(0, weight= 1, uniform= "hello")
        self.grid_propagate(False)
        
        # create a label for the app 
        self.header = ctk.CTkLabel(master, text = "Weather 🌤️", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.header.grid(row = 0, column = 0, sticky = "ne",  pady = 15, padx = 180)
        
        # Create the labels for the weather and location (placeholders for now, will be changed via the API)
        self.lbl_weather = ctk.CTkLabel(self, text = "Loading Weather...", font = ("Google Sans Flex", 18, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl_weather.grid(row = 1, column = 0, sticky = "n")
        
        self.lbl_location = ctk.CTkLabel(self, text = "Loading Location...", font = ("Google Sans Flex", 18, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl_location.grid(row = 2, column = 0, sticky = "n")
        
        # Create a label that will hold the "icon" (will just be an emoji! )
        self.img = ctk.CTkLabel(self, text = "", font = ("Google Sans Flex", 60, "normal"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.img.grid(row = 0, column = 0)
        
        # Use the threading to run this in hte background so that it does not crash everything! 
        # put the threading on the processes that will fetch the data of the weather and location so it does not constantly crash
        # the "daemon" line makes it so that when the program closes, the thread closes too, so it won't keep running afterwards
        threading.Thread(target=self.fetch_location_weather, daemon=True).start()
        
    # this is the function which will hold the main stuff
    def fetch_location_weather(self): 
        # wrap the whole thing in a try and except incase the API does not work, or the user is not connected to Wi-Fi 
        # this will make it so that the entire program won't crash
        try:
            location_req = urllib.request.Request("https://get.geojs.io/v1/ip/geo.json", headers={'User-Agent': 'Mozilla/5.0'})
            
            # get the city from the data 
            with urllib.request.urlopen(location_req) as response: 
                geo_data = json.loads(response.read().decode())
                city = geo_data["city"]

                # also get lat and long for the weather! 
                lat = geo_data["latitude"]
                long = geo_data["longitude"]
            
            # edit the city var to make it more reader-friendly (add an emoji)
            city_add = f"📍 {city}"
            
            # do the same thing now for the weather! 
            # first, use an f-string to make the link using the lat and long found!
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
            weather_req = urllib.request.Request(weather_url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(weather_req) as response: 
                weather_data = json.loads(response.read().decode())
                current = weather_data["current_weather"] 
                temp_c = current["temperature"] # this is what I will actually be using
                
                # Now, using the weathercode, I will be able to diffrienciate what the weather actually is!
                code = current["weathercode"]
                if code in [1, 2, 3]: 
                    condition = "Cloudy"
                    emoji_icon = "☁️"
                elif code in [45, 48]: 
                    condition = "Foggy"
                    emoji_icon = "🌫️"
                elif code in [51, 53, 55, 61, 63, 65]: 
                    condition = "Rain"
                    emoji_icon = "🌧️"
                elif code in [71, 73, 75]: 
                    condition = "Snow"
                    emoji_icon = "❄️"
                elif code in [95, 96, 99]: 
                    condition = "Storm"
                    emoji_icon = "⛈️"
                else: 
                    condition = "Clear"
                    emoji_icon = "☀️"
            
            # create a weather var which formats everything correctly 
            weather = f"{temp_c}°C | {condition}"
            
            # the reason why I cannot simply use "configure" is because thsi is running on a seperate thread
            # if I did that, it would go back to the main threading, crashign everything.
            # evne though its "after", it only updates ONCE so it does not slow any performance. 
            self.after(0, self.update_ui, city_add, weather, emoji_icon)
        
        except Exception: 
            pass # No need to add anything because I already took care of it via the placeholders
      
    # this function is used as a setter method to change the location/weather 
    def update_ui(self, city, weather, emoji): 
        self.lbl_location.configure(text = city)  
        self.lbl_weather.configure(text = weather)
        self.img.configure(text = emoji)