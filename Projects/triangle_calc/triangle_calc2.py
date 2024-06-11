import tkinter as tk

class MyCalc:

  def __init__(self):

    self.root = tk.Tk()

    self.label = tk.Label(self.root, text='Messege', font=('Arial', 14))
    self.label.pack(padx=10, pady=10)

    self.textbox = tk.Text(self.root, height=5, font=('Arial'))
    self.textbox.pack(padx=10, pady=10)

    self.button = tk.Button(self.root, text='Test', font=('Arial', 18))
    self.button.pack(padx=10, pady=10)

    self.root.mainloop()

def show_messege(self):
  print('Test')


MyCalc()




