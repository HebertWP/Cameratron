from tkinter import *
import time
class Caixa1(Frame):
    def __init__(self,master,camera):
        Frame.__init__(self)
        self.camera=camera
        self.titulo=Label(  self,
                            text="Foto",
                            )
        self.textoDestino=Label(self,
                                text="Destino: ",
                                )
        self.destino=Entry( self,
                            width=30)
        self.destino.insert(END,"/home/pi/Desktop/Fotos/")
        self.textoNome=Label(   self,
                                text="Nome: ",
                                )
        self.nome=Entry(self,
                        width=20)
        self.nome.insert(END,"Amostra")
        self.imagembotao=PhotoImage(file="./Imagens/02.png")
        self.botao=Button(  self,
                            image=self.imagembotao,
                            pady=1,
                            padx=1,
                            command=self.tirarFoto)
        self.titulo.pack()
        self.textoDestino.pack(side=LEFT)
        self.destino.pack(side=LEFT)
        self.textoNome.pack(side=LEFT)
        self.nome.pack(side=LEFT)
        self.botao.pack(side=LEFT)

    def tirarFoto(self):
        self.camera.setPathOut(self.destino.get())
        self.camera.tirarFoto(self.nome.get() +  time.strftime("%Y-%m-%d-%H-%M-%S"))
