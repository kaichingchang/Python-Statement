import tkinter as tk

class BiggerDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("關係運算")

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "比大小"
        self.button["command"] = self.calculate
        self.button.grid(row=2, column=0, sticky=tk.N+tk.W)

        self.label = tk.Label(self)
        self.label["text"] = "結果是..."
        self.label.grid(row=3, column=0, sticky=tk.N+tk.W)

    def calculate(self):
        a = int(self.entry1.get())
        b = int(self.entry2.get())
        if a == b:
            self.label["text"] = "兩者相等。"
        else:
            if a > b:
                self.label["text"] = str(a) + "比較大。"
            else:
                self.label["text"] = str(b) + "比較大。"

if __name__ == '__main__':
   root = tk.Tk()
   app = BiggerDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：bigger.py
# 功能：示範整數的關係運算
# 作者：張凱慶
