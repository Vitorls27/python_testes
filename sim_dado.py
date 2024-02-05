import random
from tkinter import *

class Sim_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'gerar valor do dado? '
        
    def Gerar_valor_dado(self):
        self.resp['text'] = random.randint(self.valor_minimo, self.valor_maximo)
    
    def Iniciar(self):
        """código para responder digitando:
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.Gerar_valor_dado()
            elif resposta == 'não' or resposta == 'n':
                print('')
            else:
                resp = 'Por favor digitar "sim" ou "não"'
        except:
            resp = 'ERRO'"""
        
        #layout
        layout = Tk()
        layout.title('título')
        layout.geometry('400x200')
        
        texto = Label(layout, text= self.mensagem)
        texto.grid(column=0,row=0, padx=10, pady=5)
        botao = Button(layout, text='Botão/SIM', command=self.Gerar_valor_dado)
        botao.grid(column=0,row=1, padx=8, pady=5)
        botao2 = Button(layout, text='Botão/NÃO', command=layout.destroy)
        botao2.grid(column=1,row=1, padx=8, pady=5)
        self.resp = Label(layout, text='')
        self.resp.grid(column=0,row=2, padx=10, pady=5)

        layout.mainloop()
        
simulador = Sim_dado()
simulador.Iniciar()
