import customtkinter
import customtkinter as ctk
import re


import mysql.connector
import re
import os
import sys
import io
import time
from tabulate import tabulate

# Configurar la codificación de salida a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Variable to update the email on file 
global email_verify
global new_window


# Conexion Py con SQL DB remote
mydb = mysql.connector.connect(
    host= "192.168.1.13",
    user= "UserLaptop",
    password= "sebasmesi1305",
    database= "company"    
)

# Initiate instance of use MYSQL
mycursor = mydb.cursor()



# DEF REGULAR PATTERN OF VEIFTY EMAIL
def Validation_email(email_patter):
    pattern = r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$" 
    return re.match(pattern,email_patter) is not None

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Crear la ventana principal
root_tk = ctk.CTk()
root_tk.geometry("500x450") # (x,y)

# Frame of the Windows
frame = customtkinter.CTkFrame(master=root_tk, width=200,  height=200)
frame.pack()

"""
Def after to click on login this funcion gonna receive the 
info in format STR and then is going to validate into validation_email()
"""
def on_login():
    email_verify= Email_STR.get()
    if Validation_email(email_verify): # If everying is clear and correct then
        
        #  validate that the client has a email on file 
        query = "SELECT * FROM cliente WHERE email = %s"
        
        mycursor.execute(query,(email_verify,))
        result = mycursor.fetchall()
        
        if(len(result)) > 0:
            root_tk.destroy()
            new_window = ctk.CTk()
            new_window = ctk.CTkToplevel()  # Crea una nueva ventana secundaria
            new_window.title("Hola")
            new_window.geometry("300x200")
        else:
            print("no existe")
    else:
        frame_Error = customtkinter.CTkFrame(master=root_tk, width=100, height=10)
        frame_Error.pack(side=ctk.BOTTOM)
        label2 = customtkinter.CTkLabel(frame_Error, text='no cacorrin no sabes write an email', fg_color='red', font=('Arial',15))
        label2.pack()
        
        
        
    
        





# # Label Title
label = customtkinter.CTkLabel(frame, text='CustomerPurchaseManager', fg_color='transparent', font=('Arial',25))
label.pack()

# # Label Form 
Email_STR = ctk.StringVar()
entry = customtkinter.CTkEntry(frame, placeholder_text="Email", textvariable=Email_STR)
entry.pack()

# # Button Login
button3 = ctk.CTkButton(frame, text="Login", fg_color=("#DB3E39", "#821D1A"), command = on_login)
button3.pack()  

# Ejecutar el loop principal

root_tk.mainloop()  
