from tkinter import *
import functions

# test

class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("BASE 2 BASE")
        self.pack(fill=BOTH, expand=1)
        ShowButton = Button(self,text="Calculate",command=self.client_show)
        ShowButton.place(x=150,y=80)

        label1 = Label(self,text = "Input value")
        label1.place(x=0, y=10)

        self.e1 = Entry(self)
        self.e1.place(x=90,y=10)

        self.tkvar1 = StringVar(self)
        choices1 = []
        for i in range(2,37):
            choices1.append(str(i))
        self.tkvar1.set("2")

        bases1 = OptionMenu(self,self.tkvar1,*choices1)
        bases1.place(x=250,y=5)

        label2 = Label(self, text="Output value")
        label2.place(x=0, y=45)


        self.outputval ="OUTPUT"

        self.e2 = Label(self,text = self.outputval)
        self.e2.place(x=90,y=45)

        self.tkvar2 = StringVar(self)
        self.tkvar2.set("2")

        choices2 = []
        for i in range(2, 37):
            choices2.append(str(i))

        bases2 = OptionMenu(self, self.tkvar2, *choices2)
        bases2.place(x=250, y=40)


    def client_show(self):
        base1 = int(self.tkvar1.get())
        base2 = int(self.tkvar2.get())
        usrinput = (self.e1.get())
        output = functions.dec_to_base(functions.base_to_dec(usrinput, base1), base2)
        print(output)

        self.e2['text'] = output

root = Tk()
root.geometry("320x120")
app = Window(root)
root.mainloop()

