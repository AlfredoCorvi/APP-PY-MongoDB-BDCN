from pymongo import MongoClient
import tkinter as tk
from PIL import Image, ImageTk

def salir():
    root.destroy()

def ins():
    root.withdraw()
    iniciarsesion.deiconify()

def reg():
    root.withdraw()
    registrarse.deiconify()

root = tk.Tk()
root.title("UTC")
root.geometry("1000x500")
root.config(bg="#e5f3ec")

logo = Image.open("C:/Users/HP/Pictures/logoutc.png")  
logo = logo.resize((200, 130))
logo_tk = ImageTk.PhotoImage(logo)

frame_botones = tk.Frame(root, bg="#e5f3ec")  
frame_botones.place(relx=0.5, rely=0.5, anchor="center")  

label_logo = tk.Label(frame_botones, image=logo_tk, bg="#e5f3ec")
label_logo.pack(padx=0, pady=5)

btniniciarsesion = tk.Button(frame_botones, text="Iniciar Sesión", font=("Arial", 12), bg="#e2ece7", fg="black", command=ins)
btniniciarsesion.pack(pady=5, ipadx=80, ipady=10)
btnregistrar = tk.Button(frame_botones, text="Registrar Usuario", font=("Arial", 12), bg="#e2ece7", fg="black", command=reg)
btnregistrar.pack(pady=5, ipadx=66, ipady=10)
btnscerrar = tk.Button(frame_botones, text="Salir", font=("Arial", 12), bg="#af141d", fg="white", activebackground="#840f16", activeforeground="white", command=salir)
btnscerrar.pack(pady=5, ipadx=65, ipady=5)

iniciarsesion = tk.Toplevel(root)
iniciarsesion.title("Iniciar Sesión")
iniciarsesion.geometry("1000x500")
iniciarsesion.config(bg="#e5f3ec")
iniciarsesion.withdraw()  # Comienza oculta

registrarse = tk.Toplevel(root)
registrarse.title("Registro")
registrarse.geometry("1000x500")
registrarse.config(bg="#e5f3ec")
registrarse.withdraw()  # Comienza oculta

framereg = tk.Frame(registrarse, bg="#e5f3ec")
framereg.place(relx=0, rely=0.5, relheight=1, relwidth=0.5, anchor="w")
frame_centrar = tk.Frame(framereg, bg="#e5f3ec")
frame_centrar.pack(expand=True)

reglabellogo = tk.Label(frame_centrar, image=logo_tk, bg="#e5f3ec")
reglabellogo.pack(padx=0, pady=5)
reglabeltittle = tk.Label(frame_centrar, text="Registra Equipo",bg="#e5f3ec" , font=("Arial", 20), fg="black")
reglabeltittle.pack(padx=0, pady=5)

framereginput = tk.Frame(registrarse, bg="#e5f3ec")
framereginput.place(relx=0.5, rely=0.5, relheight=1, relwidth=0.5, anchor="w")
frame_centrarinput = tk.Frame(framereginput, bg="#e5f3ec")
frame_centrarinput.pack(expand=True)

nombre = tk.Entry(frame_centrarinput, text="Nombre del Artículo").pack(expand=True)

root.mainloop()