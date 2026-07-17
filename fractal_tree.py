#libraries to inport 
# The reason why I chose a fractal for the "growth" is to add a cool touch to the entire project! 
import customtkinter as ctk 
import math # for pi to create the radial fractal pattern! 

class Fractal(ctk.CTkCanvas): 
    # custom constrictor for this 
    def __init__(self, master, width=1920, height=1080):
        super().__init__(master,width=width,height=height,bg="#242424",highlightthickness=0)
        
        # declare sme of the variables 
        self.width = width
        self.height = height 
        
        # current completion progress placeholder 
        self.progress = 0 
        
        # draw the initial (empty) fractal 
        self.draw_fractal() 
        
    # this is the function which will actually be updating how extended/retracted the pattenr will be 
    def update_progress(self, completed, total): 
        # make sure the current total is not 0 
        if total == 0: 
            self.progress = 0
        else: 
            self.progress = completed / total 
            
        # draw the fractal now thats it upgraded
        self.draw_fractal()
            
    # the hard part, actually drawing the fractal! 
    def draw_fractal(self): 
        # clear just in case there was a previous drawing 
        self.delete("all")
                
        # define the center x and y coordinates 
        center_x = self.width / 2 
        center_y = self.height / 2
        
        # ignore if there is no progress (exit the function)
        if self.progress == 0: 
            return 
        
        # control how far the fractal extends based on the fraction
        # the reason why I added 80 initially is because of the fact that it is hidden behind the clock
        # because of that, it needs a bit of a "head start"
        length = 80 + (400 * self.progress)
        
        # depth is basically how many different "branching offs" are going to happen
        # what I mean by this is how many times the thing branches off from hte origin point
        # so something with a depth of 4 would branch of 4 times, then stay as it 
        depth = 5 
        
        # branches are the number of main branches that stem from the origin point!
        branches = 16
        
        # create a for loop to find the perfect angle for the branches to leave where it is equal everywhere!
        for i in range(branches): 
            """
                mathematical reasoning behind this. 
                - 2pi is the circumfrance of a circle in radians 
                - dividing it by branches gives you the amount of "circumfrance gap" 
                  between all the different branches! 
                - multiply by i to make it unique for each branch! 
                - if it is the first branch (i = 0), the angle will be 0 degrees
                    - if it is the second branch (i = 1), it will be pi/4 rad! 
            """
            
            angle = (2 * math.pi / branches) * i 
            
            # now create a function to draw each branch! 
            self.draw_branch(center_x, center_y, length, angle, depth)
    
    # this function is to actually draw the branch after defining the fractal!
    # Use the variables made in the previous step 
    def draw_branch(self, x, y, length, angle, depth): 
        # first, make sure depth is not 0 
        if depth == 0: 
            return # if it was 0, then it would just extend from the same spot forever
        
        # using the angle, calculate the new x and y after it branches off (new coordinate)
        # in this formula, it actually uses trigonometry to find the end point, which is away from the start from exactly the hyp's length!
        x2 = x + math.cos(angle) * length
        y2 = y + math.sin(angle) * length
        
        # now, draw the actual line (hyp OR the branch) between them! 
        # create line is a function directly in tkinter which does this for me
        self.create_line(x, y, x2, y2, fill = "white", width = max(1, depth // 2))
        
        # recur this function (from each branch, stem twice!)
        # reducing length because I want to SEE the pattern
        # if you do not reduce length by the second loop it will be completely 
        # off the screen. 
        self.draw_branch(x2, y2, length * 0.55, angle+ math.pi / 6, depth - 1)
        self.draw_branch(x2, y2, length * 0.55, angle- math.pi / 6, depth - 1)