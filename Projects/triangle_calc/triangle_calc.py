'''
Triangle Calculator

- Area
- Perimeter
'''
# Using tkinter fo GUI
import tkinter as tk

# Initializes window
window = tk.Tk()

# Set Size of Window
window.geometry("800x600")

# Set Title of Window
window.title("Forrest's Triangle Calculator")

# Top Text
label = tk.Label(master=window, text="Welcome to the Triangle Zone", font=('Arial', 18))
label.pack(padx=10, pady=10)

# Initialize Grid 3x3
frame = tk.Frame(window)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=1)
frame.columnconfigure(2,weight=1)

# Side Size Entry Boxes
side_one = tk.Entry(frame)
side_one.grid(row=1, column=0, padx=10, pady=10)

side_two = tk.Entry(frame)
side_two.grid(row=1, column=1, padx=10, pady=10)

side_three = tk.Entry(frame)
side_three.grid(row=1, column=2, padx=10, pady=10)

# Buttons
btn1 = tk.Button(frame, text="Perimeter", font=('Arial', 12))
btn1.grid(row=2, column=0, padx=10, pady=10)
btn2 = tk.Button(frame, text="Area", font=('Arial', 12))
btn2.grid(row=2, column=2, padx=10, pady=10)

frame.pack()





# Starts the Program
window.mainloop()
















