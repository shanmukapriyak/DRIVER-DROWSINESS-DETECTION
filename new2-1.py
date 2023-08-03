
# Import Library
from tkinter import *
import os
from tkinter.filedialog import askopenfilename 
from new2 import running
# Create Object 
root = Tk() 
root.geometry("500x350")

  
def open_file(): 
    running()
    Button(root, text ='Open', 
       command = open_file).pack(side = TOP, 
                                 pady = 10) 
  
# Execute Tkinter
root.mainloop()