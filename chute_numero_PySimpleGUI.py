import random
import PySimpleGUI as sg

class Num_aleat:
    def __init__(self):
        self.menor = 0
        self.maior = 25
        self.msg = 'Um número de 0 a 25 foi gerado aleatóriamente. Tente acertar qual o número: '
        self.msg_menor = 'Tente um número menor'
        self.msg_maior = 'Tente um número maior'
        self.msg_certo = 'VOCÊ ACERTOU O NÚMERO!'
        self.loop = True
        
    def Gerar_num(self):
        #gerar o guardar número
        self.num = random.randint(self.menor, self.maior)
        
    def Reiniciar(self):
        print('\nGostaria de Reiniciar novamente? ')
        while (self.loop is True):
            self.eventos, self.valores = self.janela.Read()
            self.repetir = self.valores['input']
            if(self.repetir == 'sim' or self.repetir == 's'):
                self.loop = False
                self.Iniciar()
            elif(self.repetir == 'não' or self.repetir == 'n'):
                self.loop = False
            else:
                print('Por Favor, Digite "sim" ou "não"')
             
    def Iniciar(self):
        #layout
        self.layout = [
            [sg.Text(self.msg, size=(20,0))],
            [sg.Submit(), sg.Input(size=(18,0),key='input')]
        ]
        #cria janela
        self.janela = sg.Window('Adivinhe o Número!', layout=self.layout)
        
        self.loop = True
        self.Gerar_num()
        print(self.msg)
        #responder de acordo com o usuario
        while (self.loop is True):
            #receber valores layout
            self.eventos, self.valores = self.janela.Read()
            self.valor_do_chute = self.valores['input']
            #usar valores
            try:
                if int(self.valor_do_chute) == self.num:
                    print(self.msg_certo)
                    self.Reiniciar()
                elif int(self.valor_do_chute) > self.num and int(self.valor_do_chute) <= 25:
                    print(self.msg_menor)
                elif int(self.valor_do_chute) < self.num and int(self.valor_do_chute) >= 0:
                    print(self.msg_maior)
                else:
                    print('Por favor, digite um número de 0 a 25')
            except:
                print('ERRO: Por favor, digite apenas números')
        
gerar = Num_aleat()
gerar.Iniciar()
