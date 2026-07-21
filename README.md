# Monochromia - Smart Dashboard with the most simple, minimalistic UI 

**DISCLAIMER:** This app requires at least a 1920x1080 screen, and it is only tested for Windows! 

--- 

## About: 
![Monochromia Dashboard](https://github.com/user-attachments/assets/d769a262-df02-408b-bb4e-a70de758368d)

Monochromia is a smart dashboard which is designed to stay on your desktop! It utilizes a monochrome theme utilizing CustomTkinter to stay clean and sleek. The dashboard is highly conveient, working easily out of the box, only requiring you to download some python libraries! 

## How to run: 
To run the application, download the .zip file, unzip, then launch main.py using Python! 

Required libraries: 
- Many libraries are required for this application because of all the widgets that are being used
- List of all the libraries that do NOT come preinstalled into python:
    - customtkinter 
    - pillow
    - psutil

### How to install: 
```
pip install customtkinter pillow psutil
``` 

--- 

## Features of Monochromia: 
Monochromia is filled with many widgets to make sure that it stays functional and relevant. 

### To-do List
- Allows you to add, and complete tasks! 
- Upon completing tasks, they will be sent to the bottom of the list, and be striken through! 

### "Quick Start" Tab Hub 
- Allows you to add up to 6 URLs that can instantly open at the click of a button! 
- Links fully customizable by clicking the buttons at the top! 

### Local Storage System using JSONs 
- Any changes made to the To Do List or Quick launch are instantly autosaved if any changes occur, leading to no progress lost when the app closes! 
- When opening the program, the states of the items within the To Do List, and all the links will restore on the UI 

### Fractal Tree Visualizer 
- Fractal tree visualizer to showcase % of tasks complete on the To Do List! 
- When you complete tasks, it expands, and when you add more, it retracts! 
- Dynamically updates live to showcase progress! 

<img width="404" height="228" alt="fractal_demo" src="https://github.com/user-attachments/assets/e683bef0-a28a-48c9-ba01-2782b30065e4" />

### Quote Generator
- Utilizes Zenquotes keyless free public API to constantly bring new quotes to the dashboard! 

### Automatic Weather API 
- Utilizes GeoJS and Open Meteo free keyless public APIs to instantly detect location via IP Address, and display current weather of your location! 

### Live Date and Clock
- Utilizes Python's `time` library to display the live time, and date!
- Time can swap between 24 hour format, and 12 hour format! 

### PC Info
- On Desktop, shows the PC Name, and OS version! 
- On Laptop, shows those, as well as battery information! 

### Pomodoro Timer
- Creates a loop to simulate the Pomodoro Timer! 
- Starts with a 25 minute timer, then a 5 minute timer for break, and repeats! 
- Includes a "Start" and "Stop" button! 

### RAM/CPU Performance Checker
- Utilizes the `psutil` library to showcase realtime CPU and RAM usage percentages!
