import customtkinter as ctk

# Initialize the window
root_tk = ctk.CTk()
root_tk.geometry("400x200")

# Create a CTkLabel with a specific font
label1 = ctk.CTkLabel(root_tk, text="Arial, 16px, normal", font=("Arial", 16))
label1.pack(pady=10)

label2 = ctk.CTkLabel(root_tk, text="Helvetica, 18px, bold", font=("Helvetica", 18, "bold"))
label2.pack(pady=10)

label3 = ctk.CTkLabel(root_tk, text="Times New Roman, 20px, italic", font=("Times New Roman", 20, "italic"))
label3.pack(pady=10)

label4 = ctk.CTkLabel(root_tk, text="Courier, 14px, underline", font=("Courier", 14, "underline"))
label4.pack(pady=10)

# Run the main loop
root_tk.mainloop()
