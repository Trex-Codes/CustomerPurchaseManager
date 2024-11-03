import customtkinter as ctk
import re
import mysql.connector
import sys
import io

# Configurar la codificación de salida a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Variables globales
Error_Email = None  # Declarar Error_Email globalmente
Frame_Error = None  # Declarar Frame_Error globalmente

# Conexión a la base de datos remota
mydb = mysql.connector.connect(
    host="192.168.1.13",
    user="UserLaptop",
    password="sebasmesi1305",
    database="company"
)
mycursor = mydb.cursor()

# Patrón de validación de correo electrónico
def Validation_email(email_patter):
    pattern = r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$"
    return re.match(pattern, email_patter) is not None

# Configuración de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Crear la ventana principal
root_tk = ctk.CTk()
root_tk.geometry("500x450")

# Crear el frame principal
frame = ctk.CTkFrame(master=root_tk, width=200, height=200)
frame.pack()

def Create_email():
    # Crear ventana para registrar nuevo correo
        # Etiqueta para el título de la ventana de registro
    label = ctk.CTkLabel(root_tk, text="Registrar Nuevo Correo", font=("Arial", 20))
    label.pack(pady=20)
    
    # Aquí puedes agregar más componentes para la ventana de registro

# Función para limpiar el contenido de la ventana principal
def clear_frame():
    for widget in root_tk.winfo_children():
        widget.pack_forget()  # Ocultar cada widget en el frame

# Función para iniciar sesión
def on_login():
    global Error_Email  # Usar la variable global
    global Frame_Error 
    
    email_verify = Email_STR.get()

    # Eliminar el mensaje de error previo si existe
    if Error_Email is not None and Frame_Error is not None:
        Error_Email.destroy()
        Frame_Error.destroy()

    if Validation_email(email_verify):  # Si el correo es válido
        # Validar que el cliente tiene un correo en la base de datos
        query = "SELECT * FROM cliente WHERE email = %s"
        mycursor.execute(query, (email_verify,))
        result = mycursor.fetchall()    

        if len(result) > 0:
            # Si el correo existe, abrir la ventana de bienvenida
            new_window = ctk.CTkToplevel(root_tk)  # Crea una nueva ventana secundaria
            new_window.title("Hola")
            new_window.geometry("300x200")
            clear_frame()  # Limpia el contenido de la ventana principal
            ctk.CTkLabel(new_window, text="Bienvenido!", font=("Arial", 20)).pack(pady=20)
        else:
            # Si el correo no existe, mostrar mensaje de error
            Frame_Error = ctk.CTkFrame(master=root_tk, width=200, height=60)
            Frame_Error.pack(side=ctk.BOTTOM, fill=ctk.X)
            
            # Mostrar mensaje si no existe el correo en la base de datos
            Error_Email = ctk.CTkLabel(Frame_Error, text="No existe el correo en la base de datos", 
                                   fg_color="red", font=("Arial", 15), height=50, text_color="purple")
            Error_Email.pack(fill=ctk.X) 
            
            # Limpia el contenido de la ventana principal y abre la ventana de registro
            clear_frame()
            Create_email()
    else: 
        # Formato de correo no válido
        Frame_Error = ctk.CTkFrame(master=root_tk, width=200, height=60)
        Frame_Error.pack(side=ctk.BOTTOM, fill=ctk.X)
        
        # Mostrar mensaje de error si el correo es inválido
        Error_Email = ctk.CTkLabel(Frame_Error, text="Formato de Correo inválido, intenta nuevamente", 
                               fg_color="red", font=("Arial", 15), height=50)
        Error_Email.pack(fill=ctk.X)

# Etiqueta del título
label = ctk.CTkLabel(frame, text="CustomerPurchaseManager", fg_color="transparent", font=("Arial", 25))
label.pack()

# Campo de entrada de correo electrónico
Email_STR = ctk.StringVar()
entry = ctk.CTkEntry(frame, placeholder_text="Email", textvariable=Email_STR)
entry.pack()

# Botón de inicio de sesión
button3 = ctk.CTkButton(frame, text="Login", fg_color=("#DB3E39", "#821D1A"), command=on_login)
button3.pack()

# Ejecutar el bucle principal
root_tk.mainloop()
