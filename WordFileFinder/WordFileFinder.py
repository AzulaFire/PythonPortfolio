import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import customtkinter as ctk
from datetime import datetime

date_time = datetime.now().strftime('%Y%m%d')

#SETTINGS --------------------------------------------------

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

window = ctk.CTk()
window.title('Word File Finder')
window.configure(width=900, height=740, padx=40, pady=20)
# window.resizable(0, 0)
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x, y)) # This part is used for window location

#GLOBALS --------------------------------------------------

wordList = [
    'Test 1',
    'Test 2',
    'Test 3',
    5,
    'Number'
]

#FUNCTIONS --------------------------------------------------

def clearList():
    wordList.clear()
    listBox.delete(0, tk.END)

def addWord():
    newWord = txt_AddWord.get()
    if len(newWord) > 0:
        if newWord not in wordList:
            wordList.append(newWord)
            listBox.delete(0, tk.END)
            for item in wordList:
                listBox.insert(tk.END, item)
            txt_AddWord.delete(0, tk.END)

def deleteWord():
    delWord = listBox.selection_get()
    wordList.remove(delWord)
    listBox.delete(0, tk.END)
    for item in wordList:
        listBox.insert(tk.END, item)

def setBase():
    dir = fd.askdirectory()
    txt_Base.insert(0, dir)

def setSaveLocation():
    dir = fd.askdirectory()
    txt_SaveLocation.insert(0, dir)
    savePath = txt_SaveLocation.get()
    if len(savePath) > 0:
        if os.path.exists(f'{savePath}/SearchLog_{date_time}.txt'):
            os.remove(f'{savePath}/SearchLog_{date_time}.txt')

def search():
    dirPath = txt_Base.get()
    savePath = txt_SaveLocation.get()
    count = 0
    if len(dirPath) > 0 and len(savePath) > 0:
        for subdir, dirs, files in os.walk(dirPath):
            for file in files:
                filePath = os.path.join(subdir, file)
                with open(filePath) as cf:
                    for index, line in enumerate(cf):
                        for word in wordList:
                            if word in line:
                                count += 1
                                #print(file, index, line)
                                with open(f'{savePath}/SearchLog_{date_time}.txt', 'a') as sf:
                                    sf.write(f'File: {file} [Line: {index}] - {line}')
    if count > 1:
        lbl_Message.configure(text = f'   Process Completed: {count} Found.   ', fg_color='green')


#GUI --------------------------------------------------

l_frame = ctk.CTkFrame(window)
r_frame = ctk.CTkFrame(window)
b_frame = ctk.CTkFrame(window)

l_frame.grid(row=0, column=0, padx=20, sticky='nsew')
r_frame.grid(row=0, column=1, padx=20, sticky='nsew')
b_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky='nsew')

ctk.CTkLabel(l_frame, text='Word Search List').grid(row=1, column=1, pady=10, sticky='w')

listBox = tk.Listbox(l_frame, height=10, font='Arial, 16', width=30)
listBox.grid(row=2, column=1, sticky='w')
scrollbar = ctk.CTkScrollbar(l_frame, command=listBox.yview)
scrollbar.grid(row=2, column=2, sticky='ns')
listBox.configure(yscrollcommand=scrollbar.set)

for item in wordList:
    listBox.insert(tk.END, item)

ctk.CTkLabel(r_frame, text='').grid(row=1, column=2, pady=10, sticky='w')
txt_AddWord = ctk.CTkEntry(r_frame, width=200)
txt_AddWord.grid(row=2, column=0, padx=50, pady=10, sticky='w')
btn_AddWord = ctk.CTkButton(r_frame, text='Add Word', command=addWord, width=200).grid(row=3, column=0, padx=50, pady=10, sticky='e')
btn_DelWord = ctk.CTkButton(r_frame, text='Delete Word', command=deleteWord, width=200).grid(row=4, column=0, padx=50, pady=10, sticky='e')
btn_ClearList = ctk.CTkButton(r_frame, text='Clear List', command=clearList, width=200).grid(row=5, column=0, padx=50, pady=10, sticky='e')


ctk.CTkLabel(b_frame, text='Base Folder').grid(row=0, column=0, padx=10, pady=5, columnspan=2)
txt_Base = ctk.CTkEntry(b_frame, width=400)
txt_Base.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='e')
btn_SelectBase = ctk.CTkButton(b_frame, text='Base Folder', command=setBase, width=100).grid(row=1, column=2, padx=22, pady=10, sticky='e')

ctk.CTkLabel(b_frame, text='Save Location').grid(row=2, column=0, padx=10, pady=5, columnspan=2)
txt_SaveLocation = ctk.CTkEntry(b_frame, width=400)
txt_SaveLocation.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky='w')
btn_SelectSave = ctk.CTkButton(b_frame, text='Save Location', command=setSaveLocation, width=100).grid(row=3, column=2, padx=22, pady=10, sticky='e')

lbl_Message = ctk.CTkLabel(b_frame, text='')
lbl_Message.grid(row=4, column=0, padx=50, pady=5, columnspan=2, sticky='w')
btn_Search = ctk.CTkButton(b_frame, text='SEARCH', command=search, width=100, height=50, fg_color='green').grid(row=4, column=2, padx=22, pady=20, sticky='se')

window.mainloop()