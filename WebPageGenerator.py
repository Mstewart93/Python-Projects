import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) ,pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def get_data():
        label.config(text = entry.get())
    entry = Entry( width=42)
    entry.place()
    label= Label(text="")
    label.pack()

    #ttk.button(win, text= "Custom Html Page", command = get_data).place()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


#steps to add
    #Accept User input
    #store the input
    #two buttons
        #default HTML Page
        #Custom HTML Page
    #When custon is clicked have the window pop up with the users input as the body text for the
    #webpage
    
