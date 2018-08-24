import picamera
import os
import time
class Camera:
    def __init__(self,pathout="~/Desktop/Fotos"):
        self.__camera = picamera.PiCamera()
        self.__size=100;
        self.__visualizando=False
        self.__gravando=False
        self.reniciarCamera()
        self.setTamanho()
        self.setPathOut(pathout)
    
    def setPathOut(self,pathout):
        self.__pathOut=pathout
    
    def getPathOut(self):
        return self.__pathOut

    def tirarFoto(self,nome):
        if not os.path.exists(self.getPathOut()):
            #if not, create it:
            os.mkdir(self.getPathOut())

        #get the present time, down to seconds
        #print (time.strftime("%Y-%m-%d-%H-%M-%S"))
        
        # Camera warm-up time
        time.sleep(1)
        self.__camera.capture(self.getPathOut() + nome +'.jpg')

        
    def setEfeitoImagem(self,efeito="none"):
        self.__efeitoImagem=efeito
        self.__camera.image_effect = efeito
        
    def getEfeitoimagem(self):
        return self.__efeitoImagem
        
    def setBalancoBranco(self,balanco="auto"):
        self._balancoBranco=balanco
        if balanco == "green":
            self.__camera.awb_mode = "off"
            self.__camera.awb_gains = (1, 1)
        elif balanco == "red":
            self.__camera.awb_mode = "off"
            self.__camera.awb_gains = (8.0, 0.9)
        elif balanco == "blue":
            self.__camera.awb_mode = "off"
            self.__camera.awb_gains = (0.9, 8.0)
        else:
            self.__camera.awb_mode=balanco
        
    def setModoExposicao(self,exposicao="auto"):
        self.__camera.exposure_mode = exposicao
        
    def setModoMedicao(self,medicao="average"):
        self.__camera.meter_mode = medicao
        
    def inverterHorizontalmente(self,boolean="False"):
        self.__vet=boolean
        self.__camera.hflip=boolean
    
    def getInvertidoVertical(self):
        return self.__vet
    
    def inverterVerticalmente(self,boolean="False"):
        self.__hor=boolean
        self.__camera.vflip=boolean
        
    def getInvertidoHorizontal(self):
        return self.__hor
    
    def iniciarGravacao(self,name=""):
        if not os.path.exists(self.getPathOut()):
            #if not, create it:
            os.mkdir(self.getPathOut())
        self.__gravando=True
        self.__camera.resolution = (1280, 720)
        self.__camera.start_recording(self.getPathOut()+ name + ".h264")
     
    def getGravando(self):
        return self.__gravando

    def pararGravacao(self):
        self.__gravando=False
        self.__camera.stop_recording()
        self.__camera.resolution= self.getResulucao()
        
    def setBrilho(self,valor= 50):
        self.__camera.brightness = valor
 
    def setISO(self,valor=100):
        self.__camera.ISO=valor
        
    def setNitidez(self,valor=0):
        self.__camera.sharpness = valor

    def setSaturacao(self,valor=0):
        self.__camera.saturation=valor

    def visualizar(self,sim=True):
        if sim is True:
            self.__camera.start_preview(fullscreen=False, window=(0,0, self.__tamanho,self.__tamanho))
            self.__visualizando=True
        else:
            self.__camera.stop_preview()
            self.__visualizando=False
    
    def setTamanho(self,valor=100):
        self.__tamanho=valor
        if self.__visualizando is True:
                self.visualizar()

    def setContraste(self,valor=0):
        self.__camera.contrast=valor

    def setRotacao(self,valor=0):
        self.__camera.rotation=valor

    def setCompensacaoExposicao(self,valor=0):
        self.__camera.exposure_compensation=valor

    def reniciarCamera(self):
        self.setBrilho()
        self.setSaturacao()
        self.setContraste()
        self.setNitidez()
        self.setRotacao()
        self.inverterHorizontalmente()
        self.inverterVerticalmente()
        self.setISO()
        self.setCompensacaoExposicao()
        self.setModoMedicao()
        self.setModoExposicao()
        self.setBalancoBranco()
        self.setEfeitoImagem()
        self.setResolucao()
        self.setFPS()
        self.__zoom=1
        self.__verticalOffset=0
        self.__horizontalOffset=0
        
    def setResolucao(self,resolucao="2592x1944"):
        if resolucao is "2592x1944":
            self.__resolucao=(2592,1944)
            self.__camera.resolution = (2592,1944)
        elif resolucao is '1920x1080':
            self.__resolucao=(1920,1080)
            self.__camera.resolution = (1920,1080)
        elif resolucao is "1296x972":
            self.__resolucao=(1296,972)
            self.__camera.resolution = (1296,972)
        elif resolucao is "1296x730":
            self.__resolucao=(1296,730)
            self.__camera.resolution = (1296,730)
        elif resolucao is "640x480":
            self.__resolucao=(640,480)
            self.__camera.resolution = (640,480)
    
    def getResulucao(self):
        return self.__resolucao
    
    def setFPS(self,num=15):
        self.__FPS=num
        self.__camera.framerate= num

    def getFPS(self):
        return self.__FPS
    
    def setHorizontalOffset(self,num=0):
        self.__horizontalOffset=num
        self.setZoom(self.getZoom())
    
    def getHorizontalOffset(self):
        return self.__horizontalOffset
    
    def setVerticalOffset(self,num=0):
        self.__verticalOffset=num
        self.setZoom(self.getZoom())
    
    def getVerticalOffset(self):
        return self.__verticalOffset
    
    def setZoom(self,valor=1):
        zoomSide = 1 / valor
        edge = 1 - zoomSide
        self.__camera.zoom = ((self.getHorizontalOffset()/ 100.0) * edge,
                               (self.getVerticalOffset() / 100.0) * edge,
                               1 / valor,
                               1 / valor)
        self.__zoom=valor
    
    def getZoom(self):
        return self.__zoom
    def setEfeitoCor(self,valor="auto"):
        self.__corEfeito = valor
        if valor == "BW":
            self.__camera.color_effects = (128, 128)
        elif valor == "RED":
            self.__camera.color_effects = (0, 255)
        elif valor == "BLUE":
            self.__camera.color_effects = (255, 0)
        elif valor == "GREEN":
            self.__camera.color_effects = (0, 0)
        else:
            self.__camera.color_effects = None
        
