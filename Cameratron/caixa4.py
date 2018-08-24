from tkinter import *
class Caixa4(Frame):
    def __init__(self,master,camera):
        self.__camera=camera
        Frame.__init__(self,master)
        self.configure( relief=GROOVE
                        ,bd=3
                      )
    ##    self.__parte1=Frame(self)
     #   self.__parte2=Frame(self)
        self.__vilualizacao=Label(  self
                            ,text="Visualizacao"
                            ,font="Calibri 12"
                        )
        self.__imaIniVis=PhotoImage(file="./Imagens/10.png")
        self.__imaParVis=PhotoImage(file="./Imagens/11.png")
        self.__botVisualicao=Button(    self
                                        ,image=self.__imaIniVis
                                        ,command=self.__iniciarVisualizacao
                                   )
        self.__vilualizacao.pack()
        self.__botVisualicao.pack()
        self.__resolucao=Label(  self
                            ,text="Resolução"
                        )
        self.__resolucao.pack(fill=X)
        self.__resolucaoVar=StringVar()
        self.__resolucao=OptionMenu(   self
                                        ,self.__resolucaoVar
                                        ,'2592x1944'
                                        ,'1920x1080'
                                        ,'1296x972'
                                        , '1296x730'
                                        , '640x480'
                                        ,command=lambda x:self.__camera.setResolucao(self.__resolucaoVar.get())
                                        )
        self.__resolucaoVar.set("2592x1944")
        self.__resolucao.pack()
        self.__AW=StringVar()
        self.__balancoBranco=Label(  self
                            ,text="Balanco Branco"
                        )
        self.__balancoBranco.pack(fill=X)
        
        self.__AWMenu = OptionMenu(self
                                       ,self.__AW,
                                       'off', 'auto', 'green',
                                       'red', 'blue', 'sunlight', 'cloudy',
                                       'shade', 'tungsten', 'fluorescent',
                                       'incandescent',
                                       'flash', 'horizon'
                                       ,command=lambda x:self.__camera.setBalancoBranco(self.__AW.get())
                                       )
        self.__AW.set("auto")
        self.__AWMenu.pack(fill=X)
        self.__modesLabel=Label(self,text="Efeto de Imagem")
        self.__modesLabel.pack(fill=X)
        self.__modesVar=StringVar()
        self.__modes =OptionMenu(self
                                   ,self.__modesVar,
                                      "none", "negative", "solarize", "sketch",
                                      "denoise", "emboss", "oilpaint", "hatch",
                                      "gpen", "pastel", "watercolor", "film",
                                      "blur", "saturation", "colorswap",
                                      "washedout",
                                      "posterise", "colorpoint",
                                      "colorbalance", "cartoon",
                                      "deinterlace1", "deinterlace2"
                                      ,command=lambda x:self.__camera.setEfeitoImagem(self.__modesVar.get())
                                 )
        self.__modesVar.set("none")
        self.__modes.pack(fill="x")
        self.__efeitoCorLabel=Label(self,text="Efeto de Cor")
        self.__efeitoCorLabel.pack(fill=X)
        self.__efeitoCorVar=StringVar()
        self.__efeitoCor =OptionMenu(self
                                       ,self.__efeitoCorVar,
                                      "NONE",
                                      "RED", "GREEN", "BLUE", "BW"
                                      ,command=lambda x:self.__camera.setEfeitoCor(self.__efeitoCorVar.get())
                                          )
        self.__efeitoCor.pack(fill="x")
        self.__efeitoCorVar.set("none")
       
        
    def __iniciarVisualizacao(self):
        self.__botVisualicao.configure( command=self.__pararVisualizacao
                                        ,image=self.__imaParVis
                                      )
        self.__camera.visualizar()

    def __pararVisualizacao(self):
        self.__botVisualicao.configure(command=self.__iniciarVisualizacao
                                        ,image=self.__imaIniVis
                                      )
        self.__camera.visualizar(False)
'''
self.__imaHor=PhotoImage(file="./Imagens/09.png")
 #       self.__botHor=Button(   self.__parte1
                                ,image=self.__imaHor
                            )
        self.__imaAnt=PhotoImage(file="./Imagens/08.png")
        self.__botAnt=Button(   self.__parte1
                                ,image=self.__imaAnt
                            )
        self.__barRot=Scale(   self.__parte1
                                ,from_=-180
                                ,to=180
                                ,length=100
                                ,label="Rotacao"
                                ,orient=HORIZONTAL
                                )
        self.__resRot=Button(   self.__parte1
                                ,text="Reset"
                            )
        self.__barTam=Scale(    self.__parte2
                                ,from_=50
                                ,to=300
                                ,length=100
                                ,label="Tamanho"
                                ,orient=HORIZONTAL
                                )
        self.__resTam=Button(   self.__parte2
                                ,text="Reset"
                            )
        self.__vilualizacao.pack()
        self.__botVisualicao.pack()
        self.__botAnt.pack(side=LEFT)
        self.__botHor.pack(side=RIGHT)
        self.__barRot.pack()
        self.__resRot.pack(fill=X)
        self.__parte1.pack()
        self.__barTam.pack()
        self.__resTam.pack()
        self.__parte2.pack()
'''

