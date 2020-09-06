import tkinter as tk
import time
from typing import List
from random import *

class JanelaDoJogo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x600")
        self.resizable(0,0)
        self._frame = None
        self.switch_frame(StartPage)

        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=None, expand=False)

    def quit(self):
        self.destroy()




class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=900, height=600, background="#FFE4B5")
        tk.Frame.pack_propagate(self, 0)
        
        self.image = tk.PhotoImage(file="logoAleamoria.png")
        logoAleamoria = tk.Label(self, image=self.image)
        logoAleamoria.config(bg="systemTransparent")
        logoAleamoria.place(x=180, y=90)
        

        botaoComecar = tk.Button(self, text="Começar",
                  command=lambda: master.switch_frame(Comecar))
        botaoComecar.place(x=300, y=350)
        botaoComecar["width"] = 32
        botaoComecar["height"] = 4
        botaoComecar.config(background="systemTransparent")
        
        botaoManual = tk.Button(self, text="Manual", 
                  command=lambda: master.switch_frame(Manual))
        botaoManual.place(x=300, y=430)
        botaoManual["width"] = 10

        
        botaoCreditos = tk.Button(self, text="Créditos", 
                  command=lambda: master.switch_frame(Creditos))
        botaoCreditos.place(x=400, y=430)
        botaoCreditos["width"] = 10
        
        botaoSair = tk.Button(self, text="Sair", 
                  command=lambda: master.quit())
        botaoSair.place(x=500, y=430)
        botaoSair["width"] = 10




class Comecar(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=900, height=600, background="#FFE4B5")
        tk.Frame.pack_propagate(self, 0)

        self.master = master

        self.image2 = tk.PhotoImage(file="logoAleamoria.png")
        logoAleamoria = tk.Label(self, image=self.image2)
        logoAleamoria.config(bg="systemTransparent")
        logoAleamoria.place(x=180, y=90)

        jogadores = tk.Label(self, text="Digite o número total de jogadores da partida:")
        jogadores.place(x=300, y=350)
        jogadores.config(bg="systemTransparent")

        self.barra = tk.Entry(self)
        self.barra.place(x=300, y=380)
        self.barra["width"] = 20
        self.barra.bind("<Return>", self.apertarEnter)

        obs = tk.Label(self, text="(Mínimo de jogadores: 4   |   Máximo de jogadores: 20)", font=("Calibre", 11))
        obs.place(x=300, y=420)
        obs.config(bg="systemTransparent")

        botaoOk = tk.Button(self, text="Ok",
                  command=lambda: self.acaoDoBotaoOk())
        botaoOk.place(x=500, y=385)
        botaoOk["width"] = 8


        botaoVoltar = tk.Button(self, text="Voltar",
                  command=lambda: master.switch_frame(StartPage))
        botaoVoltar.place(x=5, y=5)
        botaoVoltar["width"] = 7
        botaoVoltar["height"] = 2


    def apertarEnter(self, event):
        self.acaoDoBotaoOk()

        
    def acaoDoBotaoOk(self):
        global numeroDeJogadores
        temp = self.barra.get()
        if temp.isnumeric():
            numeroDeJogadores = int(temp)
            if numeroDeJogadores >= 4 and numeroDeJogadores <= 20:
                self.sortearAleamorias()
                self.master.switch_frame(Fases)
            else:
                erro = tk.Label(self, text="O número de jogadores deve ser entre 4 e 20", font=("Calibre", 11))
                erro.place(x=300, y=450)
                erro.config(bg="systemTransparent")
        else:
            erro = tk.Label(self, text="Você deve digitar um númeral entre 4 e 20", font=("Calibre", 11))
            erro.place(x=300, y=470)
            erro.config(bg="systemTransparent")            

    def sortearAleamorias(self):
            global numeroDeJogadores
            global urna
            global aleamoriasSorteadas
            while len(urna) != numeroDeJogadores * 3:
                sorteio = choice(aleamoriasSorteadas)
                if sorteio not in urna:
                    urna.append(sorteio)




    
class Manual(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=900, height=600, background="#FFE4B5")
        tk.Frame.pack_propagate(self, 0)
        self.image4 = tk.PhotoImage(file="ManualAleamoria.png")
        imagemDeFundo = tk.Label(self, image=self.image4)
        imagemDeFundo.pack()
        botaoVoltar = tk.Button(self, text="Voltar",
                  command=lambda: master.switch_frame(StartPage))
        botaoVoltar.place(x=5, y=5)
        botaoVoltar["width"] = 7
        botaoVoltar["height"] = 2




class Creditos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=900, height=600, background="#FFE4B5")
        tk.Frame.pack_propagate(self, 0)
        self.image5 = tk.PhotoImage(file="CreditosAleamoria.png")
        imagemDeFundo = tk.Label(self, image=self.image5)
        imagemDeFundo.pack()

        botaoVoltar = tk.Button(self, text="Voltar",
                  command=lambda: master.switch_frame(StartPage))
        botaoVoltar.place(x=5, y=5)
        botaoVoltar["width"] = 7
        botaoVoltar["height"] = 2



    

class Jogo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=900, height=600, background="#FFE4B5")
        tk.Frame.pack_propagate(self, 0)


        self.image2 = tk.PhotoImage(file="logoAleamoriaPeq.png")
        logoAleamoria = tk.Label(self, image=self.image2)
        logoAleamoria.config(bg="systemTransparent")
        logoAleamoria.place(x=320, y=30)

        global faseAtual
        
        botaoVoltar = tk.Button(self, text="Voltar",
                  command=lambda: master.switch_frame(Comecar))
        botaoVoltar.place(x=5, y=5)
        botaoVoltar["width"] = 7
        botaoVoltar["height"] = 2

        equipe1 = tk.Label(self, text="EQUIPE 1: ", font=("Calibre", 16), bg="#FFA07A")
        equipe1.place(x=90, y=150)

        equipe2 = tk.Label(self, text="EQUIPE 2: ", font=("Calibre", 16), bg="#FFA07A")
        equipe2.place(x=670, y=150)


        self.botaoIniciarRodada = tk.Button(self, text="Iniciar Rodada",
                                 command=lambda: self.acaoBotaoIniciarRodada())
        self.botaoIniciarRodada.place(x=350, y=140)
        self.botaoIniciarRodada["width"] = 20
        self.botaoIniciarRodada["height"] = 3


        self.aviso = tk.Label(self, text="ATENÇÃO, líder da rodada: esconda esta tela dos demais jogadores antes de iniciar", font=("Calibre", 12), bg="#FFE4B5")
        self.aviso.place(x=200, y=200)
        
        
        if faseAtual < 4:
            self.botaoProximaFase = tk.Button(self, text="Ir para a próxima fase!",
                                     command=lambda: master.switch_frame(Fases))
            
        else:
            self.botaoProximaFase = tk.Button(self, text="Fim de Jogo! Veja o vencedor!",
                                     command=lambda: master.switch_frame(Parabens))
            
        self.botaoProximaFase.place(x=1000, y=1000)
        self.botaoProximaFase["width"] = 25
        self.botaoProximaFase["height"] = 3
        
        self.botaoAcertou = None

        self.cronometro = None

        self.labelAleamoria = None

        self.labelFinalDeFase = tk.Label(self, text="Fim de fase! Respire... Aguarde o cronômetro zerar", font=("Calibre", 20), bg="#FFE4B5")

        self.labelFimDoTempo = tk.Label(self, text="Tempo Esgotado! \n Passe a vez para a outra equipe.", font=("Calibre", 20), bg="#FFE4B5")

        
        self.sorteio = ""

        self.aleamoriaDaVez = tk.StringVar()

        self.pontosEquipe1 = tk.StringVar()

        self.pontosEquipe2 = tk.StringVar()

        global pontuacaoEquipe1 

        global pontuacaoEquipe2

        global vez

        global urna

        global descarte



    def acaoBotaoIniciarRodada(self):
        self.botaoIniciarRodada.place(x=1000, y=1000)
        self.cronometro = tk.Label(self, text="Seu tempo acaba em: ", font=("Calibre", 16), bg="#FFE4B5")
        self.cronometro.place(x=340, y=145)
        self.relogio()

        global urna
        global descarte

        if len(urna) == 0:
            urna = descarte
            descarte = []

        self.labelFinalDeFase.place(x=1000, y=1000)
        self.labelFimDoTempo.place(x=1000, y=1000)
        self.aviso.place(x=1000, y=1000)
        
        self.sorteio = urna[randint(0, len(urna))-1]

        self.aleamoriaDaVez.set(self.sorteio)
        self.labelAleamoria = tk.Label(self, textvariable=self.aleamoriaDaVez, font=("Calibre", 36), bg="#FFE4B5")
        self.labelAleamoria.place(x=350, y=290)

        self.pontosEquipe1.set(pontuacaoEquipe1)
        labelPontosEquipe1 = tk.Label(self, textvariable=self.pontosEquipe1, font=("Calibre", 16), bg="#FFA07A")
        labelPontosEquipe1.place(x=185, y=150)

        self.pontosEquipe2.set(pontuacaoEquipe2)
        labelPontosEquipe2 = tk.Label(self, textvariable=self.pontosEquipe2, font=("Calibre", 16), bg="#FFA07A")
        labelPontosEquipe2.place(x=765, y=150)

        self.botaoAcertou = tk.Button(self, text="Acertou!",
                                 command=lambda: self.acaoBotaoAcertou())
        self.botaoAcertou.place(x=350, y=450)
        self.botaoAcertou["width"] = 20
        self.botaoAcertou["height"] = 3
        
    
    def relogio(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=("Calibre", 20), bg="#FFE4B5")
        self.time.place(x=505, y=145)
        contador = self.now 
        self.time["textvariable"] = self.now
        self.tempo = 60
        self.update()

    
    
    def update(self):
        global vez
        global urna
        global descarte
        self.now.set(self.tempo)
        self.tempo -= 1
        if self.tempo == -1:
            vez = not vez
            self.botaoIniciarRodada.place(x=350, y=140)
            self.botaoAcertou.place(x=1000, y=1000)
            self.cronometro.place(x=1000, y=1000)
            self.time.place(x=1000, y=1000)
            self.labelAleamoria.place(x=1000, y=1000)

            if len(urna) != 0:
                self.labelFimDoTempo.place(x=300, y=250)
            else:
                self.labelFimDoTempo.place(x=1000, y=1000)
                self.botaoIniciarRodada.place(x=1000, y=1000)
                self.botaoProximaFase.place(x=350, y=450)
                

        else:
            self.after(1000, self.update)

    


    def acaoBotaoAcertou(self):
        global pontuacaoEquipe1
        global pontuacaoEquipe2
        global vez
        global urna
        global descarte
        if vez == True:
            pontuacaoEquipe1 += 1
            self.pontosEquipe1.set(pontuacaoEquipe1)
        else:
            pontuacaoEquipe2 += 1
            self.pontosEquipe2.set(pontuacaoEquipe2)

        urna.remove(self.sorteio)
        descarte.append(self.sorteio)
        if len(urna) != 0:
            self.sorteio = urna[randint(0, len(urna))-1]
            self.aleamoriaDaVez.set(self.sorteio)

        else:
            self.botaoAcertou.place(x=1000, y=1000)
            self.labelAleamoria.place(x=1000, y=1000)
            self.botaoIniciarRodada.place(x=1000, y=1000)
            self.labelFinalDeFase.place(x=220, y=250)
            global faseAtual
            faseAtual += 1
            



class Fases(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=900, height=600, background="#FFE4B5")
        tk.Frame.pack_propagate(self, 0)


        self.image2 = tk.PhotoImage(file="logoAleamoriaPeq.png")
        logoAleamoria = tk.Label(self, image=self.image2)
        logoAleamoria.config(bg="systemTransparent")
        logoAleamoria.place(x=320, y=30)

        global faseAtual
        global vez
        
        self.botaoJogar = tk.Button(self, text="Jogar!",
                                     command=lambda: master.switch_frame(Jogo))
        
            
        self.botaoJogar.place(x=350, y=450)
        self.botaoJogar["width"] = 20
        self.botaoJogar["height"] = 3


        self.fases = tk.StringVar()

        self.asFases = ["FASE 1: nesta fase você pode dar explicações \n verbais à vontade sobre sua Aleamória \n (vide Manual)",
                        "FASE 2: nesta fase você só pode fazer mímica \n como dica da sua Aleamória \n (vide Manual)",
                        "FASE 3: nesta fase você só pode falar uma única \n palavra como dica da sua Aleamória \n (vide Manual)",
                        "FASE 4: nesta fase você só pode emitir sons \n inteligíveis como dica da sua Aleamória \n (vide Manual)"]
        
        
        
        self.labelDaFase = tk.Label(self, textvariable=self.fases, font=("Calibre", 30), bg="#FFE4B5")
        self.labelDaFase.place(x=105, y=240)
        self.fases.set(self.asFases[faseAtual - 1])

        if vez == True:
            labelVez = tk.Label(self, text="ATENÇÃO: Quem começa esta fase é a Equipe 1", font=("Calibre", 14), bg="#FFE4B5")
            labelVez.place(x=105, y=380)
        else:
            labelVez = tk.Label(self, text="ANTENÇÃO: Quem começa esta fase é a Equipe 2", font=("Calibre", 14), bg="#FFE4B5")
            labelVez.place(x=105, y=380)
        



class Parabens(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=900, height=600, background="#FFE4B5")
        tk.Frame.pack_propagate(self, 0)

        global numeroDeJogadores
        global faseAtual
        global pontuacaoEquipe1
        global pontuacaoEquipe2
        global vez
        global urna
        global descarte

        self.image2 = tk.PhotoImage(file="logoAleamoriaPeq.png")
        logoAleamoria = tk.Label(self, image=self.image2)
        logoAleamoria.config(bg="systemTransparent")
        logoAleamoria.place(x=320, y=30)


        if pontuacaoEquipe1 > pontuacaoEquipe2:
            vencedor1 = tk.Label(self, text="A vencedora foi a Equipe 1! PARABÉNS!", font=("Calibre", 30), bg="#FFE4B5")
            vencedor1.place(x=200, y=250)
            
        if pontuacaoEquipe1 < pontuacaoEquipe2:
            vencedor2 = tk.Label(self, text="A vencedora foi a Equipe 2! PARABÉNS!", font=("Calibre", 30), bg="#FFE4B5")
            vencedor2.place(x=200, y=250)

        if pontuacaoEquipe1 == pontuacaoEquipe2:
            empate = tk.Label(self, text="INACREDITÁVEL! Deu EMPATE!", font=("Calibre", 30), bg="#FFE4B5")
            empate.place(x=200, y=250)

        self.botaoNovaPartida = tk.Button(self, text="Jogar de Novo!",
                                 command=lambda: master.switch_frame(Comecar))
        self.botaoNovaPartida.place(x=350, y=450)
        self.botaoNovaPartida["width"] = 20
        self.botaoNovaPartida["height"] = 3


        
        numeroDeJogadores = 0
        
        faseAtual = 1
        
        pontuacaoEquipe1 = 0
        
        pontuacaoEquipe2 = 0
        
        vez = True
        
        urna = []
        
        descarte = []
        


numeroDeJogadores = 0
faseAtual = 1
pontuacaoEquipe1 = 0
pontuacaoEquipe2 = 0
vez = True
urna = []
descarte = []

bancoDeAleamorias = open("BancoDeAleamorias.txt", "r")
aleamoriasSorteadas = []
for linha in bancoDeAleamorias:
    limpa = linha[0:len(linha) -1]
    aleamoriasSorteadas.append(limpa)
bancoDeAleamorias.close()

        


if __name__ == "__main__":
    app = JanelaDoJogo()
    app.mainloop()
