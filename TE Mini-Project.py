from tkinter import *
import tkinter as tk
import tkinter.messagebox as tmsg
import pymongo
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import date


client = pymongo.MongoClient('mongodb://localhost:27017')
db=client['Security_Gate_Register']
mycollection = db['Sai_Apartment']

def disp_grid():
    new1 = Toplevel()
    new1.attributes('-fullscreen', True)
    new1.configure(bg="#CACAFF")

    lst = ("Name", "Entry Time", "Exit Time", "Vehicle Number", "Address", "Phone Number")
    tree = ttk.Treeview(new1, columns=lst, show='headings')
    tree.heading('# 1', text="Name")
    tree.heading('# 2', text="Entry Time")
    tree.heading('# 3', text="Exit Time")
    tree.heading('# 4', text="Vehicle Number")
    tree.heading('# 5', text="Address")
    tree.heading('# 6', text="Phone Number")

    cursor = mycollection.find({})
    for i in cursor:
        data_lst = [i['name'],i['entry'],i['exit'],i['vehicle'],i['address'],i['phone_No']]
        tree.insert(parent='',index=END, values=tuple(data_lst))

    tree.pack(side = TOP,pady=20)
    def back1():
        new1.destroy()
    Button(new1, text="Back", bd=8, command=back1,height=3, width=15,bg="#FFFFFF",padx= 30).pack(side=BOTTOM,pady=5)

    new1.mainloop()

def adding():
    new=Toplevel()
    new.attributes('-fullscreen', True)
    new.configure(bg="#CACAFF")
    frame = Frame(new)
    frame.configure(bg="#CACAFF")
    frame.pack()

    centerF = Frame(new)
    centerF.pack(anchor="center",pady=10)

    Label(frame,text="New Entry",font=("lucida 22 bold"),padx=12,pady=30,bg="#CACAFF").grid(row=2,column=4,pady=70)
    Label(frame, text="Name", padx=6, pady=6,bg="#CACAFF").grid(row=5, column=3)
    Label(frame, text="Entry Time", padx=6, pady=6,bg="#CACAFF").grid(row=6, column=3)
    Label(frame, text="Exit Time", padx=5, pady=6,bg="#CACAFF").grid(row=7, column=3)
    Label(frame, text="Vehicle Number", padx=5, pady=6,bg="#CACAFF").grid(row=8, column=3)
    Label(frame, text="Address", padx=5, pady=6,bg="#CACAFF").grid(row=9, column=3)
    Label(frame, text="Phone Number", padx=5, pady=6,bg="#CACAFF").grid(row=10, column=3)

    namevalue = tk.StringVar()
    entryvalue = tk.StringVar()
    exitvalue = tk.StringVar()
    vehiclevalue = tk.StringVar()
    addressvalue = tk.StringVar()
    phonevalue = tk.StringVar()

    Entry(frame, bd=3, textvariable=namevalue, width=35).grid(row=5, column=5)
    Entry(frame, bd=3, textvariable=entryvalue, width=35).grid(row=6, column=5)
    Entry(frame, bd=3, textvariable=exitvalue, width=35).grid(row=7, column=5)
    Entry(frame, bd=3, textvariable=vehiclevalue, width=35).grid(row=8, column=5)
    Entry(frame, bd=3, textvariable=addressvalue, width=35).grid(row=9, column=5)
    Entry(frame, bd=3, textvariable=phonevalue, width=35).grid(row=10, column=5)

    def register():
        dic = {
            'name': namevalue.get(),
            'entry': entryvalue.get(),
            'exit': exitvalue.get(),
            'vehicle': vehiclevalue.get(),
            'address': addressvalue.get(),
            'phone_No': phonevalue.get()
        }
        mycollection.insert_one(dic)
        tmsg.showinfo("Registration", "Thank You For Visiting !!!")
        new.destroy()

    def back():
        new.destroy()

    Button(frame, text="Back", bd=8, command=back,height=3, width=15,bg="#FFFFFF",padx= 30).grid(row=25, column=3,pady=30)
    Button(frame, text="Register", bd=8,command=register,height=3, width=15,padx=30,bg="#FFFFFF").grid(row=25, column=5,pady=30)

    new.mainloop()

window=Tk()
window.attributes('-fullscreen',True)
window.configure(bg="#CACAFF")
window.title("Frame 1")
Label(window,text="Welcome to SAI Apartment",font=("playfair 22 bold"),padx=25,bg="#CACAFF").pack(side=TOP,pady=94)


nB=Button(window,text="New Registeration",bd=8,command=adding,height=3, width=20,bg="#FFFFFF").pack(side=TOP,pady=16)
dD=Button(window,text="Display Data",bd=8,command=disp_grid,height=3, width=20,bg="#FFFFFF").pack(side=TOP,pady=16)
E=Button(window, text="Exit",bd=8,command=window.destroy,height=3, width=20,bg="#FFFFFF").pack(side=TOP,pady=16)

window.mainloop()