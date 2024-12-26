import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def update_background(event):
    # Get the current window size
    width = event.width
    height = event.height

    # Resize the background image
    bg_image_resized = bg_image.resize((width, height))
    bg_photo = ImageTk.PhotoImage(bg_image_resized)

    # Update the background image in the Label
    background_label.configure(image=bg_photo)
    background_label.image = bg_photo  # Keep a reference to the image

# Initialize window

app = ctk.CTk()
app.title("Responsive Window")
app.geometry("600x400")

# Fetch image from URL
image_url = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/imagen.jpeg?raw=true"
response = requests.get(image_url)
image_data = BytesIO(response.content)

# Load the original image
bg_image = Image.open(image_data)

# Create a Frame with the background image
bg_image_resized = bg_image.resize((600, 400))  # Initially adjust the size of the image
bg_photo = ImageTk.PhotoImage(bg_image_resized)

background_frame = ctk.CTkFrame(app)
background_frame.place(x=0, y=0, relwidth=1, relheight=1)

background_label = ctk.CTkLabel(background_frame, image=bg_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a responsive button
button = ctk.CTkButton(app, text="click me")
button.place(relx=0.5, rely=0.5, anchor="center")

# Adjust the position of the Label to be lower
label = ctk.CTkLabel(app, text="Welcome Back to Our Website!")
label.place(relx=0.5, rely=0.4, anchor="center")


# Bind the resize event to update the background
app.bind("<Configure>", update_background)

# Run the main loop
app.mainloop()
