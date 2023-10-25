import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QPalette, QColor, Qt

from view.main_ui import Ui_MainWindow
from view.emprestimo_ui import Ui_Dialog
from infra.config.connection import DBConnectionHandler


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_emprestar.clicked.connect(self.adicionar_emprestimo)

        data_base = DBConnectionHandler()

    def adicionar_emprestimo(self):
        self.emprestimo_dialog = EmprestimoDialog()
    #    self.emprestimo_dialog.finished.connect(self.on_emprestimo_closed)
        self.emprestimo_dialog.show() #abrir a segunda tela
    #    self.hide()

   # def on_emprestimo_closed(self):    #função para fechar a janela principal qndo abrir essa
   #     self.show()

class EmprestimoDialog(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(EmprestimoDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication()

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
    palette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))

    app.setPalette(palette)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
