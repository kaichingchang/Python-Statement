import tkinter as tk

class ShiftDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("位移運算")

        self.label1 = tk.Label(self)
        self.label1["text"] = "整數 8:"
        self.label1.grid(row=0, column=0, columnspan=6, sticky=tk.N+tk.W)

        self.button1 = tk.Button(self)
        self.button1["text"] = "<< 3"
        self.button1["command"] = self.calculate1
        self.button1.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.button2 = tk.Button(self)
        self.button2["text"] = "<< 2"
        self.button2["command"] = self.calculate2
        self.button2.grid(row=1, column=1, sticky=tk.N+tk.W)

        self.button3 = tk.Button(self)
        self.button3["text"] = "<< 1"
        self.button3["command"] = self.calculate3
        self.button3.grid(row=1, column=2, sticky=tk.N+tk.W)

        self.button4 = tk.Button(self)
        self.button4["text"] = ">> 1"
        self.button4["command"] = self.calculate4
        self.button4.grid(row=1, column=3, sticky=tk.N+tk.W)

        self.button5 = tk.Button(self)
        self.button5["text"] = ">> 2"
        self.button5["command"] = self.calculate5
        self.button5.grid(row=1, column=4, sticky=tk.N+tk.W)

        self.button6 = tk.Button(self)
        self.button6["text"] = ">> 3"
        self.button6["command"] = self.calculate6
        self.button6.grid(row=1, column=5, sticky=tk.N+tk.W)

        self.label2 = tk.Label(self)
        self.label2["text"] = "結果是..."
        self.label2.grid(row=2, column=0, columnspan=6, sticky=tk.N+tk.W)

    def calculate1(self):
        self.label2["text"] = str(8 << 3)
        self.button1["state"] = "disabled"

    def calculate2(self):
        self.label2["text"] = str(8 << 2)
        self.button2["state"] = "disabled"

    def calculate3(self):
        self.label2["text"] = str(8 << 1)
        self.button3["state"] = "disabled"

    def calculate4(self):
        self.label2["text"] = str(8 >> 1)
        self.button4["state"] = "disabled"

    def calculate5(self):
        self.label2["text"] = str(8 >> 2)
        self.button5["state"] = "disabled"

    def calculate6(self):
        self.label2["text"] = str(8 >> 3)
        self.button6["state"] = "disabled"


if __name__ == '__main__':
   root = tk.Tk()
   app = ShiftDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：shift.py
# 功能：示範整數的四則運算
# 作者：張凱慶
