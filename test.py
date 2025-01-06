import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("简单计算器")
        
        # 初始化记忆变量
        self.memory = 0
        
        # 创建显示框
        self.display = ttk.Entry(root, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # 按钮布局
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '^', '√', 'M+', 'MR'  # 添加记忆功能按钮
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
                expression = self.display.get().replace('^', '**')  # 将^替换为**进行幂运算
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.memory = result  # 记住结果
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "错误")
        elif key == '√':
            try:
                number = float(self.display.get())
                result = math.sqrt(number)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.memory = result  # 记住结果
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "错误")
        elif key == 'M+':
            try:
                self.memory += float(self.display.get())  # 将当前显示的值加到记忆中
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "记忆已更新")
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "错误")
        elif key == 'MR':
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(self.memory))  # 显示记忆中的值
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

