import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("Vegas Airlines")
marco = Frame()
marco.config(width=600, height=400)

label = tk.Label(root, text = "Bienvenido a Vegas Airlines!")
codigo = tk.Label(root, text = "Código", font=("Agency FB", 24)).place(x= 150, y= 100)
apellido = tk.Label(root, text = "Apellido", font=("Agency FB", 24)).place(x= 376, y= 100)

entrada1 = StringVar()
entrada2 = StringVar()
txtCodigo = Entry(root, textvariable=entrada1, bd= 3).place(x=125, y=150)
txtCodigo2 = Entry(root, textvariable=entrada2, bd= 3).place(x=355, y=150)
boton = ttk.Button(text= "Confirmar").place(x= 265, y= 200)

label.pack()
marco.pack()

root.mainloop()