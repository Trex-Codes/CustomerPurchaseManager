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


            # Create a frame on the right side of the window
            right_frame = ctk.CTkFrame(root_tk, width=300, height=400, fg_color="#2B2B2B")  # Set background color to make it visible
            right_frame.place(x=0, y=0)  # Frame positioned on the right half of the window

            # Create a frame on the right side of the window
            right_frame = ctk.CTkFrame(root_tk, width=200, height=300, fg_color="#242424")  # Set background color to make it visible
            right_frame.place(x=50, y=50)  # Frame positioned on the right half of the window




            # Fetch the image icon (e.g., a small icon from a URL)
            image_url = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/Addcompra.png?raw=true"  # Example URL, replace with your icon URL
            response = requests.get(image_url)
            icon_data = BytesIO(response.content)

            # Load and resize the image icon
            icon_image = Image.open(icon_data)
            icon_image_resized = icon_image.resize((20, 20))  # Resize the icon to a smaller size
            icon_photo = ImageTk.PhotoImage(icon_image_resized)

            login_button = ctk.CTkButton(right_frame, text="Add purchase", width=150, fg_color="#5AAA95", command=func, image=icon_photo, compound="right")
            login_button.place(x=20, y=30)  # Position the entry relative to the frame


            # Fetch the second image icon from the new URL (Delcompra.png)
            image_url_delete = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/Delcompra.png?raw=true"
            response_delete = requests.get(image_url_delete)
            icon_data_delete = BytesIO(response_delete.content)

            # Load and resize the image icon
            icon_image_delete = Image.open(icon_data_delete)
            icon_image_resized_delete = icon_image_delete.resize((20, 20))  # Resize the icon to a smaller size
            icon_photo_delete = ImageTk.PhotoImage(icon_image_resized_delete)
            

            login_button = ctk.CTkButton(right_frame, text="Delete Purchase", width=150, fg_color="#5AAA95", command=func, image=icon_photo_delete, compound="right")
            login_button.place(x=20, y=100)  # Position the entry relative to the frame



            # Fetch the image icon for "View Purchases" from URL (bolsa.png)
            image_url_view = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/bolsa.png?raw=true"
            response_view = requests.get(image_url_view)
            icon_data_view = BytesIO(response_view.content)

            # Load and resize the image icon
            icon_image_view = Image.open(icon_data_view)
            icon_image_resized_view = icon_image_view.resize((20, 20))  # Resize the icon to a smaller size
            icon_photo_view = ImageTk.PhotoImage(icon_image_resized_view)

            login_button = ctk.CTkButton(right_frame, text="View purchases", width=150, fg_color="#5AAA95", command=func, image=icon_photo_view, compound="right")
            login_button.place(x=20, y=170)  # Position the entry relative to the frame   


            
                        # Fetch the image icon for "User Profile" from URL (persona.png)
            image_url_persona = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/persona.png?raw=true"
            response_persona = requests.get(image_url_persona)
            icon_data_persona = BytesIO(response_persona.content)

            # Load and resize the image icon
            icon_image_persona = Image.open(icon_data_persona)
            icon_image_resized_persona = icon_image_persona.resize((20, 20))  # Resize the icon to a smaller size
            icon_photo_persona = ImageTk.PhotoImage(icon_image_resized_persona)  

            login_button = ctk.CTkButton(right_frame, text="", width=50, height=40, fg_color="#FFD639", command=func, image=icon_photo_persona)
            login_button.place(x=40, y=230)  # Position the entry relative to the frame      


                        # Fetch the image icon for "Delete User" from URL (DelUser.png)
            image_url_del_persona = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/DelUser.png?raw=true"
            response_del_persona = requests.get(image_url_del_persona)
            icon_data_del_persona = BytesIO(response_del_persona.content)

            # Load and resize the image icon
            icon_image_del_persona = Image.open(icon_data_del_persona)
            icon_image_resized_del_persona = icon_image_del_persona.resize((20, 20))  # Resize the icon to a smaller size
            icon_photo_del_persona = ImageTk.PhotoImage(icon_image_resized_del_persona)

            login_button = ctk.CTkButton(right_frame, text="", width=50, height=40, fg_color="#F45B69", command=func,image=icon_photo_del_persona )
            login_button.place(x=110, y=230)  # Position the entry relative to the frame                 
                   



            

       
                        
      
      

def welcome():
            # If  the email is already registered, show the welcome  message
            clear_frame(root_tk)
            
            # Fetch image from URL
            image_url = "https://github.com/Trex-Codes/CustomerPurchaseManager/blob/Features/Assets/login.jpg?raw=true"
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
            label.place(x=330, y=30)  # Frame positioned on the right half of the window


            # Create a frame for login section (button and text)
            Login_frame = ctk.CTkFrame(root_tk, width=250, height=160, fg_color="#242424")  # Set background color to make it visible
            Login_frame.place(x=330, y=80)  # Position the frame on the window

            # Label Title of the program
            label = ctk.CTkLabel(Login_frame, text="Email", fg_color="#242424", font=("Helvetica", 13), text_color="#8e9091")
            label.place(x=25, y=5)  # Frame positioned on the right half of the window


            # Label to put the email (using CTkEntry for input)
            Email_STR = ctk.StringVar()
            entry = ctk.CTkEntry(Login_frame, placeholder_text="Email", textvariable=Email_STR, width=200)
            entry.place(x=25, y=30)  # Position the entry relative to the frame

            login_button = ctk.CTkButton(Login_frame, text="Login", width=150, fg_color="#5DA1FA", command=func)
            login_button.place(x=50, y=80)  # Position the entry relative to the frame










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
