
class Jogo:
    def __init__(self):
        self.vida = True
        self.introduçao = 'Você acorda em uma caverna sem se lembrar de nada, com uma mochila e uma espada ao seu lado e muita dor de cabeça. Também há outra pessoa desacordada logo a frente.\nO que você faz?\n'
        self.pergunta1 = '\nTentar se lembrar'
        self.pergunta2 = '\nDescobrir entrada da caverna'
        self.pergunta3 = ''
        self.pergunta4 = '\nVerificar pessoa'
        self.pergunta5 = ''
        self.pergunta6 = '\nAbrir mochila'
        self.pergunta7 = '\nMatar-se'
        self.verificado = False
        self.resp = ''

    def Perguntar(self):
        print(self.introduçao, self.pergunta1, self.pergunta2, self.pergunta3, self.pergunta4, self.pergunta5, self.pergunta6, self.pergunta7)
        
    def Morrer(self):
        while True:
            print('\nVocê tem certeza? ')
            inp = input(self.resp)
            if str.lower(inp) == 'sim' or str.lower(inp) == 's':
                self.vida = False
                break
            elif str.lower(inp) == 'não' or str.lower(inp) == 'n' or str.lower(inp) == 'nao':
                break
            else:
                print('Diga sim ou não\n')
    
    def Iniciar(self):
        while self.vida is True:
            self.Perguntar()
            inp = input(self.resp)
            palavras = inp.split()
            for palavra in palavras:
                try:
                    if self.pergunta1 == '\nTentar se lembrar' and str.lower(palavra)  == 'lembrar':
                        self.introduçao = '\n\nVocê se lembra que entrou nessa caverna junto com a pessoa desacordada, mas não se lembra o porquê'
                        self.pergunta1 = '\nTentar se lembrar denovo'
                        self.Perguntar()
                        continue
                    if self.pergunta2 == '\nDescobrir entrada da caverna' and str.lower(palavra)  == 'descobrir' or str.lower(palavra)  == 'entrada' or str.lower(palavra)  == 'caverna':
                        self.introduçao = '\n\nVocê verifica de onde está vindo o vento e descobre a direção para sair da caverna'
                        self.pergunta2 = '\nSair da caverna'
                        self.pergunta3 = '\nEntrar mais fundo na caverna'
                        self.Perguntar()
                        continue
                    if self.pergunta4 == '\nVerificar pessoa' and str.lower(palavra)  == 'verificar' or str.lower(palavra)  == 'pessoa':
                        self.introduçao = '\n\nEla veste uma capa como disfarçe, tem um punhal caido a sua frente. Você pega o punhal'
                        self.pergunta4 = '\nTentar acorda-lo'
                        self.pergunta5 = '\nMata-lo'
                        #gatilho para mudar teste entre matar e morrer
                        self.verificado = True
                        continue
                    if self.pergunta6 == '\nAbrir mochila' and str.lower(palavra) == 'abrir' or str.lower(palavra) == 'mochila':
                        self.introduçao = '\n\n'
                        self.pergunta6 = ''
                        
                        
                    if self.verificado == False and str.lower(palavra) == 'matar' or str.lower(palavra) == 'matar-se' or str.lower(palavra) == 'matar-me' or str.lower(palavra) == 'morrer' or str.lower(palavra) == 'suicídar' or str.lower(palavra) == 'suicidar':
                        self.Morrer()
                    elif self.verificado == True and str.lower(palavra) == 'matar-se' or str.lower(palavra) == 'matar-me' or str.lower(palavra) == 'morrer' or str.lower(palavra) == 'suicídio' or str.lower(palavra) == 'suicidio' or str.lower(palavra) == 'suicídar' or str.lower(palavra) == 'suicidar':
                        self.Morrer()
                    else:
                        print('Sem associações, tente usar alguma palavra das opções para escolher sua ação\n')
                except:
                    print('ERRO: tente novamente\n')
                
jogo = Jogo()
jogo.Iniciar()