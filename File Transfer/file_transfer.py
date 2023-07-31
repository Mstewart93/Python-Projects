import tkinter as tk
from tkinter import*
import tkinter.filedialog
import os
import shutil
import time
import datetime


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of the Graphical User Interface (GUI)
        self.master.title("File Transfer")



        #up to here creates a blank window that we can then create a widget from

        #lets create a button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir) #adds command and function from below.
        #lets position the source button in the GUI using the tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #lets now create an entry for source directory selection
        self.source_dir = Entry(width=75)
        #lest position entry in the GUI using the fridt so its the same as the button to
                                #ensure they will line up.

        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))
        #lets create a button to select the destinion of files from destination directory
        self.destDir_btn = Button(text = "Select Destination", width=20, command = self.destDir)
        #Next we position the button in the GUI using tkinter grid making sure its below the precious
        self.destDir_btn.grid(row=1, column = 0, padx=(20,10), pady=(15, 10))

        #create entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #ensure the etry pady and padx are the same so that they will line up right.
        self.destination_dir.grid(row=1, column = 1, columnspan=2, padx=(20,10), pady=(15,10))

        #creates a button to transfer files
        self.transfer_btn = Button ( text ="Transfer Files", width=20, command=self.transferFiles)
        #position it
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #create the exit button
        self.exit_btn = Button(text="Exit", width = 20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0, 15))


#creates a function to allow you to select a source on clicking the button
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the delete(0, end) will clear the content that is inserted in the entry eidget, allowing
        #the path to be inserted into the entry  widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    
        
#create a function to select destination in the directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)

#creates the function to actually  transfer files from one directory to another
    def transferFiles(self):
        day = 24*60*60
        now = time.time()
        past = now - day 
        file_time = os.path.getmtime(source_file)
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory

        for i in os.listdir(self.source_dir.get()):
            source_file = os.path.join(source ,  i)
            destination_file = os.path.join(destination ,  i)
            if file_time < past: 

                shutil.move(source_file, destination_file)
                print(i + ' was successfully transferred.')

#creates function to exit program
    def exit_program(self):
         root.destroy()
        #root is the main GUI window, the Tkinter destroy method
        #teslls python to terminate root.mainloop and ll idgets inside the GUI window
        
                        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
