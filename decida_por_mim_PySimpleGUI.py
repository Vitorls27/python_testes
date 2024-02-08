import random
import PySimpleGUI as sg

class Decida_por_mim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você tá certo!',
            'Acredito que tanto faz',
            'Pode escolher, vai na sua opinião',
            'Acho melhor não',
            'Por favor, não faça isso',
            'Você deve fazer o que for melhor aos outros, sei que você vai dar um jeito'
        ]
    
    def Iniciar(self):
        """while True:
            input('Olá, o que gostaria de perguntar?\n')
            print(random.choice(self.respostas))"""
        layout = [
            [sg.Text('Olá, o que gostaria de perguntar?')],
            [sg.Input(key='inp'), sg.Button('Enviar')],
            [sg.Output(size=(40,10))]
        ]
        
        janela = sg.Window('Decida por Mim!', layout=layout)
        while True:
            eventos, valores = janela.Read()
            saida = valores['inp']
            if eventos == 'Enviar':
                print(random.choice(self.respostas))
                if saida == 'sair':
                    janela.Close()

        
decidir = Decida_por_mim()
decidir.Iniciar()