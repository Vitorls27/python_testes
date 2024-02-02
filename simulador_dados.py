# simudador de dado
# simular um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI

class Sim_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'gerar valor do dado? '

    def Iniciar(self):
        resposta = str()
        while(resposta != 'não' or 'n'):
            resposta = input(self.mensagem)
            try:
                if resposta == 'sim' or resposta == 's':
                    self.Gerar_valor_dado()
                elif resposta == 'não' or resposta == 'n':
                    break
                else:
                    print('Por favor digitar "sim" ou "não"')
            except:
                print('ERRO')

    def Gerar_valor_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Sim_dado()
simulador.Iniciar()
