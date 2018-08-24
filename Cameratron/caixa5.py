from tkinter import *

class Caixa5(Frame):
    def __init__(self,master,camera):
        self.__camera=camera
        Frame.__init__( self
                        ,master
                      )
        self.__titulo=Label(self
                            ,text="Configuraçoes"
                            )
        self.__titulo.pack()
        self.__linha1=Frame(self)
        self.__barBrilho=Scale( self.__linha1
                                ,label="Brilho"
                                ,from_=0
                                ,to=100
                                ,orient=HORIZONTAL
                                ,length=109
                                ,command= lambda x: self.__camera.setBrilho(self.__barBrilho.get())
                              )
        self.__barBrilho.pack(side=LEFT)
        self.__barNitidez=Scale(self.__linha1
                                ,label="Nitidez"
                                ,from_=-100
                                ,to=100
                                ,orient=HORIZONTAL
                                ,length=109
                                ,command= lambda x: self.__camera.setNitidez(self.__barNitidez.get())
                              )
        self.__barNitidez.pack(side=LEFT)
        self.__barSaturaçao=Scale(  self.__linha1
                                    ,label="Saturação"
                                    ,from_=-100
                                    ,to=100
                                    ,orient=HORIZONTAL
                                    ,length=109
                                    ,command= lambda x:self.__camera.setSaturacao(self.__barSaturaçao.get())
                                 )
        self.__barSaturaçao.pack(side=LEFT)
        self.__barISO=Scale(self.__linha1
                            ,label="ISO"
                            ,from_=0
                            ,to=1600
                            ,orient=HORIZONTAL
                            ,length=109
                            ,command= lambda dx:self.__camera.setISO(self.__barISO.get())
                            )
        self.__barISO.pack(side=LEFT)
        self.__linha1.pack()
        self.__linha3=Frame(self)
        self.__barContraste=Scale( self.__linha3
                                ,label="Contraste"
                                ,from_=-100
                                ,to=100
                                ,orient=HORIZONTAL
                                ,length=109
                                ,command= lambda x:self.__camera.setContraste(self.__barContraste.get())
                              )
        self.__barContraste.pack(side=LEFT)
        self.__barExposicao=Scale(self.__linha3
                                ,label="Comp. Exposição"
                                ,from_=-25
                                ,to=25
                                ,orient=HORIZONTAL
                                ,length=109
                                ,command= lambda x: self.__camera.setCompensacaoExposicao(self.__barExposicao.get())
                              )
        self.__barExposicao.pack(side=LEFT)
        self.__barZoom=Scale(  self.__linha3
                                    ,label="Digi. Zoom"
                                    ,from_=1
                                    ,to=10
                                    ,orient=HORIZONTAL
                                    ,length=109
                                    ,command= lambda x:self.__camera.setZoom(self.__barZoom.get())
                                 )
        self.__barZoom.pack(side=LEFT)
        self.__barFPS=Scale(self.__linha3
                            ,label="FPS"
                            ,from_=15
                            ,to=60
                            ,orient=HORIZONTAL
                            ,length=109
                            ,res=5
                            ,command= lambda x:self.__camera.setFPS(self.__barFPS.get())
                            )
        self.__barFPS.pack(side=LEFT)
        self.__linha3.pack()
        self.__linha5=Frame(self)
        self.__barTamanho=Scale( self.__linha5
                                ,label="Tamanho"
                                ,from_=100
                                ,to=900
                                ,orient=HORIZONTAL
                                ,length=109
                                ,command=lambda x:self.__camera.setTamanho(self.__barTamanho.get())
                              )
        self.__barTamanho.pack(side=LEFT)
        self.__barRotacao=Scale(self.__linha5
                                ,label="Rotação"
                                ,from_=0
                                ,to=270
                                ,orient=HORIZONTAL
                                ,length=109
                                ,command= lambda x:self.__camera.setRotacao(self.__barRotacao.get())
                              )
        self.__barRotacao.pack(side=LEFT)
        self.__barHorizOffset=Scale(  self.__linha5
                                    ,label="Horaz. Offset"
                                    ,from_=0
                                    ,to=100
                                    ,orient=HORIZONTAL
                                    ,length=109
                                    ,command= lambda x:self.__camera.setHorizontalOffset(self.__barHorizOffset.get())
                                 )
        self.__barHorizOffset.pack(side=LEFT)
        self.__barVertiOffset=Scale(self.__linha5
                            ,label="Verti. Offset"
                            ,from_=0
                            ,to=100
                            ,orient=HORIZONTAL
                            ,length=109
                            ,command= lambda x:self.__camera.setVerticalOffset(self.__barVertiOffset.get())
                            )
        self.__barVertiOffset.pack(side=LEFT)
        self.__linha5.pack()
        self.__linha6=Frame(self)
        self.__flipVerticalVar=BooleanVar()
        self.__flipVerticalVar.set(self.__camera.getInvertidoVertical())
        self.__flipVertical=Checkbutton(self.__linha6,text="Inverter Verticalmente",variable=self.__flipVerticalVar,onvalue=True, offvalue=False
                                        ,command=self.__vert
                                        )
        self.__flipVertical.pack(side=LEFT)
        self.__flipHorizontalVar=BooleanVar()
        self.__flipHorizontalVar.set(self.__camera.getInvertidoHorizontal())
        self.__flipHorizontal=Checkbutton(self.__linha6,text="Inverter Horizontal",variable=self.__flipHorizontalVar,onvalue=True, offvalue=False
                                          ,command=self.__hoz)
        self.__flipHorizontal.pack(side=LEFT)
        self.__linha6.pack(side=LEFT)
    def __vert(self):
        self.__camera.inverterVerticalmente(self.__flipVerticalVar.get())
    def __hoz(self):
        self.__camera.inverterHorizontalmente(self.__flipHorizontalVar.get())