from posix import listdir
from tkinter import filedialog
from tkinter import *
from PIL import Image
import os

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
folder_location = '/'.join(folder_selected.split('/')[0:-1])
folder_name = folder_selected.split('/')[-1]
size = simpledialog.askstring("Figure size", "What's the size?",parent=root)
size = int(size)
folder_to_save = folder_location+"/"+folder_name+"_"+str(size)
print(folder_to_save)
os.mkdir(folder_to_save)


for file in listdir(folder_selected):
    if file.endswith((".png","jpg")):
        print(file+" resized")
        image = Image.open(folder_selected+f"/{file}")
        image.thumbnail((size,size))
        image.save(f"{folder_to_save}/{file}")

