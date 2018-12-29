
# =============================================================================
# Importing the libraries
# =============================================================================

import tkinter as tk 
import tkinter.ttk as ttk
import pandas as pd
import datetime as dt

# =============================================================================
# Code to run after hitting run button
# =============================================================================

def values(): 
    
    # increment progressbar 
    #setting progress bar to 5%
    pb.step(5)
    style.configure('text.Horizontal.TProgressbar', 
                    text='{:g} %'.format(5))  # update label
       
    #our 1st input variable
    global startDate 
    startDate = str(entry1.get()) 
    
    #our 2nd input variable
    global endDate 
    endDate = str(entry2.get()) 
    
    # =============================================================================
    # add you code logic after this line which wull use startDate & endDate
    # =============================================================================
     
   #setting progress bar to 50%
    pb.step(45)
    style.configure('text.Horizontal.TProgressbar', 
                    text='{:g} %'.format(50))  # update label
         
    output  = "Start Date --> " + str(startDate) + " End Date -->" + str(endDate)
    outputLabel = tk.Label(root, text= output, bg='orange')
    canvas1.create_window(260, 280, window=outputLabel)

   #setting progress bar to 100%
    pb.step(49)  #using 1point less to show complete fill
    style.configure('text.Horizontal.TProgressbar', 
                    text='{:g} %'.format(100))  # update label
    
# =============================================================================
# tkinter GUI
# =============================================================================
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# with sklearn
text1 = "Pricing Tool"
label_Intercept = tk.Label(root, text=text1, justify = 'center',font=("Helvetica", 16,"bold"))
canvas1.create_window(260, 40, window=label_Intercept)

#### Start date label and input box
# Start date label
label1 = tk.Label(root, text='Type Start date (dd/mm/yyyy): ')
canvas1.create_window(113, 100, window=label1)

# Start date entry box
entry1 = tk.Entry (root) 
canvas1.create_window(270, 100, window=entry1)

#### End date label and input box
# End date label
label2 = tk.Label(root, text=' Type End date (dd/mm/yyyy): ')
canvas1.create_window(110, 130, window=label2)

# End date entry box
entry2 = tk.Entry (root)
canvas1.create_window(270, 130, window=entry2)

#Run Button
button1 = tk.Button (root, text='Run',command=values, bg='blue', fg='white') # button to call the 'values' command above 
canvas1.create_window(270, 160, window=button1)

#Adding progress bar
style = ttk.Style(root)

# add label in the layout
style.layout('text.Horizontal.TProgressbar', 
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}), 
              ('Horizontal.Progressbar.label', {'sticky': ''})])

# set initial text
style.configure('text.Horizontal.TProgressbar', text='0 %')
variable = tk.DoubleVar(root)

# Progress Bar
label2 = tk.Label(root, text=' Progress ')
canvas1.create_window(110, 200, window=label2)

pb=ttk.Progressbar(root,style='text.Horizontal.TProgressbar',length=100,maximum=100,mode='determinate',variable=variable)
canvas1.create_window(270, 200, window=pb)



# Calling tKinter app (this should be the last line of program)
root.mainloop()
