import tkinter as tk
import random as ra
import time as ti

def Happy():
    root = tk.Tk()
    width = 200
    height = 50
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = ra.randint(0, screenwidth)
    y = ra.randint(0, screenheight)
    root.title("⭐")
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    tk.Label(root, text='国庆快乐', fg='gold', bg='red', font=("Comic Sans MS", 20), width=30, height=5).pack()
    root.mainloop()

def Star():
    root = tk.Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    root.geometry("%dx%d+%d+%d" % (screenwidth, screenheight, 0, 0))
    root.title("⭐")
    tk.Label(root, text="⭐", fg='yellow', bg='red', font=("Comic Sans MS", 500), width=300, height=0).pack()
    root.mainloop()

# 在主线程中运行Happy和Star函数
Happy()
time.sleep(1)  # 等待1秒
Star()
