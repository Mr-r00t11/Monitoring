from tkinter import *
import json

class Window:
    pass

    def __init__(self, inter):
        self.b2 = ''
        self.b3 = ''
        self.b4 = ''
        self.b5 = ''
        self.interfaz = inter
        self.interfaz.geometry("400x138")
        self.interfaz.title("PySSH")
        self.interfaz.config(bg = 'floral white')

        self.name_1 = '148.250.107.71'
        self.name_2 = '148.250.107.72'
        self.name_3 = '148.250.108.71'
        self.name_4 = '148.250.108.72'

        self.Create_Widgets()
        self.Read_Json()
        self.Uptime()
        self.Uptime_2()
        self.Uptime_3()
        self.Uptime_4()

        self.uptime.after(1000, self.Uptime)
        self.uptime_2.after(1000, self.Uptime_2)
        self.uptime_3.after(1000, self.Uptime_3)
        self.uptime_4.after(1000, self.Uptime_4)

    def Uptime(self):
        if self.b2 == 'Up':
            self.uptime = Label(self.interfaz, text='Up', fg='White', bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime.place(x=215, y=38, width=215, height=25)
            self.uptime.after(1000, self.Uptime)

        elif self.b2 == 'Down':
            self.uptime = Label(self.interfaz, text='Down', fg='White', bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime.place(x=215, y=38, width=215, height=25)
            self.uptime.after(1000, self.Uptime)
        self.Read_Json()

    def Uptime_2(self):
        if self.b3 == 'Up':
            self.uptime_2 = Label(self.interfaz, text='Up', fg='White', bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_2.place(x=215, y=63, width=215, height=25)
            self.uptime_2.after(1000, self.Uptime_2)
        
        elif self.b3 == 'Down':
            self.uptime_2 = Label(self.interfaz, text='Down', fg='White', bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_2.place(x=215, y=63, width=215, height=25)
            self.uptime_2.after(1000, self.Uptime_2)
        self.Read_Json()

    def Uptime_3(self):
        if self.b4 == 'Up':
            self.uptime_3 = Label(self.interfaz, text='Up', fg='White', bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_3.place(x=215, y=88, width=215, height=25)
            self.uptime_3.after(1000, self.Uptime_3)

        elif self.b4 == 'Down':
            self.uptime_3 = Label(self.interfaz, text='Down', fg='White', bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_3.place(x=215, y=88, width=215, height=25)
            self.uptime_3.after(1000, self.Uptime_3)
        self.Read_Json()

    def Uptime_4(self):
        if self.b5 == 'Up':
            self.uptime_4 = Label(self.interfaz, text='Up', fg='White', bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_4.place(x=215, y=113, width=215, height=25)
            self.uptime_4.after(1000, self.Uptime_4)

        elif self.b5 == 'Down':
            self.uptime_4 = Label(self.interfaz, text='Down', fg='White', bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_4.place(x=215, y=113, width=215, height=25)
            self.uptime_4.after(1000, self.Uptime_4)
        self.Read_Json()

    def Create_Widgets(self):
        self.etiqueta = Label(self.interfaz, text='Wall-Mart', fg='black',
            bg='papaya whip', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta.pack(fill=BOTH)

        self.etiqueta1 = Label(self.interfaz, text=self.name_1, fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta1.place(x=0, y=38, width=215, height=25)

        self.etiqueta2 = Label(self.interfaz, text=self.name_2, fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta2.place(x=0, y=63, width=215, height=25)

        self.etiqueta3 = Label(self.interfaz, text=self.name_3, fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta3.place(x=0, y=88, width=215, height=25)
        
        self.etiqueta4 = Label(self.interfaz, text=self.name_4, fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta4.place(x=0, y=113, width=215, height=25)

    def Read_Json(self):
        with open("dicc.json", "r") as self.json_read:
            self.json_read = json.load(self.json_read)

            if self.json_read['Status_1'] == 'Up':
                self.b2 = 'Up'
            else:
                self.b2 = 'Down'

            if self.json_read['Status_2'] == 'Up':
                self.b3 = 'Up'
            else:
                self.b3 = 'Down'

            if self.json_read['Status_3'] == 'Up':
                self.b4 = 'Up'
            else:
                self.b4 = 'Down'

            if self.json_read['Status_4'] == 'Up':
                self.b5 = 'Up'
            else:
                self.b5 = 'Down'
        pass

if __name__ == '__main__':        
    obj = Window(Tk())
    obj.interfaz.mainloop()
