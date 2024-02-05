import random

class Num_aleat:
    def __init__(self):
        self.menor = 0
        self.maior = 25
        self.msg_menor = 'Tente um número menor'
        self.msg_maior = 'Tente um número maior'
        self.msg_certo = 'VOCÊ ACERTOU O NÚMERO!'
        self.loop = True
        self.terminar = True
        
    def Gerar_num(self):
        #gerar o guardar número
        self.num = random.randint(self.menor, self.maior)
        
    def Reiniciar(self):
        print('\nGostaria de Reiniciar novamente? ')
        while (self.loop is True):
            self.resp = input()
            if(self.resp == 'sim' or self.resp == 's'):
                self.loop = False
            elif(self.resp == 'não' or self.resp == 'n'):
                self.loop = False
                self.terminar = False
            else:
                print('Por Favor, Digite "sim" ou "não"')
             
    def Iniciar(self):
        while(self.terminar is True):
            self.loop = True
            self.Gerar_num()
            print('Um número de 0 a 25 foi gerado aleatóriamente. Tente acertar qual o número: ')
            #responder de acordo com o usuario
            while (self.loop is True):
                self.resp = input()
                try:
                    if int(self.resp) == self.num:
                        print(self.msg_certo)
                        self.Reiniciar()
                    elif int(self.resp) > self.num and int(self.resp) <= 25:
                        print(self.msg_menor)
                    elif int(self.resp) < self.num and int(self.resp) >= 0:
                        print(self.msg_maior)
                    else:
                        print('Por favor, digite um número de 0 a 25')
                except:
                    print('ERRO: tente novamente')
        
gerar = Num_aleat()
gerar.Iniciar()
