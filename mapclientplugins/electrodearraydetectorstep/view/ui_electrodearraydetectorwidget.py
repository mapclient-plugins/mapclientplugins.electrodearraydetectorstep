# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'electrodearraydetectorwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from opencmiss.utils.zinc.widgets.basesceneviewerwidget import BaseSceneviewerWidget

class Ui_ElectrodeArrayDetectorWidget(object):
    def setupUi(self, ElectrodeArrayDetectorWidget):
        if not ElectrodeArrayDetectorWidget.objectName():
            ElectrodeArrayDetectorWidget.setObjectName(u"ElectrodeArrayDetectorWidget")
        ElectrodeArrayDetectorWidget.resize(870, 576)
        self.horizontalLayout = QHBoxLayout(ElectrodeArrayDetectorWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.controlPanel_groupBox = QGroupBox(ElectrodeArrayDetectorWidget)
        self.controlPanel_groupBox.setObjectName(u"controlPanel_groupBox")
        self.verticalLayout = QVBoxLayout(self.controlPanel_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.time_groupBox = QGroupBox(self.controlPanel_groupBox)
        self.time_groupBox.setObjectName(u"time_groupBox")
        self.gridLayout_4 = QGridLayout(self.time_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.timePlayStop_pushButton = QPushButton(self.time_groupBox)
        self.timePlayStop_pushButton.setObjectName(u"timePlayStop_pushButton")

        self.gridLayout_4.addWidget(self.timePlayStop_pushButton, 1, 1, 1, 1)

        self.timeValue_label = QLabel(self.time_groupBox)
        self.timeValue_label.setObjectName(u"timeValue_label")

        self.gridLayout_4.addWidget(self.timeValue_label, 0, 0, 1, 1)

        self.timeValue_doubleSpinBox = QDoubleSpinBox(self.time_groupBox)
        self.timeValue_doubleSpinBox.setObjectName(u"timeValue_doubleSpinBox")
        self.timeValue_doubleSpinBox.setMaximum(12000.000000000000000)

        self.gridLayout_4.addWidget(self.timeValue_doubleSpinBox, 0, 1, 1, 1)

        self.timeLoop_checkBox = QCheckBox(self.time_groupBox)
        self.timeLoop_checkBox.setObjectName(u"timeLoop_checkBox")

        self.gridLayout_4.addWidget(self.timeLoop_checkBox, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.time_groupBox)

        self.groupBox_2 = QGroupBox(self.controlPanel_groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.detectElectrodes_pushButton = QPushButton(self.groupBox_2)
        self.detectElectrodes_pushButton.setObjectName(u"detectElectrodes_pushButton")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.detectElectrodes_pushButton)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.trackElectrodePoints_pushButton = QPushButton(self.groupBox_3)
        self.trackElectrodePoints_pushButton.setObjectName(u"trackElectrodePoints_pushButton")

        self.horizontalLayout_4.addWidget(self.trackElectrodePoints_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.groupBox_3)

        self.reset_pushButton = QPushButton(self.groupBox_2)
        self.reset_pushButton.setObjectName(u"reset_pushButton")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.reset_pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.controlPanel_groupBox)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.statusText_label = QLabel(self.groupBox)
        self.statusText_label.setObjectName(u"statusText_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusText_label.sizePolicy().hasHeightForWidth())
        self.statusText_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.statusText_label)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame = QFrame(self.controlPanel_groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.done_pushButton = QPushButton(self.frame)
        self.done_pushButton.setObjectName(u"done_pushButton")

        self.horizontalLayout_2.addWidget(self.done_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.controlPanel_groupBox)

        self.sceneviewer_widget = BaseSceneviewerWidget(ElectrodeArrayDetectorWidget)
        self.sceneviewer_widget.setObjectName(u"sceneviewer_widget")
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.sceneviewer_widget)


        self.retranslateUi(ElectrodeArrayDetectorWidget)

        QMetaObject.connectSlotsByName(ElectrodeArrayDetectorWidget)
    # setupUi

    def retranslateUi(self, ElectrodeArrayDetectorWidget):
        ElectrodeArrayDetectorWidget.setWindowTitle(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Electrode Array Detector", None))
        self.controlPanel_groupBox.setTitle(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Control Panel", None))
        self.time_groupBox.setTitle(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Time:", None))
        self.timePlayStop_pushButton.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Play", None))
        self.timeValue_label.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Time value:", None))
        self.timeLoop_checkBox.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Loop", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Activity:", None))
        self.detectElectrodes_pushButton.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Detect electrodes", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Track electrode points", None))
        self.trackElectrodePoints_pushButton.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Track", None))
        self.reset_pushButton.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Reset", None))
        self.groupBox.setTitle("")
        self.statusText_label.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"TextLabel", None))
        self.done_pushButton.setText(QCoreApplication.translate("ElectrodeArrayDetectorWidget", u"Done", None))
    # retranslateUi

