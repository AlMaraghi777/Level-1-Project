import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load data
df = pd.read_csv("Data.csv")
df["Time"] = df["Time"].astype(float)

# All the units of different parameters measured
units = {
    "Time":"Second",#Interval time
}

def update_plot():
    ax.clear()
    if df.empty or "Name" not in df.columns or "Time" not in df.columns:
        ax.set_title("No data available")
    else:
        ax.bar(df["Name"],df["Time"],color='skyblue')
        ax.set_title("Radio Signal Analysis")
        ax.set_xlabel("Name")
        ax.set_ylabel(f"{'Time'} ({units['Time']})")
        #Avoid duplication of names
        ax.set_xticks(range(len(df["Name"]))) 
        ax.set_xticklabels(df["Name"], rotation=90, fontsize=8) 
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Results Graphed")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8,5))

# Create a canvas for the plot
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a dropdown menu
dropdown = ttk.Combobox(root, values=["Time"])
dropdown.current(0)  # Set default value
dropdown.pack(side=tk.BOTTOM)

# Bind the dropdown menu to the update function
dropdown.bind("<<ComboboxSelected>>", lambda event: update_plot())

# Call update_plot once to initialize the plot
update_plot()

# Start the Tkinter main loop
root.mainloop() 