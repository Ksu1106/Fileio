from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import pyperclip



def upliad():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files={'file': f}
                response = requests.post('https://file.io',files = files)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0,END)
                entry.insert(0,link)
                pyperclip.copy(link)
                mb.showinfo('Ссылка скопирована',f'Ссылка:\n{link}\nскопирована в буфер обмена')
    except Exception as e:
        mb.showerror('Ошибка',f'Произошла ошибка: {e}')

window = Tk()
window.title()
window.geometry('400x200')

buton = ttk.Button(text='Загрузить файл',command=upliad)
buton.pack()

entry= ttk.Entry()
entry.pack()

window.mainloop()