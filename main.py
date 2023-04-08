from tkinter import *
from datetime import datetime

from fontTools.ttLib import TTFont
font = TTFont('digital-7.ttf')

cor1 = "#3d3d3d" #preta
cor2 = "#fafcff" #branca
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelho
cor5 = "#dedcdc" #cinza
cor6 = "3080f0"  #azul

fundo = cor1
cor = cor3

janela = Tk()
janela.title("")
janela.geometry('440x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=fundo)

tempo = datetime.now()

hora = tempo.strftime("%H:%M:%S")
dia_semana = tempo.strftime("%A")
dia = tempo.day
mes = tempo.strftime("%b")
ano = tempo.strftime("%Y")

l1 = Label(janela, font=('Digital-7 80'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2 = Label(janela, font=('Digital-7 20'), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "   " + str(dia) + "/" + str(mes) + "/" + (ano))

relogio()
janela.mainloop()