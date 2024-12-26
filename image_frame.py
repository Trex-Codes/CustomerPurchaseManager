import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Initialize window
root_tk = ctk.CTk()
root_tk.title("Responsive Window")
root_tk.geometry("600x400")  # 600x400 window size

# Fetch image from URL
image_url = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/imagen.jpeg?raw=true"
response = requests.get(image_url)
image_data = BytesIO(response.content)

# Load the original image
bg_image = Image.open(image_data)

# Resize the image to fit the left half of the window (300px width, full height)
bg_image_resized = bg_image.resize((300, 400))  # Half the width of the window, full height
bg_photo = ImageTk.PhotoImage(bg_image_resized)

# Add background image label to the left side of the window
left_image_label = ctk.CTkLabel(root_tk, image=bg_photo, text="", width=300, height=400)
left_image_label.place(x=0, y=0)  # Left image, occupying the left half of the window

# Create a frame on the right side of the window
right_frame = ctk.CTkFrame(root_tk, width=300, height=400)  # Set background color to make it visible
right_frame.place(x=300, y=0)  # Frame positioned on the right half of the window

# Label Title of the program
label = ctk.CTkLabel(root_tk, text="CustomerPurchaseManager", fg_color="#2B2B2B", font=("Arial", 20))
label.place(x=330, y=10)  # Frame positioned on the right half of the window


# Create a frame for login section (button and text)
Login_frame = ctk.CTkFrame(root_tk, width=250, height=200, fg_color="#242424")  # Set background color to make it visible
Login_frame.place(x=330, y=80)  # Position the frame on the window

# Label Title of the program
label = ctk.CTkLabel(Login_frame, text="Email", fg_color="#242424", font=("Helvetica", 15), text_color="#8e9091")
label.place(x=25, y=5)  # Frame positioned on the right half of the window


# Label to put the email (using CTkEntry for input)
Email_STR = ctk.StringVar()
entry = ctk.CTkEntry(Login_frame, placeholder_text="Email", textvariable=Email_STR, width=200)
entry.place(x=25, y=30)  # Position the entry relative to the frame

login_button = ctk.CTkButton(Login_frame, text="Login", width=150)
login_button.place(x=50, y=80)  # Position the entry relative to the frame




# Run the main loop
root_tk.mainloop()


