import random
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
        self.newpergunta3 = '\nBater na porta'
        self.newpergunta4 = '\nVerificar altar'
        self.newpergunta5 = ''
        self.verificado = False
        self.lembra1 = False
        self.lembra2 = False
        self.lembra3 = False
        self.lembra4 = False
        self.resp = ''

    def Perguntar(self):
        print(self.introduçao, self.pergunta1, self.pergunta2, self.pergunta3,
              self.pergunta4, self.pergunta5, self.pergunta6, self.pergunta7)

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

    def Terminar(self):
        print(self.introduçao)
        input('\nPressione ENTER para terminar sua história')
        self.vida = False

    def FimVdd(self):
        print(self.introduçao)
        input('\nParabéns, você encontrou o final verdadeiro. Muito obrigado por entrar nessa aventura\nPressione ENTER para terminar sua grande jornada')

    def Iniciar(self):
        while self.vida is True:
            self.Perguntar()
            inp = input(self.resp)
            palavras = inp.split()
            for palavra in palavras:
                try:
                    # serie da pergunta 1
                    if self.pergunta1 == '\nTentar se lembrar' and str.lower(palavra) == 'lembrar':
                        if self.lembra1 == False:
                            self.introduçao = '\n\nVocê se lembra que entrou nessa caverna junto com a pessoa desacordada, mas não se lembra o porquê'
                            self.lembra1 = True
                        elif self.pergunta6 == '' and self.lembra2 == False:
                            self.introduçao = '\n\nVocê não foi trazido pra cá ou algo assim, você veia aqui em busca de algo'
                            self.lembra2 = True
                        elif self.pergunta4 != '\nVerificar pessoa' and self.lembra3 == False:
                            self.introduçao = '\n\nFoi feito um trato entre você e a pessoa, mas não se lembra o que foi'
                            self.lembra3 = True
                        elif self.pergunta4 == '\nUsar chave' or self.newpergunta4 == '\nUsar chave' and self.lembra4 == False:
                            self.introduçao = '\n\nVocê não se lembra de mais nada por enquanto'
                            self.lembra4 = True
                        else:
                            self.introduçao = '\n\nVocê não se lembra de mais nada por enquanto'
                    # serie da pergunta 2
                    elif self.pergunta2 == '\nDescobrir entrada da caverna' and str.lower(palavra) == 'descobrir' or str.lower(palavra) == 'entrada' or str.lower(palavra) == 'caverna':
                        self.introduçao = '\n\nVocê verifica de onde está vindo o vento e descobre a direção para sair da caverna'
                        self.pergunta2 = '\nSair da caverna'                            # variação 2.1
                        self.pergunta3 = '\nEntrar mais fundo na caverna'               # variação 3.1
                    elif self.pergunta2 == '\nSair da caverna' and str.lower(palavra) == 'sair' or str.lower(palavra) == 'saida' or str.lower(palavra) == 'saída' or str.lower(palavra) == 'caverna' or str.lower(palavra) == 'embora':
                        if self.pergunta1 == '\nTentar se lembrar':
                            self.introduçao = '\n\nVocê sai da caverna bem confuso, apenas querendo voltar para casa, seja lá onde for. Encontra uma pequena vila, mas nada lhe é familiar. Tenta começar uma nova vida, sem saber quem era.'
                            self.Terminar()     # FINAL 1
                        elif self.pergunta1 == '\nTentar se lembrar denovo':
                            self.introduçao = '\n\nVocê sai da caverna confuso, se perguntando por que veio aqui. Encontra uma pequena vila e tenta pedir por ajuda. Ninguém é familiar, então decide ir embora para ficar longe do que for que tenha acontecido.'
                            self.Terminar()     # FINAL 2
                    elif self.pergunta2 == '\nVoltar' and str.lower(palavra) == 'voltar' or str.lower(palavra) == 'sair' or str.lower(palavra) == 'volta':
                        self.pergunta2 = '\nSair da caverna'                            # variação 2.1
                        self.newpergunta3 = self.pergunta3
                        self.pergunta3 = '\nEntrar mais fundo na caverna'               # variação 3.1
                        self.pergunta4 = self.oldpergunta4
                        self.pergunta5 = self.oldpergunta5
                    # serie da pergunta 3
                    elif self.pergunta3 == '\nEntrar mais fundo na caverna' and str.lower(palavra) == 'entrar' or str.lower(palavra) == 'fundo' or str.lower(palavra) == 'entra':
                        if self.pergunta6 == '\nAbrir mochila':
                            self.introduçao = '\n\nVocê chega ao final da caverna e encontra apenas uma porta grande'
                            self.pergunta2 = '\nVoltar'                                 # variação 2.2
                            self.pergunta3 = self.newpergunta3                          # variação 3.2
                            self.oldpergunta4 = self.pergunta4
                            self.pergunta4 = ''
                            self.oldpergunta5 = self.pergunta5
                            self.pergunta5 = ''
                        else:
                            self.introduçao = '\n\nVocê chega ao final da caverna e encontra uma porta grande e, ao lado em um canto mais escuro, um altar'
                            self.pergunta2 = '\nVoltar'                                 # variação 2.2
                            self.pergunta3 = '\nBater na porta'                         # variação 3.2
                            self.oldpergunta4 = self.pergunta4
                            self.pergunta4 = self.newpergunta4                          # variação 4.3
                            self.oldpergunta5 = self.pergunta5
                            self.pergunta5 = self.newpergunta5                          # variação 5.2
                    elif self.pergunta3 == '\nBater na porta' and str.lower(palavra) == 'bater' or str.lower(palavra) == 'bate' or str.lower(palavra) == 'porta' or str.lower(palavra) == 'toc':
                        self.introduçao = '\n\nVocê bate na porta. Você nota uma fechadura para um tipo estranho de chave'
                        self.pergunta3 = ''
                    elif self.pergunta3 == '\nUsar chave' and str.lower(palavra) == 'chave' or str.lower(palavra) == 'usar' or str.lower(palavra) == 'porta':
                        self.introduçao = '\n\nA porta se abre'
                        self.pergunta3 = '\nEntrar'
                    elif self.pergunta3 == '\nEntrar' and str.lower(palavra) == 'entrar' or str.lower(palavra) == 'entra' or str.lower(palavra) == 'ir' or str.lower(palavra) == 'vou' or str.lower(palavra) == 'vai':
                        self.introduçao = '\n\nVocê finalmente saberá porque veio aqui. Encontra guardado incontáveis moedas de ouro, o desejo e sonho de qualquer um.\nMas sua mente ficou ainda mais aflita ainda. Mesmo que tenhas vindo até aqui, sente que não era isso que estava procurando.'
                        self.FimVdd()
                    # serie da pergunta 4
                    elif self.pergunta4 == '\nVerificar pessoa' and str.lower(palavra) == 'verificar' or str.lower(palavra) == 'pessoa':
                        self.introduçao = '\n\nEla veste uma capa como disfarçe, tem um punhal caido a sua frente. Você pega o punhal'
                        self.pergunta4 = '\nTentar acorda-lo'                           # variação 4.1
                        self.pergunta5 = '\nMata-lo'                                    # variação 5.1
                        # gatilho para mudar teste entre matar e morrer e punhal
                        self.verificado = True
                    elif self.pergunta4 == '\nTentar acorda-lo' and str.lower(palavra) == 'acorda-lo' or str.lower(palavra) == 'acordar' or str.lower(palavra) == 'despertar' or str.lower(palavra) == 'desperta-lo':
                        if self.pergunta5 == '':
                            self.introduçao = '\n\nEle está morto'
                        else:
                            self.introduçao = '\n\nVocê tenta acorda-lo mas nada funciona, porém ainda está respirando. Há um ferimento na cabeça dele, provavelmento o que o desacordou'
                        self.pergunta4 = ''                                             # variação 4.2
                    elif self.pergunta4 == '\nVerificar altar' and str.lower(palavra) == 'verificar' or str.lower(palavra) == 'altar':
                        self.introduçao = '\n\nHá escrituras gravadas no altar. Se um corpo sem vida for deixado nesse altar, você receberá o que veio buscar'
                        self.pergunta4 = '\nSacrificar-se'                              # variação 4.4
                        self.newpergunta4 = self.pergunta4
                        if self.oldpergunta4 != '\nVerificar pessoa' and self.oldpergunta5 != '\nMata-lo':
                            self.pergunta5 = '\nTrazer a pessoa morta'                  # variação 5.3
                            self.newpergunta5 = self.pergunta5
                        else:
                            self.pergunta5 = '\nTrazer a pessoa desacordada'            # variação 5.4
                            self.newpergunta5 = self.pergunta5
                    elif self.pergunta4 == '\nSacrificar-se' and str.lower(palavra) == 'me' or str.lower(palavra) == 'sacrificar-se':
                        self.introduçao = '\n\nDeitando-se sobre o altar, sacas a adaga e coloca-a na garganta.'
                        self.Morrer()  # FINAL 3
                    # serie da pergunta 5
                    elif self.pergunta5 == '\nMata-lo' and str.lower(palavra) == 'mata-lo' or str.lower(palavra) == 'matar' or str.lower(palavra) == 'assasinar':
                        self.introduçao = '\n\nVocê pega a espada e mata a pessoa desacordado'
                        self.pergunta5 = ''                                             # variação 5.2
                    elif self.pergunta5 == '\nTrazer a pessoa morta' and str.lower(palavra) == 'trazer' or str.lower(palavra) == 'pessoa':
                        self.introduçao = '\n\nVolta e traz o corpo sem vida da pessoa'
                        self.pergunta5 = '\nColocar o corpo no altar'
                        self.newpergunta5 = self.pergunta5
                    elif self.pergunta5 == '\nTrazer a pessoa desacordada' and str.lower(palavra) == 'trazer' or str.lower(palavra) == 'pessoa':
                        self.introduçao = '\n\nVolta e traz o corpo daquela pessoa desacordada'
                        self.pergunta5 = '\nColocar o corpo no altar'
                        self.newpergunta5 = self.pergunta5
                    elif self.pergunta5 == '\nColocar o corpo no altar' and str.lower(palavra) == 'colocar' or str.lower(palavra) == 'corpo' or str.lower(palavra) == 'altar':
                        if self.oldpergunta4 != '\nVerificar pessoa' and self.oldpergunta5 != '\nMata-lo':
                            if self.pergunta3 == '\nBater na porta':
                                self.introduçao = '\n\nAbre-se uma abertura na parede da caverna com o que parece ser a chave da porta. Você pega e logo a abertura se fecha'
                                self.pergunta5 = ''
                                self.newpergunta5 = self.pergunta5
                            else:
                                self.introduçao = '\n\nAbre-se uma abertura na parede da caverna com um objeto estranho. Parece se encaixar em algo. Você pega e logo a abertura se fecha'
                                self.pergunta5 = ''
                                self.newpergunta5 = self.pergunta5
                                self.pergunta3 = '\nUsar chave'                     # variação 3.3
                                self.pergunta4 = ''
                                self.newpergunta4 = self.pergunta4
                    elif self.pergunta5 == '\nTrazer a pessoa desacordada' and str.lower(palavra) == 'trazer' or str.lower(palavra) == 'pessoa' or str.lower(palavra) == 'desacordada' or str.lower(palavra) == 'desacordado':
                        self.introduçao = '\n\nVoltando ao local anterior, pega o pessoa desacordada e traz até o fundo da caverna. Ela não acordou ainda'
                        self.pergunta5 = '\nSacrifica-lo'
                    elif self.pergunta5 == '\nSacrifica-lo' and str.lower(palavra) == 'ele' or str.lower(palavra) == 'sacrifica-lo':
                        while True:
                            # daria pra fazer um combate de acordo com o que tivesse e mais complexo
                            self.introduçao = '\n\nVocê pega sua espada, mas quando está prestes a mata-lo, ele acorda e toma a sua arma, preparando-se para lutar'
                            ops = ['Atacar', 'Defender', 'Nada']
                            rnd = random.choice(ops)
                            hp = 3
                            vida = 5
                            print('\nAtacar\nDefender\nCorrer\nNada\n')  # opções
                            inp2 = input(self.resp)
                            if str.lower(inp2) == 'atacar' or str.lower(inp2) == 'ataque' or str.lower(inp2) == 'ataco':
                                if rnd == 'Atacar':
                                    if self.verificado == True:
                                        self.introduçao = '\n\nVocês dois atacam. Com o punhal você consegue machuca-lo'
                                        hp -= 2
                                    elif self.verificado == False:
                                        self.introduçao = '\n\nVocês dois atacam. Você não consegue fazer muita coisa desarmado. Ele te corta'
                                        vida -= 2
                                if rnd == 'Defender':
                                    if self.verificado == True:
                                        self.introduçao = '\n\nEle se defende. Você faz um corte superficial com o punhal'
                                        hp -= 1
                                    elif self.verificado == False:
                                        self.introduçao = '\n\nEle se defende. Você não consegue machuca-lo'
                                if rnd == 'Nada':
                                    if self.verificado == True:
                                        self.introduçao = '\n\nEle se desfoca e, com o punhal, você consegue corta-lo'
                                        hp -= 2
                                    elif self.verificado == False:
                                        self.introduçao = '\n\nEle se desfoca e você consegue soca-lo'
                                        hp -= 1
                            elif str.lower(inp2) == 'defender' or str.lower(inp2) == 'defesa' or str.lower(inp2) == 'defende' or str.lower(inp2) == 'defenda-se' or str.lower(inp2) == 'defenda':
                                if rnd == 'Atacar':
                                    if self.verificado == True:
                                        self.introduçao = '\n\nEle te ataca. Com o punhal você consegue se defender bem'
                                    elif self.verificado == False:
                                        self.introduçao = '\n\nEle te ataca. Mesmo defendendo, ele te machuca um pouco'
                                        hp -= 1
                                if rnd == 'Defender':
                                    self.introduçao = '\n\nVocês dois se preparam para defender'
                                if rnd == 'Nada':
                                    self.introduçao = '\n\nVocê se preparou para defender mas ele não fez nada'
                            elif str.lower(inp2) == 'correr' or str.lower(inp2) == 'corra' or str.lower(inp2) == 'corre':
                                if rnd == 'Atacar':
                                    self.introduçao = '\n\nVocê começa a correr, mas ele consegue te alcançar e te bloqueia'
                                if rnd == 'Defender' or rnd == 'Nada':
                                    self.introduçao = '\n\nVocê corre para fora da caverna, deixando ele para traz.\nCorrendo até não conseguir mais, ficando longe daquele lugar, você nunca saberá o que realmente aconteceu'
                                    self.Terminar()
                            elif str.lower(inp2) == 'nada':
                                if rnd == 'Atacar':
                                    self.introduçao = '\n\nEle te ataca, desferindo um corte grande'
                                    vida -= 2
                                if rnd == 'Defender':
                                    self.introduçao = '\n\nEle prepara uma defesa. Ninguém sofre dano'
                                if rnd == 'Nada':
                                    self.introduçao = '\n\nNinguém faz nada. Vendo os olhos dele, percebe raiva e um objetivo bem definido'
                            else:
                                print(
                                    '\nSem associações, tente usar alguma palavra das opções para escolher sua ação\n')
                            if hp <= 0:
                                print('Você o derrotou. Ele está morto')
                                self.pergunta5 = '\nColocar o corpo no altar'
                                self.newpergunta5 = self.pergunta5
                                break
                            elif vida <= 0:
                                print('Você se sente muito fraco. Você perdeu')
                                self.introduçao = '\n\nDurante seus últimos momentos, você só consegue ver o sorriso de quem te matou e se pergunta porque tudo isso aconteceu'
                                self.vida = False
                                break
                    # serie da pergunta 6
                    elif self.pergunta6 == '\nAbrir mochila' and str.lower(palavra) == 'abrir' or str.lower(palavra) == 'mochila':
                        self.introduçao = '\n\nVocê encontra uma lanterna e um mapa. O mapa mostra que há algo valioso dentro da caverna'
                        self.pergunta6 = ''                                             # variação 6.1

                    elif self.verificado == False and str.lower(palavra) == 'morte' or str.lower(palavra) == 'matar' or str.lower(palavra) == 'matar-se' or str.lower(palavra) == 'matar-me' or str.lower(palavra) == 'morrer' or str.lower(palavra) == 'suicídar' or str.lower(palavra) == 'suicidar':
                        self.Morrer()
                    elif self.verificado == True and str.lower(palavra) == 'matar-se' or str.lower(palavra) == 'matar-me' or str.lower(palavra) == 'morrer' or str.lower(palavra) == 'suicídio' or str.lower(palavra) == 'suicidio' or str.lower(palavra) == 'suicídar' or str.lower(palavra) == 'suicidar':
                        self.Morrer()
                    else:
                        print(
                            '\nSem associações, tente usar alguma palavra das opções para escolher sua ação\n')
                except:
                    print('\nERRO: tente novamente\n')

jogo = Jogo()
jogo.Iniciar()
