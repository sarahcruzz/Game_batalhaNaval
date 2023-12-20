from PyQt5 import QtWidgets, uic

class telas:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("telas/telainicial.ui")
        self.tela_jogo = uic.loadUi("telas/principal.ui")
        self.tela_inicial.show()
        self.tela_inicial.bStart.clicked.connect(self.mudar_tela)
        self.tela_inicial.bSair.clicked.connect(self.fechar_jogo)
        app.exec()
    
    def fechar_jogo(self):
        self.tela_inicial.close()

    def mudar_tela(self):
        self.tela_inicial.close()
        self.tela_jogo.show()

if __name__ == '__main__':
    c = telas()
