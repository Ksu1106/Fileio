from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests

def upliad():
    filepath = fd.askopenfilename()
    if filepath:
        files={'file': open(filepath, 'rb')}
        response = requests.post('https://www.file.io',files = files)
        if response.status_code==200:
             link = response.json()['link']
            entry.insert(0,link)


window = Tk()
window.title()
window.geometry('400x200')

buton = ttk.Button(text='Загрузить файл',command=upliad)
buton.pack()

entry= ttk.Entry
entry.pack()

window.mainloop()