import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

root = tk.Tk()
root.title("Vegas Airlines")
marco = Frame()
marco.config(width=600, height=400)

label = tk.Label(root, text = "Bienvenido a Vegas Airlines!")
codigo = tk.Label(root, text = "Código", font=("Agency FB", 24)).place(x= 150, y= 100)
apellido = tk.Label(root, text = "Apellido", font=("Agency FB", 24)).place(x= 376, y= 100)

def confirmacion(): #Datos de prueba
    if entrada1.get() == "1234" and entrada2.get() == "Perez":
        abrirventana()
    else:
        messagebox.showerror("Vegas Airlines", "Error, Codigo o Apellido indetectable en base de datos.")

def abrirventana():
    root.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Vegas Airlines")
    ventana.geometry("600x400")
    marco2 = Frame(ventana)
    marco2.config(width=600, height=400)
    label2 = tk.Label(ventana, text= "Vegas Airlines", font=("Agency FB", 24))
    label3 = tk.Label(ventana, text= "Origen", font=("Agency FB", 20), bd= 3).place(x= 150, y= 100)
    label4 = tk.Label(ventana, text= "Destino", font=("Agency FB", 20), bd= 3).place(x= 150, y= 250)
    label5 = tk.Label(ventana, text= "Fecha", font=("Agency FB", 20), bd= 3).place(x= 420, y= 100)
    label6 = tk.Label(ventana, text= "Personas", font=("Agency FB", 20), bd= 3).place(x= 400, y= 250)
    opciones_origen = ttk.Combobox(ventana, values=["Bogota", "Cali", "Cartagena", "Medellin", "Santa Marta", "Tulua"]).place(x= 110, y= 150)
    opciones_destino = ttk.Combobox(ventana, values=["Bogota", "Cali", "Cartagena", "Medellin", "Santa Marta", "Tulua"]).place(x= 110, y= 300)
    entrada_fecha = StringVar()
    entrada_personas = StringVar()
    txtFecha = Entry(ventana, textvariable=entrada_fecha, bd= 3).place(x= 380, y= 150)
    txtPersonas = Entry(ventana, textvariable=entrada_personas, bd= 3).place(x= 380, y= 300)
    boton2 = ttk.Button(ventana, text= "Confirmar", command=abrirventana2).place(x= 265, y= 350)
    
    label2.pack()
    marco2.pack()
    ventana.mainloop()

def abrirventana2():
    pass


entrada1 = StringVar()
entrada2 = StringVar()
txtCodigo = Entry(root, textvariable=entrada1, bd= 3).place(x=125, y=150)
txtCodigo2 = Entry(root, textvariable=entrada2, bd= 3).place(x=355, y=150)
boton = ttk.Button(text= "Confirmar", command=confirmacion).place(x= 265, y= 200)

label.pack()
marco.pack()

root.mainloop()