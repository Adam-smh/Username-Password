from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Username and Password")
root.geometry("500x400")
root.config(bg="#161A1D")


class userpass:
    def __init__(self, window):
        self.req = Label(window, text="Please enter your Username and Password:", bg="#161A1D", fg="white")
        self.req.place(relx="0.2", rely="0.1")
        self.userl = Label(window, text="Username:", bg="#161A1D", fg="white")
        self.userl.place(relx="0.1", rely="0.3")
        self.user_entry = Entry(window)
        self.user_entry.place(relx="0.3", rely="0.3")
        self.passw = Label(window, text="Password:", bg="#161A1D", fg="white")
        self.passw.place(relx="0.1", rely="0.4")
        self.passw_entry = Entry(window)
        self.passw_entry.place(relx="0.3", rely="0.4")
        self.submit = Button(window, text="Submit", command=self.submitb)
        self.submit.place(relx="0.3", rely="0.5")
        self.clear = Button(window, text="Clear", command=self.delete)
        self.clear.place(relx="0.51", rely="0.5")
        self.exit = Button(window, text="Exit", command="exit")
        self.exit.place(relx="0.43", rely="0.6")
        self.user_pass = {'Vuyani': 'vuya@2021', 'Atheelah': 'maroon17', 'Ikraam': 'carsthemovie', 'Nathan': 'blue101',
                          'Amanda': '@manda20'}

    def submitb(self):
        name = self.user_entry.get()
        pw = self.passw_entry.get()
        if name == "" or pw == "":
            messagebox.showerror(message="Please enter details")

        elif name in self.user_pass:
            if pw == self.user_pass[name]:
                messagebox.showinfo(message="Success")
            else:
                messagebox.showerror(message="Password incorrect")
        else:
            messagebox.showerror(message="Username not found")

    def delete(self):
        self.user_entry.delete(0, END)
        self.passw_entry.delete(0, END)


userpass(root)
root.mainloop()
