from tkinter import *

class Disappear:
    def __init__(self):
        self.window = Tk()
        self.text_box = Text(height=20, width=40)
        self.text_box.grid(column=0, row=1, columnspan=3)
        title_text = Label(text="Disappearing Text!")
        title_text.grid(column=0, row=0, columnspan=3)
        title_text = Label(text="Keep typing or else it'll go away!")
        title_text.grid(column=0, row=2, columnspan=3)
        self.total = 1
        self.disappear()
        self.window.mainloop()


    def disappear(self):
        #set variable for length of text
        length_of_text = len(self.text_box.get('1.0', END))
        #If user has typed more than the last total
        if self.total < length_of_text:
            self.total = length_of_text
        else:
            #If not we set the total back to 1 and delete whats in the box
            self.total = 1
            self.text_box.delete('1.0', END)
            #Re run self every 5 seconds
        self.window.after(5000, self.disappear)

app = Disappear()


