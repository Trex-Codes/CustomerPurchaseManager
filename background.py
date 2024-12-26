import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Clear widgets of the main window after to verify the email or create a new user
def clear_frame(Window):
    for widget in Window.winfo_children():
        widget.destroy()  # Ocultar cada widget en el fracme

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




def func():
      # If  the email is already registered, show the welcome  message
            clear_frame(root_tk)
            
      
      

def welcome():
            # If  the email is already registered, show the welcome  message
            clear_frame(root_tk)
            
            frame_Login_Done = ctk.CTkFrame(master=root_tk, width=270, height=250)
            # frame_Login_Done.grid(row=0, column=0, pady=50, padx=50)
            frame_Login_Done.place(relx=0.5, rely=0.5, anchor="center")

            # Label Title of the program
            label = ctk.CTkLabel(frame_Login_Done, text="CustomerPurchaseManager", fg_color="transparent", font=("Arial", 25))
            label.grid(row=1, column=0, columnspan=3, pady=40, padx=20)

            # Label  to put the email
            Email_STR = ctk.StringVar()
            entry = ctk.CTkEntry(frame_Login_Done, placeholder_text="Email", textvariable=Email_STR, width=200)
            entry.grid(row=2, column=0, columnspan=3, pady=(0,20))

            # Button to login
            button_Login = ctk.CTkButton(frame_Login_Done, text="Login", fg_color=("#DB3E39", "#821D1A"), command=func)
            button_Login.grid(row=3, column=0, columnspan=3, pady=(0,20))









# Initialize window
root_tk = ctk.CTk()
root_tk.title("Responsive Window")
root_tk.geometry("600x400")

# Fetch image from URL
image_url = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/imagen.jpeg?raw=true"
response = requests.get(image_url)
image_data = BytesIO(response.content)

# Load the original image
bg_image = Image.open(image_data)

# Create a Frame with the background image
bg_image_resized = bg_image.resize((600, 400))  # Initially adjust the size of the image
bg_photo = ImageTk.PhotoImage(bg_image_resized)

background_frame = ctk.CTkFrame(root_tk)
background_frame.place(x=0, y=0, relwidth=1, relheight=1)

background_label = ctk.CTkLabel(background_frame, image=bg_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a responsive button
button = ctk.CTkButton(root_tk, text="click me", fg_color="#5DA1FA", command=welcome)
button.place(relx=0.5, rely=0.5, anchor="center")

# Adjust the position of the Label to be lower
label = ctk.CTkLabel(root_tk, text="Welcome Back to Our Website!")
label.place(relx=0.5, rely=0.4, anchor="center")

# Bind the resize event to update the background
root_tk.bind("<Configure>", update_background)

# Run the main loop
root_tk.mainloop()
