import customtkinter as ctk
import re
import mysql.connector
import sys
import io
import time

# Configuration of Output a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Global Variables
Error_Email = None  # Declarar Error_Email globalmente
Frame_Error = None  # Declarar Frame_Error globalmente

# Connection DB MYSQL
mydb = mysql.connector.connect(
    host="192.168.1.13",
    user="UserLaptop",
    password="sebasmesi1305",
    database="company"
)
mycursor = mydb.cursor()

# pattern email for regex 
def Validation_email(email_patter):
    pattern = r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$"
    return re.match(pattern, email_patter) is not None

    
# Clear widgets of the main window after to verify the email or create a new user
def clear_frame(Window):
    for widget in Window.winfo_children():
        widget.pack_forget()  # Ocultar cada widget en el fracme

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create main Windows (Root)
root_tk = ctk.CTk()
root_tk.geometry("500x550")

# Create Frame_Windows (Root)
frame = ctk.CTkFrame(master=root_tk, width=400, height=600)
frame.pack()

def Create_email():
    
    def Create_Account():
        
        list_Items_CX_NEW = [FullName_CreateSTR.get(), Age_CreateSTR.get(),  Phone_CreateSTR.get(), Email_STR.get(), select_Option_City.get(), Address_CreateSTR.get()]
        if any(not items for items in list_Items_CX_NEW):
                print(list_Items_CX_NEW)
                
                # Configura el marco para la parte inferior
                bottom_frame = ctk.CTkFrame(master=root_tk)
                bottom_frame.grid(row=1, column=0, sticky="ew") 

                # Configura el Label en el frame inferior
                Error_Email = ctk.CTkLabel(bottom_frame, text="Campos vacíos", fg_color="red", font=("Arial", 15), height=50, text_color="purple")
                Error_Email.pack(fill=ctk.X, side=ctk.BOTTOM)  

                # Configura el peso de la fila y la columna para ocupar todo el espacio
                root_tk.grid_columnconfigure(0, weight=1)
                root_tk.grid_rowconfigure(0, weight=1)  # Asegúrate de que la fila 0 tiene peso
        else: 
            # query to insert the new information of the client on the DB 
            query = "INSERT INTO cliente (nombre, edad, telefono, email, ciudad, direccion) VALUES (%s, %s, %s, %s, %s, %s);"
            mycursor.execute(query,  list_Items_CX_NEW)
            mydb.commit()
            
            # Configura el marco para la parte inferior
            bottom_frame = ctk.CTkFrame(master=root_tk)
            bottom_frame.grid(row=1, column=0, sticky="ew") 

            # Configura el Label en el frame inferior
            Error_Email = ctk.CTkLabel(bottom_frame, text="Register (s) inserted in right way!", fg_color="lightgreen", font=("Arial", 15), height=50, text_color="purple")
            Error_Email.pack(fill=ctk.X,  side=ctk.BOTTOM) 
            
            # Configura el peso de la fila y la columna para ocupar todo el espacio
            root_tk.grid_columnconfigure(0, weight=1)
            root_tk.grid_rowconfigure(0, weight=1)  # Asegúrate de que la fila 0 tiene peso

            # Clean the windows (Root) and then gonna move the cx to create a new user
            root_tk.after(1000,  lambda: clear_frame(root_tk))
            # root_tk.after(1000,  on_login)
            exit()
        
            
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
    
    
    # ----------------- MUST BE A LIST  OF OPTIONS  ----------------- 
    # label  city   
    label_city = ctk.CTkLabel(frame_create_Email, text="City:")
    label_city.grid(row=5, column=0, pady=(0,30))
    # Entry  city
    select_Option_City = ctk.StringVar(value="Options")
    options = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Cúcuta", 
    "Bucaramanga", "Pereira", "Manizales", "Ibagué", "Santa Marta", 
    "Villavicencio", "Pasto", "Montería", "Neiva", "Armenia", "Sincelejo", 
    "Valledupar", "Popayán", "Tunja", "Riohacha", "Florencia", "Quibdó", 
    "Yopal", "San Andrés", "Leticia", "Mocoa", "Puerto Carreño", 
    "San José del Guaviare", "Inírida"
]

    Label_Option_city = ctk.CTkOptionMenu(frame_create_Email, variable=select_Option_City, values=options)
    Label_Option_city.grid(row=5, column=1, padx=(5,20), pady=(0,30))
    
    # Label address
    label_address = ctk.CTkLabel(frame_create_Email, text="Address:")
    label_address.grid(row=6, column=0, pady=(0,30))
    # Entry  address
    Address_CreateSTR = ctk.StringVar()
    entry_address = ctk.CTkEntry(frame_create_Email, width=150, placeholder_text="Address:", textvariable=Address_CreateSTR)
    entry_address.grid(row=6, column=1, padx=(5,20), pady=(0,30))
    
    # Button create Account (Sign yp)
    button_Create_Email = ctk.CTkButton(frame_create_Email, text="Sign up", fg_color=("#DB3E39", "#821D1A"), command=Create_Account)
    button_Create_Email.grid(row=7, column=0, columnspan=3, padx=(5,20), pady=(0,30))
    
    
    
    
     
    


# function start or login into the  system
def on_login():
    global Error_Email  # Global variable
    global Frame_Error 
    
    email_verify = Email_STR.get()
    # email_verify = "sdfsdf@gmail.oil.es"

    # Delete frame and label of error when the format is not valid at the email
    # Verify if those  fields are not empty, if they are  empty nothing happend
    # but is those variables already appear on the screen, they gonna be deleted
    if Error_Email is not None and Frame_Error is not None:
        Error_Email.destroy()
        Frame_Error.destroy()

    if Validation_email(email_verify):  # Valid Email
        
        # Verify that the email  is already registered on the DB
        query = "SELECT * FROM cliente WHERE email = %s"
        mycursor.execute(query, (email_verify,))
        result = mycursor.fetchall()    

        if len(result) > 0:
            
            # If  the email is already registered, show the welcome  message
            new_window = ctk.CTkToplevel(root_tk)  
            new_window.title("Hola")
            new_window.geometry("300x200")
            # clear_frame()  # Clear the widgets of the main windows (Root)
            ctk.CTkLabel(new_window, text="Bienvenido!", font=("Arial", 20)).pack(pady=20)
        else:
            # If  the email doesn't exits on db, show the error message
            Frame_Error = ctk.CTkFrame(master=root_tk, width=200, height=60)
            Frame_Error.pack(side=ctk.BOTTOM, fill=ctk.X)
            
            Error_Email = ctk.CTkLabel(Frame_Error, text="No existe el correo en la base de datos", 
                                   fg_color="red", font=("Arial", 15), height=50, text_color="purple")
            Error_Email.pack(fill=ctk.X) 
            
            # Clean the windows (Root) and then gonna move the cx to create a new user
            root_tk.after(1000,  lambda: clear_frame(root_tk))
            root_tk.after(1000,  Create_email)

    else: 
        # If format of the email is not valid, gonna  show the error message
        
        Frame_Error = ctk.CTkFrame(master=root_tk, width=200, height=60)
        Frame_Error.pack(side=ctk.BOTTOM, fill=ctk.X)
        
        Error_Email = ctk.CTkLabel(Frame_Error, text="Formato de Correo inválido, intenta nuevamente", 
                               fg_color="red", font=("Arial", 15), height=50)
        Error_Email.pack(fill=ctk.X) 


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
