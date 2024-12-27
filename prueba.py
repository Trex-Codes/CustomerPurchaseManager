import customtkinter as ctk
import re
import mysql.connector
import sys

import requests
from PIL import Image
import io
# Configuration of Output a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Global Variables
Error_Email = None  # Declarar Error_Email globalmente
Frame_Error = None  # Declarar Frame_Error globalmente

# Colors_Error_incorrect info
Color_Error_incorrect = '#f75555'
Color_correct = '#88f17a'
color_text_Message = '#f3f3f3'

# Connection DB MYSQL
mydb = mysql.connector.connect(
    host="localhost",        # Dirección del servidor MySQL
    user="root",       # Tu usuario MySQL
    password="Sebasmesi1305",# Tu contraseña MySQL
    database="company" # Nombre de la base de datos
)
mycursor = mydb.cursor()

# pattern email for regex 
def Validation_email(email_patter):
    pattern = r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$"
    return re.match(pattern, email_patter) is not None
    
# Clear widgets of the main window after to verify the email or create a new user
def clear_frame(Window):
    for widget in Window.winfo_children():
        widget.destroy()  # Ocultar cada widget en el fracme

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create main Windows (Root)
root_tk = ctk.CTk()
root_tk.geometry("560x550") # (x,y)


def Create_email():
    
    def Create_Account():
        
        list_Items_CX_NEW = [FullName_CreateSTR.get(), Age_CreateSTR.get(),  Phone_CreateSTR.get(), Email_STR.get(), select_Option_City.get(), Address_CreateSTR.get()]
        if any(not items for items in list_Items_CX_NEW):
                MessageFrame_Generation_CreateEmail("Empy fields, review all", Color_Error_incorrect, color_text_Message)
        else: 
            # query to insert the new information of the client on the DB 
            query = "INSERT INTO cliente (nombre, edad, telefono, email, ciudad, direccion) VALUES (%s, %s, %s, %s, %s, %s);"
            mycursor.execute(query, list_Items_CX_NEW)
            mydb.commit()
            
            MessageFrame_Generation_CreateEmail("Register (s) inserted in right way!", Color_correct, color_text_Message)
            root_tk.after(2000, root_tk.destroy)
            
    frame_create_Email = ctk.CTkFrame(master=root_tk, width=100, height=30)
    frame_create_Email.grid(row=0, column=0, pady=(50,0), padx=120)

    label = ctk.CTkLabel(frame_create_Email, text="Create New Account", font=("Arial", 20))
    label.grid(row=1, column=0, pady=15, columnspan=3)

    # Label Full name
    label_name = ctk.CTkLabel(frame_create_Email, text="Full name:")
    label_name.grid(row=2, column=0, pady=(0,30))
    # Entry  Full name
    FullName_CreateSTR = ctk.StringVar()
    entry_name = ctk.CTkEntry(frame_create_Email, width=150, placeholder_text="Full Name", textvariable=FullName_CreateSTR)
    entry_name.grid(row=2, column=1, padx=(5,20), pady=(0,30))
    
     # Label Age
    label_age = ctk.CTkLabel(frame_create_Email, text="Age:")
    label_age.grid(row=3, column=0, pady=(0,30))
     # Entry Age
    Age_CreateSTR = ctk.StringVar()
    entry_age = ctk.CTkEntry(frame_create_Email, width=150, placeholder_text="Age", textvariable=Age_CreateSTR)
    entry_age.grid(row=3, column=1, padx=(5,20), pady=(0,30))
    
    #  Label Phone number
    label_phone = ctk.CTkLabel(frame_create_Email, text="Phone number:")
    label_phone.grid(row=4, column=0, pady=(0,30))
    # Entry  Phone number
    Phone_CreateSTR = ctk.StringVar()
    entry_phone = ctk.CTkEntry(frame_create_Email, width=150, placeholder_text="Phone:", textvariable=Phone_CreateSTR)
    entry_phone.grid(row=4, column=1, padx=(5,20), pady=(0,30))
    
    
    # label  city   
    options = [
        "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Cúcuta", 
        "Bucaramanga", "Pereira", "Manizales", "Ibagué", "Santa Marta", 
        "Villavicencio", "Pasto", "Montería", "Neiva", "Armenia", "Sincelejo", 
        "Valledupar", "Popayán", "Tunja", "Riohacha", "Florencia", "Quibdó", 
        "Yopal", "San Andrés", "Leticia", "Mocoa", "Puerto Carreño", 
        "San José del Guaviare", "Inírida" 
    ]
    
    label_city = ctk.CTkLabel(frame_create_Email, text="City:")
    label_city.grid(row=5, column=0, pady=(0,30))
    # Entry Options city
    select_Option_City = ctk.StringVar(value="Options")
    Label_Option_city = ctk.CTkOptionMenu(frame_create_Email, variable=select_Option_City, values=options)
    Label_Option_city.grid(row=5, column=1, padx=(5,20), pady=(0,30))
    
    # Label address
    label_address = ctk.CTkLabel(frame_create_Email, text="Address:")
    label_address.grid(row=6, column=0, pady=(0,30))
    # Entry  address
    Address_CreateSTR = ctk.StringVar()
    entry_address = ctk.CTkEntry(frame_create_Email, width=150, placeholder_text="Address:", textvariable=Address_CreateSTR)
    entry_address.grid(row=6, column=1, padx=(5,20), pady=(0,30))
    
    # Button create Account (Sign up)
    button_Create_Email = ctk.CTkButton(frame_create_Email, text="Sign up", fg_color=("#DB3E39", "#821D1A"), command=Create_Account)
    button_Create_Email.grid(row=7, column=0, columnspan=3, padx=(5,20), pady=(0,30))
    
    
    
 
 
 
def MessagesFrame_Generation(textFrame, fg_colorFrame, color_textFrame):
    
    global Error_Email  # Global variable
    global Frame_Error 
    
    if Error_Email is not None and Frame_Error is not None:
        Error_Email.destroy()
        Frame_Error.destroy()
        
    Frame_Error = ctk.CTkFrame(master=root_tk, width=200, height=60)
    Frame_Error.pack(side=ctk.BOTTOM, fill=ctk.X)
    
    Error_Email = ctk.CTkLabel(Frame_Error,
                               text=textFrame, 
                               fg_color=fg_colorFrame,
                               font=("Arial", 15),
                               height=50,
                               text_color=color_textFrame)
    Error_Email.pack(fill=ctk.X) 
    
def MessageFrame_Generation_CreateEmail(textFrame, fg_colorFrame, color_textFrame):
    
    # Configura el marco para la parte inferior
    bottom_frame = ctk.CTkFrame(master=root_tk)
    bottom_frame.grid(row=1, column=0, sticky="ew") 

    # Configura el Label en el frame inferior
    Error_EmptyLabel = ctk.CTkLabel(bottom_frame,
                                    text=textFrame,
                                    fg_color=fg_colorFrame,
                                    font=("Arial", 15),
                                    height=50,
                                    text_color=color_textFrame)
    Error_EmptyLabel.pack(fill=ctk.X, side=ctk.BOTTOM)  

    # Configura el peso de la fila y la columna para ocupar todo el espacio
    root_tk.grid_columnconfigure(0, weight=1)
    root_tk.grid_rowconfigure(0, weight=1)  # Asegúrate de que la fila 0 tiene peso
    

# function start or login into the  system
def on_login():

    email_verify = Email_STR.get()
    # email_verify = "carlos@gmail.com"

    # Delete frame and label of error when the format is not valid at the email
    # Verify if those  fields are not empty, if they are  empty nothing happend
    # but is those variables already appear on the screen, they gonna be deleted

    if Validation_email(email_verify):  # Valid Email
        
        # Verify that the email  is already registered on the DB
        query = "SELECT * FROM cliente WHERE email = %s"
        mycursor.execute(query, (email_verify,))
        result = mycursor.fetchall()    

        if len(result) > 0:
            
            # If  the email is already registered, show the welcome  message
            clear_frame(root_tk)
            
            # ADD PURCHASE
            urlADD = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/Delcompra.png?raw=true"
            responseAdd = requests.get(urlADD)
            image_dataAdd = io.BytesIO(responseAdd.content)
            
            frame_Login_Done = ctk.CTkFrame(master=root_tk, width=270, height=250)
            frame_Login_Done.grid(row=0, column=0, pady=(40,0), padx=50)

            icon_imageAdd = ctk.CTkImage(dark_image=Image.open(image_dataAdd), size=(20, 20))

            button_ADD_Purchase = ctk.CTkButton(
                                                frame_Login_Done,
                                                text="Add Purchase",
                                                fg_color="#51adee",
                                                hover_color='#70bd99',
                                                compound="right",
                                                image=icon_imageAdd)
            button_ADD_Purchase.grid(row=1, column=0, columnspan=2, pady=(50,30), padx=50)
            
            
            

            
            # DELETE PURCHASE
            urlDEL = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/Addcompra.png?raw=true"
            responseDel = requests.get(urlDEL)
            image_dataDel = io.BytesIO(responseDel.content)
            
            icon_imageDel = ctk.CTkImage(dark_image=Image.open(image_dataDel), size=(20, 20))

            button_DEL_Purchase = ctk.CTkButton(
                                                frame_Login_Done,
                                                text="Delete Purchase",
                                                fg_color='#ed5154',
                                                hover_color='#70bd99',
                                                compound="right",
                                                image=icon_imageDel)
            button_DEL_Purchase.grid(row=2, column=1, columnspan=2, pady=(30,30), padx=50)
            
            
            
            
            
            # UPDATE USER
            urlDEL = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/persona.png?raw=true"
            responseUser = requests.get(urlDEL)
            image_dataUser = io.BytesIO(responseUser.content)
            
            icon_imageUser = ctk.CTkImage(dark_image=Image.open(image_dataUser), size=(20, 20))

            button_DEL_Purchase = ctk.CTkButton(
                                               frame_Login_Done,
                                                text="Update User",
                                                fg_color='#1F5673',
                                                compound="right",
                                                image=icon_imageUser,
                                                width=25)
            button_DEL_Purchase.grid(row=3, column=1, columnspan=2, pady=(30,30), padx=50)
                        
            
            
            
            
            
            
            # DELETE USER
            urlDEL = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/persona.png?raw=true"
            responseUser = requests.get(urlDEL)
            image_dataUser = io.BytesIO(responseUser.content)
            
            icon_imageUser = ctk.CTkImage(dark_image=Image.open(image_dataUser), size=(20, 20))

            button_DEL_Purchase = ctk.CTkButton(
                                               frame_Login_Done,
                                                text="Update User",
                                                fg_color='#1F5673',
                                                compound="right",
                                                image=icon_imageUser,
                                                width=25)
            button_DEL_Purchase.grid(row=3, column=1, columnspan=2, pady=(30,30), padx=50)
                                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
         



            
            

            
            
            
            
            # labelWelcomeBack =  ctk.CTkLabel(root_tk, text="Bienvenido!", text_color="white")
            # labelWelcomeBack.grid(row=0, column=0)
            
            
            
        else:
            # If  the email doesn't exits on db, show the error message
            MessagesFrame_Generation("NO existes en la DB", Color_Error_incorrect, color_text_Message)
            
            # Clean the windows (Root) and then gonna move the cx to create a new user
            root_tk.after(1000,  lambda: clear_frame(root_tk))
            root_tk.after(1000,  Create_email)

    else: 
        # If format of the email is not valid, gonna  show the error message
        MessagesFrame_Generation("Formato de email invalido", Color_Error_incorrect, color_text_Message)
        
      

# Create Frame_Windows (Root)
frame = ctk.CTkFrame(master=root_tk, width=400, height=600)
frame.pack()

# Label Title of the program
label = ctk.CTkLabel(frame, text="CustomerPurchaseManager", fg_color="transparent", font=("Arial", 25))
label.grid(row=1, column=0, columnspan=3, pady=40, padx=20)

# Label  to put the email
Email_STR = ctk.StringVar()
entry = ctk.CTkEntry(frame, placeholder_text="Email", textvariable=Email_STR, width=200)
entry.grid(row=2, column=0, columnspan=3, pady=(0,20))

# Button to login
button_Login = ctk.CTkButton(frame, text="Login", fg_color=("#DB3E39", "#821D1A"), command=on_login)
button_Login.grid(row=3, column=0, columnspan=3, pady=(0,20))

# Ejecutar el bucle principal
root_tk.mainloop()
