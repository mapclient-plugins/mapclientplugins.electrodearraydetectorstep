# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.verticalLayout_2 = QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.identifier_label = QLabel(self.configGroupBox)
        self.identifier_label.setObjectName(u"identifier_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.identifier_label)

        self.identifier_lineEdit = QLineEdit(self.configGroupBox)
        self.identifier_lineEdit.setObjectName(u"identifier_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.identifier_lineEdit)

        self.frame = QFrame(self.configGroupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.frame)


        self.verticalLayout_2.addWidget(self.configGroupBox)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.identifier_label.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
    # retranslateUi

