from tkinter import *
class Caixa5(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)
        self.configure(# highlightbackground="black",
         #       highlightcolor="black",
         #       highlightthickness=2,
         #       bg="red",
         #       pady=1
                )
        self.titulo=Label(  self
                            ,text="Configuracao"
#                           , bg="red"
                            ,font="Calibri 12"
                            )
        self.textoDestino=Label(self,
                                text="Destino: "
#                                bg="red"
                                )
        self.destino=Entry( self,
                            width=30)
        self.destino.insert(END,"~/Descktop/Fotos/")
        self.textoNome=Label(   self
                                ,text="Nome: "
                                #,bg="red"
                                )
        self.nome=Entry(self,
                        width=30)
        self.nome.insert(END,"Amostra")
        self.imagemBotaoStart=PhotoImage(file="./Imagens/06.png")
        self.imagemBotaoStop=PhotoImage(file="./Imagens/07.png")
        self.botao=Button(  self,
                            image=self.imagemBotaoStart,
#                            highlightbackground="red",
 #                           highlightcolor="red",
  #                          highlightthickness=2,
            #                bg="red",
                            pady=1,
                            padx=1,
                            command=self.iniciarGravacao)
        self.titulo.pack()
        self.textoDestino.pack(side=LEFT)
        self.destino.pack(side=LEFT)
        self.textoNome.pack(side=LEFT)
        self.nome.pack(side=LEFT)
        self.botao.pack(side=LEFT)
    def iniciarGravacao(self):
        self.botao.configure(   command=self.stopGravacao,
                                image=self.imagemBotaoStop)
        self.titulo.configure(text="Gravando")
        print(self.destino.get())
        print(self.nome.get())

    def stopGravacao(self):
         self.botao.configure(  command=self.iniciarGravacao,
                                image=self.imagemBotaoStart)
         self.titulo.configure(text="Video")
 
