import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Example function to be executed on button press
def func():
    print("Add Purchase Button Clicked")

# Initialize the window
root_tk = ctk.CTk()
root_tk.title("Add Purchase Example")
root_tk.geometry("600x400")

# Fetch the image icon (e.g., a small icon from a URL)
image_url = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/Addcompra.png?raw=true"  # Example URL, replace with your icon URL
response = requests.get(image_url)
icon_data = BytesIO(response.content)

# Load and resize the image icon
icon_image = Image.open(icon_data)
icon_image_resized = icon_image.resize((20, 20))  # Resize the icon to a smaller size
icon_photo = ImageTk.PhotoImage(icon_image_resized)

# Add a CTkButton with both an icon and text
login_button = ctk.CTkButton(right_frame, 
                              text="Add Purchase", 
                              width=150, 
                              fg_color="#5DA1FA", 
                              command=func,
                              image=icon_photo,  # Set the icon on the button
                              compound="right")   # Position the icon to the left of the text

# Place the button inside the frame
login_button.place(x=20, y=30)

# Run the main loop
root_tk.mainloop()
