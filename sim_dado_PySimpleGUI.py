import random
import PySimpleGUI as sg

class Sim_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'gerar valor do dado? '
        
        #layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
    
    def Iniciar(self):
        #criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        while True:
            #ler os valores da tela
            self.eventos, self.valores = self.janela.Read()
            #fazer algo com os valores
            try:
                if self.eventos == 'Sim' or self.eventos == 's':
                    self.Gerar_valor_dado()
                elif self.eventos == 'Não' or self.eventos == 'n':
                    print('ok')
                    break
                else:
                    print('Por favor digitar "sim" ou "não"')
            except:
                print('ERRO')
            
    def Gerar_valor_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
simulador = Sim_dado()
simulador.Iniciar()
