import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) ,pady=(10,10),row=2, column=1)
        self.custom = Button(self.master, text="Custon HTML Page", width=30, height=2 )
        self.custom.grid(padx=(10,10), pady=(10,10), row=2, column=2, command = self.get_data)
        entry = tk.Entry(root,textvariable = custom_html, font=('calibre',10,'normal'))
        custom_html.grid(row=1,column=1)

        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = get_data()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(get_data())
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def get_data():
        label.config(text = entry.get())
        entry = Entry( width=42)
        entry.place()
        label= Label(text="")
        label.pack()




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
   
 
        

   

