from tkinter import *
import os
from tkinter import filedialog, messagebox

BG_COLOR = "#263D42"

apps = []

def displayApp(frame1):
    for stuff in frame1.winfo_children():
        stuff.destroy()
    for app in apps:
        label = Label(frame1, text=app, bg="gray")
        label.pack(side=TOP)

def addApp(frame1):
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Executables", "*.exe"), ("All Files", "*.*")))
    if filename != "":
        apps.append(filename)
        print(filename)
        displayApp(frame1)

def runApp(label1):
    if len(apps)==0:
        print("No files")
        if label1.cget("text") == "No Files Selected":
            def turnwhite():
                label1.config(text="No Files Selected", fg="red", bg="white", font=("Courier", 12))
                label1.after(50, turnblack)
            def turnblack():
                label1.config(text="No Files Selected", fg="red", bg="black", font=("Courier", 12))
                checker = label1.after(50, turnwhite)
                if checker is not None:
                    label1.after_cancel(checker)
            turnwhite()
        else:
            label1.config(text="No Files Selected", fg="red", bg="black", font=("Courier", 12))
    else:
        for app in apps:
            label1.config(text="")
            os.startfile(app)

def removeApp(frame1, label1):
    if len(apps)==0:
        result1 = messagebox.askokcancel("No Files Selected", "Please select a file before removing")
        if result1 == True:
            label1.config(text="No Files Selected", fg="red", bg="black", font=("Courier", 12))
        else:
            pass
    else:
        result = messagebox.askquestion("Delete all Content", "Deleted content cannot be retrieved. Are you sure you want to delete?", icon="warning")
        if result == 'yes':
            apps.clear()
            displayApp(frame1)
        else:
            pass

def main():
    root4 = Tk()
    root4.title("Open Apps")
    ws = root4.winfo_screenwidth()/2 - 250
    hs = root4.winfo_screenheight()/2 - 300
    root4.geometry("500x600+%d+%d" % (ws, hs))
    canvas = Canvas(root4, height=400, width=400, bg=BG_COLOR)
    canvas.pack(fill=BOTH, expand=True)
    frame1 = Frame(canvas, bg="white")
    frame1.place(relwidth=0.85, relheight=0.85, relx=0.075, rely=0.075)
    frame2 = Frame(canvas)
    frame2.pack(side=BOTTOM)
    label1 = Label(frame2)
    label1.pack(side=BOTTOM)

    openfile = Button(root4, text="Open Files", fg="white", bg=BG_COLOR, height=1, font=("Arial", 12), command=lambda:addApp(frame1))
    openfile.pack(side=TOP, padx=10, pady=3)
    runfile = Button(root4, text="Run Files", fg="green", bg=BG_COLOR, height=1, font=("Arial", 12), command=lambda:runApp(label1))
    runfile.pack(side=TOP, padx=10, pady=3)
    removefile = Button(root4, text="Remove All Files", fg="red", bg=BG_COLOR, height=1, font=("Arial", 12), command=lambda:removeApp(frame1, label1))
    removefile.pack(side=TOP, padx=10, pady=3)
    displayApp(frame1)

    root4.mainloop()


if __name__=='__main__':
    if os.path.isfile("saved-apps.txt"):
        with open("saved-apps.txt", "r") as f:
            temp_app = f.read()
            temp_app = temp_app.split(",")
            apps = [x for x in temp_app if x.strip()]
            print(temp_app)
            print(apps)
    main()
    with open('saved-apps.txt', 'w') as f:
        for app in apps:
            f.write(app + ",")
            print("App has been saved")