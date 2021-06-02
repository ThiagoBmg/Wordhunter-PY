# desenvolvido por Thiago Gomes
# Ciência da Computação

from tkinter import scrolledtext
from tkinter import *
import os

chat_pasta = os.path.dirname(os.path.abspath(__file__)) # guardando o caminho da pasta atual
chat_archive = os.path.join(chat_pasta, 'chat.txt') # guardando o caminho do arquivo chat

def getWords():
    txt.delete(0.1, END) # limpando a text box antes de printar o novo valor
    frequency.delete(0,END) # limpando a text box antes de printar o novo valor
    words = palavraEntrada.get() # pegando o valor digitado pelo usuário
    frequency_tmp = 0 # definindo variavel que ira contar a frequencia com que a palavra digitada aparece no chat 
    archive = open(chat_archive, "r") # abrindo o archive para realizar as interações 
    for rows in archive: # passando pelas linhas do archive
        rows.strip().split('\n') # utilizando o delimitador para separar as linhas
        if words in rows: # passando pelas palavras do archive
            frequency_tmp += 1 # interando quantas vezes a palavra digitada apareceu
            txt.insert(INSERT, rows+'\n') # inserindo os textos na grid principal 
    archive.close() # fechando o archive após realizar os processos
    frequency.insert(0, frequency_tmp) # inserindo a nova frequencia


app = Tk() # criando app
app.geometry("900x900") #atribuindo o tamanho da app
app.title("filtro de palavra") #titulo da app

Label(app, text="palavra suspeita: ", font=("Arial", 14)).place(relx=0.05, rely=0.08) # criando texto 
Label(app, text="frequência: ", font=("Arial", 14)).place(relx=0.05, rely=0.15) # criando texto
Label(app, text="ocorrencias: ", font=("Arial", 14)).place(relx=0.05, rely=0.3) # criando texto
Button(app, text="pesquisar", command=getWords).place(relx=0.5, rely=0.08) # botão

palavraEntrada = Entry(app, width=15, font=("Arial", 14)) # criando input
palavraEntrada.place(relx=0.25, rely=0.08) # definindo local do input
frequency = Entry(app, width=15, font=("Arial", 14)) # criando input
frequency.place(relx=0.25, rely=0.15) # definindo local do input
txt = scrolledtext.ScrolledText(app, width=100, height=23)  # criando ScrolledText
txt.place(relx=0.05, rely=0.35) # definindo local do ScrolledText
app.mainloop()