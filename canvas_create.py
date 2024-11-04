import customtkinter as ctk

# Configuración de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Crear la ventana principal
root = ctk.CTk()

# Variable para almacenar la opción seleccionada
selected_option = ctk.StringVar(value="Opción 1")  # Valor inicial

# Crear el CTkOptionMenu
options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
option_menu = ctk.CTkOptionMenu(root, variable=selected_option, values=options)
option_menu.pack(pady=20)  # Agregar el menú a la ventana

# Función para mostrar la opción seleccionada
def show_selection():
    print(f"Opción seleccionada: {selected_option.get()}")

# Botón para mostrar la opción seleccionada
button = ctk.CTkButton(root, text="Mostrar Selección", command=show_selection)
button.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
