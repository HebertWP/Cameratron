from tkinter import *
import time
class Caixa2(Frame):
    def __init__(self,master,camera):
        self.camera=camera
        Frame.__init__(self,master)
        self.configure(# highlightbackground="black",
         #       highlightcolor="black",
         #       highlightthickness=2,
         #       bg="red",
         #       pady=1
                )
        self.titulo=Label(  self
                            ,text="Video"
                            ,font="Calibri 12"
                            )
        self.textoDestino=Label(self
                                ,text="Destino: "
                                )
        self.destino=Entry( self,
                            width=30)
        self.destino.insert(END,"/home/pi/Desktop/Videos/")
        self.textoNome=Label(   self
                                ,text="Nome: "
                                )
        self.nome=Entry(self,
                        width=20)
        self.nome.insert(END,"Amostra")
        self.imagemBotaoStart=PhotoImage(file="./Imagens/06.png")
        self.imagemBotaoStop=PhotoImage(file="./Imagens/07.png")
        self.botao=Button(  self,
                            image=self.imagemBotaoStart,
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
        self.camera.setPathOut(self.destino.get())
        print(self.destino.get())
        print(self.nome.get())
        self.camera.iniciarGravacao(self.nome.get()+ time.strftime("%Y-%m-%d-%H-%M-%S"))

    def stopGravacao(self):
         self.botao.configure(  command=self.iniciarGravacao,
                                image=self.imagemBotaoStart)
         self.titulo.configure(text="Video")
         self.camera.pararGravacao()
        
