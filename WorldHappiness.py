from tkinter import Tk, Menu
from tkinter import messagebox as msg


def aboutmenu():
    msg.showinfo("ABOUT", "WORLD HAPPINESS REPORT\nVERSION 1.0")

def helpmenu():
    msg.showinfo("HELP", "INSERT A WORLD HAPPINESS REPORT")

class WorldHappiness():
    def __init__(self, master):
        self.master = master
        self.master.title("World Happiness")
        self.master.geometry("250x200")
        self.master.resizable(False, False)
        self.filename = ""
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv", accelerator='Ctrl+O', command=self.insertcsv)
        self.file_menu.add_command(label="Close File", accelerator="Ctrl+F4", command=self.closefile)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

    
    def insertcsv(self):
        pass

    def closefile(self):
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE TO CLOSE")
        else:
            self.filename = ""
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")

    def exitmenu(self):
        """ Exit function"""
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    

    


        

def main():
    """menu function"""
    root = Tk()
    WorldHappiness(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
