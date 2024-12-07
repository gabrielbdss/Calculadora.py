# importando tkinter
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#191a19"  # preta
cor2 = "#feffff"  # branca
cor3 = "#185b61"  # azul
cor4 = "#cccecf"  # cinza
cor5 = "#e88a3c"  # laranja
cor6 = "#ed4040"  # vermelho

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# Dsv. Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variável para todos os valores
todos_valores = ''

# Dsv. Label
valor_texto = StringVar()

# Funções
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    # Passando valor no display
    valor_texto.set(todos_valores)

# Função para calcular
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
    except:
        valor_texto.set("Erro")

# Função para limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")  # Corrigido: valor_texto.set("") ao invés de valor_texto.set=(())

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Dsv. Botões
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command=lambda:entrar_valores('%'), text="%", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, command=lambda:entrar_valores('/'), text="/", width=6, height=2, bg=cor5, fg=cor2, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda:entrar_valores('7'), text="7", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, command=lambda:entrar_valores('8'), text="8", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, command=lambda:entrar_valores('9'), text="9", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, command=lambda:entrar_valores('*'), text="*", width=6, height=2, bg=cor5, fg=cor2, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command=lambda:entrar_valores('4'), text="4", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, command=lambda:entrar_valores('5'), text="5", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_9.place(x=59, y=104)

b_10 = Button(frame_corpo, command=lambda:entrar_valores('6'), text="6", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=6, height=2, bg=cor5, fg=cor2, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command=lambda:entrar_valores('1'), text="1", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, command=lambda:entrar_valores('2'), text="2", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, command=lambda:entrar_valores('3'), text="3", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, command=lambda:entrar_valores('+'), text="+", width=6, height=2, bg=cor5, fg=cor2, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command=lambda:entrar_valores('0'), text="0", width=11, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo, command=lambda:entrar_valores('.'), text=".", width=6, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo, command=calcular, text="=", width=6, height=2, bg=cor5, fg=cor2, relief=RAISED, overrelief=RIDGE, font=('ivy 13 bold'))
b_18.place(x=177, y=208)

janela.mainloop()
