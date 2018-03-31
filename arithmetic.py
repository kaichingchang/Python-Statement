import tkinter as tk

class ArithmeticDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("四則運算")

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.optionList = ("+", "-", "*", "/")
        self.value = tk.StringVar()
        self.value.set("請選擇")
        self.optionmenu = tk.OptionMenu(self, self.value, *self.optionList)
        self.optionmenu.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=2, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "計算"
        self.button["command"] = self.calculate
        self.button.grid(row=3, column=0, sticky=tk.N+tk.W)

        self.label = tk.Label(self)
        self.label["text"] = "結果是..."
        self.label.grid(row=4, column=0, sticky=tk.N+tk.W)

    def calculate(self):
        result = 0
        a = int(self.entry1.get())
        b = int(self.entry2.get())
        if self.value.get() == "+":
            result =  a + b
        elif self.value.get() == "-":
            result =  a - b
        elif self.value.get() == "*":
            result =  a * b
        elif self.value.get() == "/":
            result =  a / b
        else:
            result = -9999
        self.label["text"] = str(result)

if __name__ == '__main__':
   root = tk.Tk()
   app = ArithmeticDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：arithmetic.py
# 功能：示範整數的四則運算
# 作者：張凱慶
