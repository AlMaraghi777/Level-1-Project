import matplotlib.pyplot as plt
import csv
import mplcursors
from pathlib import Path

def read_data(file_path):
    names = []
    times = []
    colours = []
    
    lower_boundary = 15.0
    upper_boundary = 85.0
    
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row.get('Name')

                time = float(row.get('Time (Seconds)'))
                names.append(name)
                times.append(time)
                if time < lower_boundary:
                    colours.append('lime')
                elif time > upper_boundary:
                    colours.append('red')
                else:
                    colours.append('black')
                    
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except ValueError as e:
        print(f"Invalid data: {e}")
        
    return names, times, colours

def plot_data(names, times, colours):
    plt.figure(figsize=(18, 10))
    scatter = plt.scatter(names, times, color=colours, marker='o', s=50)
    mplcursors.cursor(scatter, hover=True)
    plt.xlabel('Name', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Scatter Plot', fontsize=14)
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout(pad=2)
    plt.show()

file_path = Path('data.csv')

try:
    names, times, colours = read_data(file_path)
    plot_data(names, times, colours)
except Exception as e:
    print(f"Error: {e}")
