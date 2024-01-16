#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as Tkinter 
from datetime import datetime 
counter = 66600 
running = False 
def counter_label(label): 
    def count(): 
        if running: 
            global counter 
            # To manage up the initial delay. 
            if counter==66600:            
                display="Starting..." 
            else: 
                tt = datetime.fromtimestamp(counter) 
                strings = tt.strftime("%H:%M:%S") 
                display=strings 
            label['text']=display # Or label.config(text=display) 
            # Label.after(arg1, arg2) executes the function  specified as the second parameter after delaying by the first argument's millisecond value. 
# In situations like these, we typically need to repeatedly call the # function where it is present. 
# Recount calls after 1000 millisecond delays, or 1 second. 
            label.after(1000, count) 
            counter += 1 
    # Triggering up of the start of the counter. 
    count()  
# starting function of the stopwatch 
def Start(label): 
    global running 
    running=True 
    counter_label(label) 
    start['state']='disabled' 
    stop['state']='normal' 
    reset['state']='normal' 
# Stopping of function of the stopwatch 
def Stop(): 
    global running 
    start['state']='normal' 
    stop['state']='disabled' 
    reset['state']='normal' 
    running = False 
# Resetting function of the stopwatch in code 
def Reset(label): 
    global counter 
    counter=68600 
 
    # if stop is pressed first, then rest. 
    if running==False:   
        reset['state']='disabled' 
        label['text']='Welcome!' 
 
    # if the stopwatch is starting when the reset button is clicked. 
    else:            
        label['text']='Starting...' 
root = Tkinter.Tk() 
root.title("Stopwatch_inter") 
# Fixing up the window size. 
root.minsize(width=260, height=80) 
label = Tkinter.Label(root, text="Welcome", fg="black", font="Verdana 35 bold") 
label.pack() 
f = Tkinter.Frame(root) 
start = Tkinter.Button(f, text='Start up', width=8, command=lambda:Start(label)) 
stop = Tkinter.Button(f, text='Stop in',width=8,state='disabled', command=Stop) 
reset = Tkinter.Button(f, text='Reset at',width=8, state='disabled', command=lambda:Reset(label)) 
f.pack(anchor = 'center',pady=6) 
start.pack(side="left") 
stop.pack(side ="left") 
reset.pack(side="left") 
root.mainloop() 


# In[ ]:




