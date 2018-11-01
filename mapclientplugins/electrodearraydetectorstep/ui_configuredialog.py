# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapclientplugins\electrodearraydetectorstep\qt\configuredialog.ui'
#
# Created: Fri Oct 26 10:10:53 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.identifier_label = QtGui.QLabel(self.configGroupBox)
        self.identifier_label.setObjectName("identifier_label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.identifier_label)
        self.identifier_lineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.identifier_lineEdit.setObjectName("identifier_lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.identifier_lineEdit)
        self.frame = QtGui.QFrame(self.configGroupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fiducials_radioButton = QtGui.QRadioButton(self.frame)
        self.fiducials_radioButton.setChecked(True)
        self.fiducials_radioButton.setObjectName("fiducials_radioButton")
        self.verticalLayout.addWidget(self.fiducials_radioButton)
        self.electrode_radioButton = QtGui.QRadioButton(self.frame)
        self.electrode_radioButton.setObjectName("electrode_radioButton")
        self.verticalLayout.addWidget(self.electrode_radioButton)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.frame)
        self.verticalLayout_2.addWidget(self.configGroupBox)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure Step", None, QtGui.QApplication.UnicodeUTF8))
        self.identifier_label.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.fiducials_radioButton.setText(QtGui.QApplication.translate("ConfigureDialog", "Detect and output fiducial markers only", None, QtGui.QApplication.UnicodeUTF8))
        self.electrode_radioButton.setText(QtGui.QApplication.translate("ConfigureDialog", "Detect and output electrode locations only", None, QtGui.QApplication.UnicodeUTF8))

