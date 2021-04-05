from login_sys import Login
from tkinter import*


def setup(window):
    window.title("Restaurant Management")
    window.geometry("1200x900")
    log = Login(window)
    log.pack(expand=True, fill=BOTH)


if __name__ == '__main__':
    root = Tk()
    setup(root)
    root.mainloop()
