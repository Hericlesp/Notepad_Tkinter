import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk 

class SetNote:

    #inicializando a nossa janela
    __root =Tk()

    #configurações iniciais de nosso bloco de notas

    __thisWidth = 300
    __thisHeight = 300  
    __thisTextArea = Text(__root, padx=10,pady=10, wrap="word")
    #warp = "word" função de quebra de palavras para texto(text='word')

    __thisMenuBar = Menu(__root)


    def run(self):
        self.__root.mainloop()

note = SetNote()
note.run()