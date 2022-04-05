#module for running DOS command 
import subprocess
#modules for opening a file dialog
import tkinter as tk
from tkinter import filedialog

#open file dialog to determine path to lab file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

#run mongoimport command in shell
command = f'mongoimport --host localhost --db traveldb --collection cities --file "{file_path}" --jsonArray'
print(command)
try:
    subprocess.check_output(command, shell=True).decode()    
except subprocess.CalledProcessError as e:
    print (e.output)
