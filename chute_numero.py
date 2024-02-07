import random
from tkinter import *

class Num_aleat:
    def __init__(self):
        self.menor = 0
        self.maior = 25
        self.msg = 'Um número de 0 a 25 foi gerado aleatóriamente. Tente acertar qual o número: '
        self.msg_menor = 'Tente um número menor'
        self.msg_maior = 'Tente um número maior'
        self.msg_certo = 'VOCÊ ACERTOU O NÚMERO!'
        #self.loop = True
        
    def Gerar_num(self):
        #gerar o guardar número
        self.num = random.randint(self.menor, self.maior)
        
    def Reiniciar(self):
        """self.msg['text'] = '\nGostaria de Reiniciar novamente? '
        #while (self.loop is True):
            #self.Input()  
        if(self.resp == 'sim' or self.resp == 's'):
            #self.loop = False
            self.msg['text'] = 'Um número de 0 a 25 foi gerado aleatóriamente. Tente acertar qual o número: '
            self.resultado['text'] = ''
        elif(self.resp == 'não' or self.resp == 'n'):
            #self.loop = False
            self.layout.destroy()
        else:
            self.resultado['text'] = 'Por Favor, Digite "sim" ou "não"'"""
        self.layout2 = Tk()
        self.layout2.title('Reiniciar?')
        
        pergunta = Label(self.layout2, text='Deseja adivinhar o número denovo?')
        pergunta.grid(row=0, column=0)
        botao_sim = Button(self.layout2, text='sim', command=self.Com_sim)
        botao_sim.grid(row=1, column=0)
        botao_nao = Button(self.layout2, text='não', command=self.Com_nao)
        botao_nao.grid(row=1, column=1)
                
        self.layout2.mainloop()
        
    def Com_sim(self):
        self.layout.destroy()
        self.layout2.destroy()
        self.Iniciar()
        
    def Com_nao(self):
        self.layout.destroy()
        self.layout2.destroy()
        
    def Inp(self):
        try:
            if int(self.resp.get('1.0', END)) == self.num:
                self.resultado['text'] = self.msg_certo
                self.Reiniciar()
            elif int(self.resp.get('1.0', END)) > self.num and int(self.resp.get('1.0', END)) <= 25:
                self.resultado['text'] = self.msg_menor
            elif int(self.resp.get('1.0', END)) < self.num and int(self.resp.get('1.0', END)) >= 0:
                self.resultado['text'] = self.msg_maior
            else:
                self.resultado = 'Por favor, digite um número de 0 a 25'
        except:
            self.resultado = 'ERRO: Por favor, digite apenas números'
             
    def Iniciar(self):
        #self.loop = True
        self.Gerar_num()
        print(self.num)
        #print(self.msg)
        #responder de acordo com o usuario
        """while (self.loop is True):
            try:
                if int(self.resp) == self.num:
                    self.resultado['text'] = self.msg_certo
                    self.Reiniciar()
                elif int(self.resp) > self.num and int(self.resp) <= 25:
                    self.resultado['text'] = self.msg_menor
                elif int(self.resp) < self.num and int(self.resp) >= 0:
                    self.resultado['text'] = self.msg_maior
                else:
                    self.resultado = 'Por favor, digite um número de 0 a 25'
            except:
                self.resultado = 'ERRO: Por favor, digite apenas números'"""
        
        #layout
        self.layout = Tk()
        self.layout.title('Acerte o Número')
        
        self.txt_inicio = Label(self.layout, text=self.msg)
        self.txt_inicio.grid(row=0, column=0)
        self.botao = Button(self.layout, text='Submit', command=self.Inp)
        self.botao.grid(row=1,column=0)
        self.resp = Text(self.layout, height=5, width=20)
        self.resp.grid(row=2,column=0)
        self.resultado = Label(self.layout, text='')
        self.resultado.grid(row=3,column=0)
        
        self.layout.mainloop()
    
gerar = Num_aleat()
gerar.Iniciar()
