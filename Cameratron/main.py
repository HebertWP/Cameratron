from tkinter import *
from caixa1 import Caixa1
from caixa2 import Caixa2
from caixa4 import Caixa4
from caixa5 import Caixa5
from camera import Camera
class Interface:
    def __init__(self,master):
        self.__camera=Camera()
        self.__master=master
        self.__master.title("Cameratron")
        self.__caixa1=Caixa1(self.__master,self.__camera)
        self.__caixa1.pack()
        self.__caixa2=Caixa2(self.__master,self.__camera)
        self.__caixa2.pack()
        self.__caixa3=Frame(self.__master)
        self.__caixa4=Caixa4(self.__caixa3,self.__camera)
        self.__caixa5=Caixa5(self.__caixa3,self.__camera)
        self.__caixa4.pack(side=LEFT)
        self.__caixa5.pack(fill=X)
        self.__caixa3.pack(side=LEFT)
 

instancia= Tk()
#instancia.wm_iconbitmap("icono.ico")

interface=Interface(instancia)
instancia.mainloop()
