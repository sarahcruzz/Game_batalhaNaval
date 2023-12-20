from PyQt5 import QtWidgets, uic
import random
 
class telas:
    def __init__(self):
        app = QtWidgets.QApplication([])
 
        self.telaInicial = uic.loadUi("telaInicial.ui")
        self.tabuleiro = uic.loadUi("tabuleiro.ui")
        self.telaGameOver = uic.loadUi("telaGameOver.ui")
        self.telaWinner = uic.loadUi("telaWinner.ui")
        self.telaInicial.show()
        self.telaInicial.play.clicked.connect(self.mudar_telaInicial)
 
        coordenadasLetras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        coordenadasNumeros = ["1","2","3","4","5","6","7","8","9","10"]
        sorteio = []
 
        sorteio1 = random.sample(coordenadasLetras, 4)
 
        while True:
            sorteio2 = random.sample(coordenadasNumeros, 4)
            if int(sorteio2[1]) > 8:
                continue
            if int(sorteio2[2]) > 7:
                continue
            if int(sorteio2[3]) > 6:
                continue
            else:
                break
 
 
        for i in range(len(sorteio1)):
            sorteio.append(f"{sorteio1[i]}{sorteio2[i]}")
 
        print(sorteio)
 
 
        self.barcos = []
 
        for a in range(len(sorteio)):
            if a == 0:
                for i in range(len(sorteio)):
                    self.barcos.append(sorteio[i])
 
            if a == 1:
                print("\nCOMEÇA O 2")
                separado = list(sorteio[a])
                print(separado)
                self.barcos.append(f"{separado[0]}{int(separado[1])+1}")
                print(self.barcos)
               
           
            if a == 2:
                for i in range(2):
                    print("\nCOMEÇA O 3")
                    separado = list(sorteio[a])
                    print(separado)
                    self.barcos.append(f"{separado[0]}{int(separado[1])+(i + 1)}")
                    print(self.barcos)
 
            if a == 3:
                    for i in range(3):
                        print("\nCOMEÇA O 4")
                        separado = list(sorteio[a])
                        print(separado)
                        self.barcos.append(f"{separado[0]}{int(separado[1])+(i+1)}")
                        print(self.barcos)
 
        for button in self.tabuleiro.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.selecionarBotao)
           
        app.exec()
 
    def mudar_telaInicial(self):
        self.telaInicial.close()
        self.tabuleiro.show()
   
    def selecionarBotao(self):
        sender = self.telaInicial.sender()
        senderCoordenada = sender.objectName()
   
 
        for i in range(1, 21, 1):
            if senderCoordenada in self.barcos:
                sender.setStyleSheet("background-image: url('img/bomba_estourou.png'); border: none")
                self.barcos.remove(senderCoordenada)
 
                if len(self.barcos) == 0:
                    self.tabuleiro.close()
                    self.telaWinner.show()
 
                elif i > 20:
                    self.tabuleiro.close()
                    self.telaGameOver.show()
 
            else:
                sender.setStyleSheet("background-image: url('img/bomba.png'); border: none")
 
 
 
if __name__ == '__main__':
    c = telas()