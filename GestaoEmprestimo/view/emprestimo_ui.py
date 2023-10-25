# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emprestimo_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import view.resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 280)
        Dialog.setMaximumSize(QSize(410, 280))
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_cpf_funcionario_emprestimo = QLabel(self.widget)
        self.lbl_cpf_funcionario_emprestimo.setObjectName(u"lbl_cpf_funcionario_emprestimo")

        self.verticalLayout.addWidget(self.lbl_cpf_funcionario_emprestimo)

        self.txt_cpf_emprestimo = QLineEdit(self.widget)
        self.txt_cpf_emprestimo.setObjectName(u"txt_cpf_emprestimo")

        self.verticalLayout.addWidget(self.txt_cpf_emprestimo)

        self.lbl_nome_funcionario_emprestimo = QLabel(self.widget)
        self.lbl_nome_funcionario_emprestimo.setObjectName(u"lbl_nome_funcionario_emprestimo")

        self.verticalLayout.addWidget(self.lbl_nome_funcionario_emprestimo)

        self.txt_nome_funcionario_emprestimo = QLineEdit(self.widget)
        self.txt_nome_funcionario_emprestimo.setObjectName(u"txt_nome_funcionario_emprestimo")

        self.verticalLayout.addWidget(self.txt_nome_funcionario_emprestimo)

        self.lbl_tipo_uniforme = QLabel(self.widget)
        self.lbl_tipo_uniforme.setObjectName(u"lbl_tipo_uniforme")

        self.verticalLayout.addWidget(self.lbl_tipo_uniforme)

        self.cb_tipo_uniforme = QComboBox(self.widget)
        self.cb_tipo_uniforme.addItem("")
        self.cb_tipo_uniforme.setObjectName(u"cb_tipo_uniforme")

        self.verticalLayout.addWidget(self.cb_tipo_uniforme)

        self.btn_confirmar_emprestimo = QPushButton(self.widget)
        self.btn_confirmar_emprestimo.setObjectName(u"btn_confirmar_emprestimo")

        self.verticalLayout.addWidget(self.btn_confirmar_emprestimo)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Adicionar empr\u00e9stimo", None))
        self.lbl_cpf_funcionario_emprestimo.setText(QCoreApplication.translate("Dialog", u"CPF funcion\u00e1rio", None))
        self.lbl_nome_funcionario_emprestimo.setText(QCoreApplication.translate("Dialog", u"Nome funcion\u00e1rio", None))
        self.lbl_tipo_uniforme.setText(QCoreApplication.translate("Dialog", u"Tipo de uniforme", None))
        self.cb_tipo_uniforme.setItemText(0, QCoreApplication.translate("Dialog", u"Selecione um uniforme", None))

        self.btn_confirmar_emprestimo.setText(QCoreApplication.translate("Dialog", u"Confirmar", None))
    # retranslateUi

