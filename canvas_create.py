import requests
from PIL import Image
from io import BytesIO
import customtkinter as ctk

def main():
    # URL de la imagen RAW
    url = "https://raw.githubusercontent.com/Trex-Codes/CustomerPurchaseManager/Features/Assets/Addcompra.png"

    # Crear la ventana principal
    root = ctk.CTk()
    root.geometry("400x300")  # Configura el tamaño de la ventana

    # Crear un frame para el botón
    frame_Login_Done = ctk.CTkFrame(root)
    frame_Login_Done.pack(pady=20)

    # Obtener la imagen de forma remota
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        
        # Usar la imagen en el botón
        icon_image = ctk.CTkImage(dark_image=image, size=(20, 20))
        button_ADD_Purchase = ctk.CTkButton(
            frame_Login_Done,
            text="",
            fg_color='#1F5673',
            compound="right",
            image=icon_image,
            width=25
        )
        button_ADD_Purchase.grid(row=3, column=1, pady=(0, 40), padx=50)
    else:
        print("Error al cargar la imagen:", response.status_code)

    root.mainloop()

if __name__ == "__main__":
    main()
