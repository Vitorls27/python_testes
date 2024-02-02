# simudador de dado
# simular um dado, gerando um valor de 1 até 6
import random
from tkinter import *
class Sim_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'gerar valor do dado? '
        
        resp = self.Gerar_valor_dado()
        resp['text'] = self.Gerar_valor_dado()
        #layout
        layout = Tk()
        layout.title('título')
        layout.geometry('400x200')
        
        texto = Label(layout, text='texto')
        texto.grid(column=0,row=0, padx=10, pady=5)
        botao = Button(layout, text='Botão/SIM', command=self)
        botao.grid(column=0,row=1, padx=8, pady=5)
        botao2 = Button(layout, text='Botão/NÃO', command='')
        botao2.grid(column=1,row=1, padx=8, pady=5)
        resp = Label(layout, text='')
        resp.grid(column=0,row=2, padx=10, pady=5)

        layout.mainloop()
        
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.Gerar_valor_dado()
            elif resposta == 'não' or resposta == 'n':
                print('')
            else:
                resp = 'Por favor digitar "sim" ou "não"'
        except:
            resp = 'ERRO'
    
    def Gerar_valor_dado(self):
        return random.randint(self.valor_minimo, self.valor_maximo)

simulador = Sim_dado()
simulador.Iniciar()
