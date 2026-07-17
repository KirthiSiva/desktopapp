from pathlib import Path 
import customtkinter as ctk 
from PIL import Image
import urllib.request
import json

DIR_OF_FILE = Path(__file__).resolve().parent

PC_DARK = DIR_OF_FILE / "assets" / "pc_dark.png"
PC_LIGHT = DIR_OF_FILE /  "assets" / "pc_light.png"
LAP_LIGHT = DIR_OF_FILE / "assets" / "lap_light.png"
LAP_DARK = DIR_OF_FILE / "assets" / "lap_dark.png"

app = ctk.CTk() 

print(PC_LIGHT)

# define the grid 
app.columnconfigure((0, 1, 2), weight=1, uniform="hello")
app.rowconfigure((0, 1, 2), weight=1, uniform="hello")

# Detect the user profile name, and set that as the app title  
name = "hi"
app.title(f"Welcome, {name}!") # use the "getpass" library to get the username of the device 

# maximize the screen 
app.after(0, lambda: app.state('zoomed'))

# set a minimum size that the screen can be 
app.minsize(1368, 768)


location_req = urllib.request.Request("https://get.geojs.io/v1/ip/geo.json", headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(location_req) as response: 
    geo_data = json.loads(response.read().decode())
    city = geo_data["city"]
print(city)

my_image = ctk.CTkImage(light_image=Image.open(PC_LIGHT), dark_image=Image.open(PC_DARK), size = (90, 115))
img_lbl = ctk.CTkLabel(app, image=my_image, text="", fg_color="transparent", bg_color="transparent")
img_lbl.grid(row = 1, column = 1)

# start the main loop 
app.mainloop()