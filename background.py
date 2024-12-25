import customtkinter as ctk
from PIL import Image, ImageTk

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
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Responsive Window")
app.geometry("600x400")

# Local image path
image_path = r"C:/Users/USUARIO/Downloads/IMAGEN.jpeg"  # Make sure to use 'r' for paths in Windows

# Load the original image
bg_image = Image.open(image_path)

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

# The Label should have no background
label.configure(fg_color="transparent", text_color="white")  # Transparent background, white text

# Bind the resize event to update the background
app.bind("<Configure>", update_background)

# Run the main loop
app.mainloop()
