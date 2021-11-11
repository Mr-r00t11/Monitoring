from tkinter import *
import json

class Window:
    pass

    def __init__(self, inter):
        self.c2 = ''
        self.c3 = ''
        self.c4 = ''
        self.c5 = ''
        self.c6 = ''
        self.c7 = ''
        self.c8 = ''
        self.c9 = ''
        self.c10 = ''
        self.c11 = ''
        self.c12 = ''
        self.c13 = ''
        self.c14 = ''
        self.c15 = ''
        self.c16 = ''

        self.output_1 = ''
        self.output_2 = ''
        self.output_3 = ''
        self.output_4 = ''
        self.output_5 = ''
        self.output_6 = ''
        self.output_7 = ''
        self.output_8 = ''
        self.output_9 = ''
        self.output_10 = ''
        self.output_11 = ''
        self.output_12 = ''
        self.output_13 = ''
        self.output_14 = ''
        self.output_15 = ''

        self.interfaz = inter
        self.interfaz.geometry("400x410")
        self.interfaz.title("PySSH")
        self.interfaz.config(bg = 'floral white')
        self.Create_Widgets()
        self.Uptime()
        self.Uptime_2()
        self.Uptime_3()
        self.Uptime_4()
        self.Uptime_5()
        self.Uptime_6()
        self.Uptime_7()
        self.Uptime_8()
        self.Uptime_9()
        self.Uptime_10()
        self.Uptime_11()
        self.Uptime_12()
        self.Uptime_13()
        self.Uptime_14()
        self.Uptime_15()
        self.uptime.after(1000, self.Uptime)
        self.uptime_2.after(1000, self.Uptime_2)
        self.uptime_3.after(1000, self.Uptime_3)
        self.uptime_4.after(1000, self.Uptime_4)
        self.uptime_5.after(1000, self.Uptime_5)
        self.uptime_6.after(1000, self.Uptime_6)
        self.uptime_7.after(1000, self.Uptime_7)
        self.uptime_8.after(1000, self.Uptime_8)
        self.uptime_9.after(1000, self.Uptime_9)
        self.uptime_10.after(1000, self.Uptime_10)
        self.uptime_11.after(1000, self.Uptime_11)
        self.uptime_12.after(1000, self.Uptime_12)
        self.uptime_13.after(1000, self.Uptime_13)
        self.uptime_14.after(1000, self.Uptime_14)
        self.uptime_15.after(1000, self.Uptime_15)

    def Uptime(self):
        if self.c2 == 'Up':
            self.uptime = Label(self.interfaz, text=self.output_1, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime.place(x=215, y=38, width=215, height=25)
            self.uptime.after(1000, self.Uptime)
        else:
            self.uptime = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime.place(x=215, y=38, width=215, height=25)
            self.uptime.after(1000, self.Uptime)
        self.Read_Json()

    def Uptime_2(self):
        if self.c3 == 'Up':
            self.uptime_2 = Label(self.interfaz, text=self.output_2, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_2.place(x=215, y=63, width=215, height=25)
            self.uptime_2.after(1000, self.Uptime_2)
        else:
            self.uptime_2 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_2.place(x=215, y=63, width=215, height=25)
            self.uptime_2.after(1000, self.Uptime_2)
        self.Read_Json()

    def Uptime_3(self):
        if self.c4 == 'Up':
            self.uptime_3 = Label(self.interfaz, text=self.output_3, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_3.place(x=215, y=88, width=215, height=25)
            self.uptime_3.after(1000, self.Uptime_3)
        else:
            self.uptime_3 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_3.place(x=215, y=88, width=215, height=25)
            self.uptime_3.after(1000, self.Uptime_3)
        self.Read_Json()

    def Uptime_4(self):
        if self.c5 == 'Up':
            self.uptime_4 = Label(self.interfaz, text=self.output_4, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_4.place(x=215, y=113, width=215, height=25)
            self.uptime_4.after(1000, self.Uptime_4)
        else:
            self.uptime_4 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_4.place(x=215, y=113, width=215, height=25)
            self.uptime_4.after(1000, self.Uptime_4)
        self.Read_Json()

    def Uptime_5(self):
        if self.c6 == 'Up':
            self.uptime_5 = Label(self.interfaz, text=self.output_5, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_5.place(x=215, y=138, width=215, height=25)
            self.uptime_5.after(1000, self.Uptime_5)
        else:
            self.uptime_5 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_5.place(x=215, y=138, width=215, height=25)
            self.uptime_5.after(1000, self.Uptime_5)
        self.Read_Json()

    def Uptime_6(self):
        if self.c7 == 'Up':
            self.uptime_6 = Label(self.interfaz, text=self.output_6, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_6.place(x=215, y=163, width=215, height=25)
            self.uptime_6.after(1000, self.Uptime_6)
        else:
            self.uptime_6 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_6.place(x=215, y=163, width=215, height=25)
            self.uptime_6.after(1000, self.Uptime_6)
        self.Read_Json()

    def Uptime_7(self):
        if self.c8 == 'Up':
            self.uptime_7 = Label(self.interfaz, text=self.output_7, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_7.place(x=215, y=188, width=215, height=25)
            self.uptime_7.after(1000, self.Uptime_7)
        else:
            self.uptime_7 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_7.place(x=215, y=188, width=215, height=25)
            self.uptime_7.after(1000, self.Uptime_7)
        self.Read_Json()

    def Uptime_8(self):
        if self.c9 == 'Up':
            self.uptime_8 = Label(self.interfaz, text=self.output_8, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_8.place(x=215, y=213, width=215, height=25)
            self.uptime_8.after(1000, self.Uptime_8)
        else:
            self.uptime_8 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_8.place(x=215, y=213, width=215, height=25)
            self.uptime_8.after(1000, self.Uptime_8)
        self.Read_Json()

    def Uptime_9(self):
        if self.c10 == 'Up':
            self.uptime_9 = Label(self.interfaz, text=self.output_9, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_9.place(x=215, y=238, width=215, height=25)
            self.uptime_9.after(1000, self.Uptime_9)
        else:
            self.uptime_9 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_9.place(x=215, y=238, width=215, height=25)
            self.uptime_9.after(1000, self.Uptime_9)
        self.Read_Json()

    def Uptime_10(self):
        if self.c11 == 'Up':
            self.uptime_10 = Label(self.interfaz, text=self.output_10, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_10.place(x=215, y=263, width=215, height=25)
            self.uptime_10.after(1000, self.Uptime_10)
        else:
            self.uptime_10 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_10.place(x=215, y=263, width=215, height=25)
            self.uptime_10.after(1000, self.Uptime_10)
        self.Read_Json()

    def Uptime_11(self):
        if self.c12 == 'Up':
            self.uptime_11 = Label(self.interfaz, text=self.output_11, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_11.place(x=215, y=288, width=215, height=25)
            self.uptime_11.after(1000, self.Uptime_11)
        else:
            self.uptime_11 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_11.place(x=215, y=288, width=215, height=25)
            self.uptime_11.after(1000, self.Uptime_11)
        self.Read_Json()

    def Uptime_12(self):
        if self.c13 == 'Up':
            self.uptime_12 = Label(self.interfaz, text=self.output_12, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_12.place(x=215, y=313, width=215, height=25)
            self.uptime_12.after(1000, self.Uptime_12)
        else:
            self.uptime_12 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_12.place(x=215, y=313, width=215, height=25)
            self.uptime_12.after(1000, self.Uptime_12)
        self.Read_Json()

    def Uptime_13(self):
        if self.c14 == 'Up':
            self.uptime_13 = Label(self.interfaz, text=self.output_13, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_13.place(x=215, y=338, width=215, height=25)
            self.uptime_13.after(1000, self.Uptime_13)
        else:
            self.uptime_13 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_13.place(x=215, y=338, width=215, height=25)
            self.uptime_13.after(1000, self.Uptime_13)
        self.Read_Json()

    def Uptime_14(self):
        if self.c15 == 'Up':
            self.uptime_14 = Label(self.interfaz, text=self.output_14, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_14.place(x=215, y=363, width=215, height=25)
            self.uptime_14.after(1000, self.Uptime_14)
        else:
            self.uptime_14 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_14.place(x=215, y=363, width=215, height=25)
            self.uptime_14.after(1000, self.Uptime_14)
        self.Read_Json()

    def Uptime_15(self):
        if self.c16 == 'Up':
            self.uptime_15 = Label(self.interfaz, text=self.output_15, fg='White',
                bg='green', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_15.place(x=215, y=388, width=215, height=25)
            self.uptime_15.after(1000, self.Uptime_15)
        else:
            self.uptime_15 = Label(self.interfaz, text='Down', fg='White',
                bg='red4', font=("Eras Demi ITC", 9, 'bold'))
            self.uptime_15.place(x=215, y=388, width=215, height=25)
            self.uptime_15.after(1000, self.Uptime_15)
        self.Read_Json()

    def Create_Widgets(self):
        self.etiqueta = Label(self.interfaz, text='ADO', fg='black',
            bg='papaya whip', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta.pack(fill=BOTH)

        self.etiqueta1 = Label(self.interfaz, text='ADOA1', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta1.place(x=0, y=38, width=215, height=25)

        self.etiqueta2 = Label(self.interfaz, text='ADOA2', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta2.place(x=0, y=63, width=215, height=25)

        self.etiqueta3 = Label(self.interfaz, text='ADOB', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta3.place(x=0, y=88, width=215, height=25)
        
        self.etiqueta4 = Label(self.interfaz, text='CBV', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta4.place(x=0, y=113, width=215, height=25)
        
        self.etiqueta5 = Label(self.interfaz, text='COV', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta5.place(x=0, y=138, width=215, height=25)

        self.etiqueta6 = Label(self.interfaz, text='CUN', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta6.place(x=0, y=163, width=215, height=25)

        self.etiqueta7 = Label(self.interfaz, text='EDO', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta7.place(x=0, y=188, width=215, height=25)

        self.etiqueta8 = Label(self.interfaz, text='MANAGER', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta8.place(x=0, y=213, width=215, height=25)
        
        self.etiqueta9 = Label(self.interfaz, text='GDL', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta9.place(x=0, y=238, width=215, height=25)

        self.etiqueta10 = Label(self.interfaz, text='JAV', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta10.place(x=0, y=263, width=215, height=25)

        self.etiqueta11 = Label(self.interfaz, text='MEY', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta11.place(x=0, y=288, width=215, height=25)

        self.etiqueta12 = Label(self.interfaz, text='OAO', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta12.place(x=0, y=313, width=215, height=25)

        self.etiqueta13 = Label(self.interfaz, text='PUP', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta13.place(x=0, y=338, width=215, height=25)

        self.etiqueta14 = Label(self.interfaz, text='TGC', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta14.place(x=0, y=363, width=215, height=25)

        self.etiqueta15 = Label(self.interfaz, text='VHT', fg='White',
            bg='sky blue', font=("Eras Demi ITC", 17, 'bold'))
        self.etiqueta15.place(x=0, y=388, width=215, height=25)

    def Read_Json(self):
        with open("dicc.json", "r") as self.json_read:
            self.json_read = json.load(self.json_read)

            if self.json_read['ADO1'] == 'Up':
                self.c2 = 'Up'
                self.output_1 = self.json_read['Status_1']
            else:
                self.c2 = 'Down'

            if self.json_read['ADO2'] == 'Up':
                self.c3 = 'Up'
                self.output_2 = self.json_read['Status_2']
            else:
                self.c3 = 'Down'

            if self.json_read['ADO3'] == 'Up':
                self.c4 = 'Up'
                self.output_3 = self.json_read['Status_3']
            else:
                self.c4 = 'Down'

            if self.json_read['ADO4'] == 'Up':
                self.c5 = 'Up'
                self.output_4 = self.json_read['Status_4']
            else:
                self.c5 = 'Down'
            
            if self.json_read['ADO5'] == 'Up':
                self.c6 = 'Up'
                self.output_5 = self.json_read['Status_5']
            else:
                self.c6 = 'Down'

            if self.json_read['ADO6'] == 'Up':
                self.c7 = 'Up'
                self.output_6 = self.json_read['Status_6']
            else:
                self.c7 = 'Down'

            if self.json_read['ADO7'] == 'Up':
                self.c8 = 'Up'
                self.output_7 = self.json_read['Status_7']
            else:
                self.c8 = 'Down'

            if self.json_read['ADO8'] == 'Up':
                self.c9 = 'Up'
                self.output_8 = self.json_read['Status_8']
            else:
                self.c9 = 'Down'

            if self.json_read['ADO9'] == 'Up':
                self.c10 = 'Up'
                self.output_9 = self.json_read['Status_9']
            else:
                self.c10 = 'Down'

            if self.json_read['ADO10'] == 'Up':
                self.c11 = 'Up'
                self.output_10 = self.json_read['Status_10']
            else:
                self.c11 = 'Down'

            if self.json_read['ADO11'] == 'Up':
                self.c12 = 'Up'
                self.output_11 = self.json_read['Status_11']
            else:
                self.c12 = 'Down'

            if self.json_read['ADO12'] == 'Up':
                self.c13 = 'Up'
                self.output_12 = self.json_read['Status_12']
            else:
                self.c13 = 'Down'
            
            if self.json_read['ADO13'] == 'Up':
                self.c14 = 'Up'
                self.output_13 = self.json_read['Status_13']
            else:
                self.c14 = 'Down'

            if self.json_read['ADO14'] == 'Up':
                self.c15 = 'Up'
                self.output_14 = self.json_read['Status_14']
            else:
                self.c15 = 'Down'

            if self.json_read['ADO15'] == 'Up':
                self.c16 = 'Up'
                self.output_15 = self.json_read['Status_15']
            else:
                self.c16 = 'Down'

obj = Window(Tk())
obj.interfaz.mainloop()
