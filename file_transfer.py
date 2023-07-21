import tkinter as tk
from tkinter import *
import tkinter.filedialog

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of the Graphical User Interface (GUI)
        self.master.title("File Transfer")
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
#the .delete(0, END) will clear the content that is inserted in the entry.
#this allows the path to be inserted into the entry properly.
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source direct Entry
        self.source_dir.insert(0, selectSourceDir)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

#up to here creates a blank window that we can then create a widget from

#lets create a button to select files from source directory
self.sourceDir_btn = Button(text="Select Source", width=20)
#lets position the source button in the GUI using the tkinter grid()
self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

#lets now create an entry for source directory selection
self.source_dir = Entry(width=75)
#lest position entry in the GUI using the fridt so its the same as the button to
                        #ensure they will line up.

self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))


                        
