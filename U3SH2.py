from pymongo import MongoClient
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

mongo_client = MongoClient("mongodb://localhost:27017/")
utc = mongo_client["utc"]
coleccion = utc["articulos"]

def salir():
    root.destroy()

def ins():
    root.withdraw()
    iniciarsesion.deiconify()
    cargar_datos()

def reg():
    root.withdraw()
    registrarse.deiconify()

def volver_a_root(ventana):
    ventana.withdraw()
    root.deiconify()

def registrar_articulo():
    nombre = entrynombre.get().strip()
    cantidad = entrycantidad.get().strip()
    precio = entryprecio.get().strip()
    
    if nombre and cantidad and precio:
        try:
            cantidad = int(cantidad)
            precio = float(precio)
            articulo = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
            coleccion.insert_one(articulo)
            labelmensaje.config(text="Artículo registrado con éxito", fg="green")
        except ValueError:
            labelmensaje.config(text="Error: Cantidad debe ser entero y Precio decimal.", fg="red")
    else:
        labelmensaje.config(text="Completa todos los campos.", fg="red")

def cargar_datos():
    tabla.delete(*tabla.get_children())

    for articulo in coleccion.find():
        tabla.insert("", "end", values=(articulo["nombre"], articulo["cantidad"], articulo["precio"]))

root = tk.Tk()
root.title("UTC")
root.geometry("1000x500")
root.config(bg="#e5f3ec")

logo = Image.open("C:/Users/HP/Pictures/logoutc.png") #cambia la ubicacion copia la ruta 
logo = logo.resize((200, 130))
logo_tk = ImageTk.PhotoImage(logo)

frame_botones = tk.Frame(root, bg="#e5f3ec")  
frame_botones.place(relx=0.5, rely=0.5, anchor="center")  

label_logo = tk.Label(frame_botones, image=logo_tk, bg="#e5f3ec")
label_logo.pack(padx=0, pady=5)

btniniciarsesion = tk.Button(frame_botones, text="Articulos Registrados", font=("Arial", 12), bg="#e2ece7", fg="black", command=ins)
btniniciarsesion.pack(pady=5, ipadx=80, ipady=10)
btnregistrar = tk.Button(frame_botones, text="Registrar Articulos", font=("Arial", 12), bg="#e2ece7", fg="black", command=reg)
btnregistrar.pack(pady=5, ipadx=66, ipady=10)
btnscerrar = tk.Button(frame_botones, text="Salir", font=("Arial", 12), bg="#af141d", fg="white", activebackground="#840f16", activeforeground="white", command=salir)
btnscerrar.pack(pady=5, ipadx=65, ipady=5)

iniciarsesion = tk.Toplevel(root)
iniciarsesion.title("Iniciar Sesión")
iniciarsesion.geometry("1000x500")
iniciarsesion.config(bg="#e5f3ec")
iniciarsesion.withdraw()

frame_tabla = tk.Frame(iniciarsesion, bg="#e5f3ec")
frame_tabla.pack(pady=20, padx=20, expand=True, fill="both")

columnas = ("Nombre", "Cantidad", "Precio")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

tabla.heading("Nombre", text="Nombre")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Precio", text="Precio")

tabla.column("Nombre", width=300)
tabla.column("Cantidad", width=150)
tabla.column("Precio", width=150)

scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

btnactualizar = tk.Button(iniciarsesion, text="Actualizar Tabla", font=("Arial", 12), bg="#e2ece7", fg="black", command=cargar_datos)
btnactualizar.pack(pady=10)

btn_volver_inicio = tk.Button(iniciarsesion, text="Volver al Menú", font=("Arial", 12), bg="#e2ece7", fg="black", command=lambda: volver_a_root(iniciarsesion))
btn_volver_inicio.pack(pady=10)

registrarse = tk.Toplevel(root)
registrarse.title("Registro")
registrarse.geometry("1000x500")
registrarse.config(bg="#e5f3ec")
registrarse.withdraw()

framereg = tk.Frame(registrarse, bg="#e5f3ec")
framereg.place(relx=0, rely=0.5, relheight=1, relwidth=0.5, anchor="w")
frame_centrar = tk.Frame(framereg, bg="#e5f3ec")
frame_centrar.pack(expand=True)

reglabellogo = tk.Label(frame_centrar, image=logo_tk, bg="#e5f3ec")
reglabellogo.pack(padx=0, pady=5)
reglabeltittle = tk.Label(frame_centrar, text="Registra Artículo", bg="#e5f3ec", font=("Arial", 20), fg="black")
reglabeltittle.pack(padx=0, pady=5)

framereginput = tk.Frame(registrarse, bg="#e5f3ec")
framereginput.place(relx=0.5, rely=0.5, relheight=1, relwidth=0.5, anchor="w")
frame_centrarinput = tk.Frame(framereginput, bg="#e5f3ec")
frame_centrarinput.pack(expand=True)

tk.Label(frame_centrarinput, text="Nombre", font=("Arial", 18)).pack(pady=5)
entrynombre = tk.Entry(frame_centrarinput, font=("Arial", 14))
entrynombre.pack(pady=5, ipadx=80, ipady=5)

tk.Label(frame_centrarinput, text="Cantidad", font=("Arial", 18)).pack(pady=5)
entrycantidad = tk.Entry(frame_centrarinput, font=("Arial", 14))
entrycantidad.pack(pady=5, ipadx=80, ipady=5)

tk.Label(frame_centrarinput, text="Precio", font=("Arial", 18)).pack(pady=5)
entryprecio = tk.Entry(frame_centrarinput, font=("Arial", 14))
entryprecio.pack(pady=5, ipadx=80, ipady=5)

labelmensaje = tk.Label(frame_centrarinput, text="", font=("Arial", 12), fg="black", bg="#e5f3ec")
labelmensaje.pack(pady=5)

btnregistrararticulo = tk.Button(frame_centrarinput, text="Registrar Artículo", font=("Arial", 18), bg="#e2ece7", fg="black", command=registrar_articulo)
btnregistrararticulo.pack(pady=5, ipadx=80, ipady=10)

btn_volver_registro = tk.Button(frame_centrarinput, text="Volver al Menú", font=("Arial", 12), bg="#e2ece7", fg="black", command=lambda: volver_a_root(registrarse))
btn_volver_registro.pack(pady=10)

root.mainloop()
