import customtkinter as ctk

# Crear la ventana principal
root_tk = ctk.CTk()
root_tk.geometry("500x450")  # Establecer el tamaño de la ventana

# Crear el Label y ubicarlo en la parte inferior
label = ctk.CTkLabel(root_tk, text='Este es un Label en la parte inferior', font=('Arial', 20))
label.pack(side=ctk.BOTTOM, pady=20)  # El padding (pady) agrega espacio vertical alrededor del Label

# Ejecutar el loop principal
root_tk.mainloop()
