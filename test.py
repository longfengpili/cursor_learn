import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("简单计算器")
        
        # 创建显示框
        self.display = ttk.Entry(root, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # 按钮布局
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # 创建按钮
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(root, text=button, command=cmd).grid(
                row=row, column=col, padx=2, pady=2, sticky="nsew"
            )
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # 添加清除按钮
        ttk.Button(root, text='C', command=self.clear).grid(
            row=row, column=col, padx=2, pady=2, sticky="nsew"
        )
        
        # 设置网格权重，使按钮能够自适应窗口大小
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "错误")
        else:
            self.display.insert(tk.END, key)

    def clear(self):
        self.display.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry("300x400")  # 设置窗口初始大小
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

