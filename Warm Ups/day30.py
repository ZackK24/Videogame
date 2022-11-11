""" 
Using the two blocks of code below, create a window that creates a folder, and creates a file with content from the window.

"""
# https://automatetheboringstuff.com/2e/chapter9/

from pathlib import Path
import os
print(Path.cwd())
os.chdir('C:/github')


# using tkinter to create a usable window
#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

#Define a function to show a message
def myclick():
   message= "Your Folder "+ entry.get()
   label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
   os.makedirs('C:/github/' + entry.get())
   os.chdir('C:/github/' + entry.get())
   label.pack(pady=30)
   entry.delete(0, 'end')
   
   message1= "Your File " + entry1.get()
   label= Label(frame, text= message1, font= ('Times New Roman', 14, 'italic'))
   p = Path(entry1.get() + '.txt')
   entry1.delete(0, 'end')
   label.pack(pady=30)
    
   message2= "Your Content " + entry2.get()
   label= Label(frame, text= message2, font= ('Times New Roman', 14, 'italic'))
   p.write_text(str(entry2.get()))
   p.read_text()
   entry2.delete(0, 'end')
   label.pack(pady=30)


#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)
#Create an Entry widget in the Frame
entry = ttk.Entry(frame, width= 40)
entry1 = ttk.Entry(frame, width = 40)
entry2 = ttk.Entry(frame, width = 40)
entry1.insert(INSERT, "Create your folder...")
entry2.insert(INSERT, "Creat your file...")
entry.insert(INSERT, "Create your contents...")
entry.pack()
entry1.pack()
entry2.pack()
#Create a Button
ttk.Button(win, text= "Create", command= myclick).pack(pady=20)
win.mainloop()