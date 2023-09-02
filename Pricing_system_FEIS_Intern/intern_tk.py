
import tkinter as tk
from tkinter import ttk

def on_tab_change(event):
    # This function will be called when the user changes the tab
    selected_tab = tab_control.index(tab_control.select())
    print(f"Selected tab: {selected_tab}")

# Create the main application window
win = tk.Tk()
win.title("Four Tabs Interface")

# Create a Notebook (tabs container)
tab_control = ttk.Notebook(win)

# Create the four tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

# Add tabs to the Notebook
tab_control.add(tab1, text="Tab 1")
tab_control.add(tab2, text="Tab 2")
tab_control.add(tab3, text="Tab 3")
tab_control.add(tab4, text="Tab 4")

# Pack the Notebook to make it visible
tab_control.pack(expand=1, fill="both")

# Content for each tab (you can customize this according to your needs)
label1 = tk.Label(tab1, text="This is Tab 1 content")
label1.pack(padx=10, pady=10)

label2 = tk.Label(tab2, text="This is Tab 2 content")
label2.pack(padx=10, pady=10)

label3 = tk.Label(tab3, text="This is Tab 3 content")
label3.pack(padx=10, pady=10)

label4 = tk.Label(tab4, text="This is Tab 4 content")
label4.pack(padx=10, pady=10)

# Bind the event when the tab is changed
tab_control.bind("<<NotebookTabChanged>>", on_tab_change)

# Start the application main loop
win.mainloop()
