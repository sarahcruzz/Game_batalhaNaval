from PyQt5 import QtWidgets, uic
import random

class telas:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("telas/telainicial.ui")
        self.tela_jogo = uic.loadUi("telas/principal.ui")
        self.tela_inicial.show()
        self.tela_inicial.bStart.clicked.connect(self.mudar_tela)
        self.tela_inicial.bSair.clicked.connect(self.fechar_jogo)

        coordenadas_letra = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        coordenadas_num = ["1","2","3","4","5","6","7","8","9","10"]
        sorteio = []
        posicao = []

        for i in coordenadas_letra:
            for j in coordenadas_num:
                sorteio.append(i + j)

        print(sorteio)
        

        app.exec()
    
    def fechar_jogo(self):
        self.tela_inicial.close()

    def mudar_tela(self):
        self.tela_inicial.close()
        self.tela_jogo.show()

    def sortear(self):
        posicao.append




if __name__ == '__main__':
    c = telas()
