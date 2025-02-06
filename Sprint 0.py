#GUI
import tkinter as tk
from tkinter import ttk

def on_checkbox_toggle():
    print("Checkbox toggled")

def on_radio_button():
    print("Radio button selected")
#Initialize the main application window
root = tk.Tk()
root.title("SOS GUI")
root.geometry("300x200")
#Create a label for the GUI
label = tk.Label(root, text="SOS Game GUI")
label.pack()
#Create a canvas with a horizontal line
canvas = tk.Canvas(root, width=200, height=10)
canvas.pack()
canvas.create_line(0, 5, 200, 5)
#Create a checkbox with an event handler
checkbox = tk.Checkbutton(root, text="Enable Advanced Mode", command=on_checkbox_toggle)
checkbox.pack()
#create radio button with event handelers
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="1", command=on_radio_button)
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="2", command=on_radio_button)
radio1.pack()
radio2.pack()
#Run the tkinter vent loop
root.mainloop()


#Unit Tests
import unittest
import tkinter as tk

class TestSOSGui(unittest.TestCase):
    
    def setUp(self):
        #create a tkinter root window for testing
        self.root = tk.Tk()
        self.root.title("SOS GUI Test")
        self.checkbox = tk.Checkbutton(self.root, text="Enable Advanced Mode") #Create a checkbox widget
        self.checkbox.pack()
        self.radio_var = tk.StringVar()
        self.radio1 = tk.Radiobutton(self.root, text="Option 1", variable=self.radio_var, value="1")
        self.radio2 = tk.Radiobutton(self.root, text="Option 2", variable=self.radio_var, value="2")
        self.radio1.pack()
        self.radio2.pack()
    
    def test_checkbox_exists(self): #Test if the checkbox is created successfully
        self.assertIsNotNone(self.checkbox, "Checkbox should be created")
    
    def test_radio_buttons_exist(self): #Test if the radio button are created successfully
        self.assertIsNotNone(self.radio1, "Radio button 1 should be created")
        self.assertIsNotNone(self.radio2, "Radio button 2 should be created")

if __name__ == '__main__':
    unittest.main()



