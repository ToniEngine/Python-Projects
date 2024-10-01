import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Changing Text")

# Texts to display
texts = ["First Text", "Second Text", "Third Text", "Fourth Text"]
index = 0  # Index to track current text

# Label to display the text
label = tk.Label(root, text="", font=("Helvetica", 24))
label.pack(pady=20)

# Function to update the text
def change_text():
    global index
    label.config(text=texts[index])
    index = (index + 1) % len(texts)  # Loop back to the first text
    root.after(2000, change_text)  # Change text every 2 seconds

# Call the function to start changing text
change_text()

# Run the Tkinter event loop
root.mainloop()
