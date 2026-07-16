import customtkinter as ctk 

app = ctk.CTk() 
app.title("Dashboard 3000")
# used to make it maximize to show task bar and nothing else 
# how does this work on mac? 
app.after(0, lambda: app.state('zoomed'))

app.mainloop()