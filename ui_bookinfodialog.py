# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookinfodialog.ui'
#
# Created: Fri Nov  6 14:42:10 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_BookInfoDialog(object):
    def setupUi(self, BookInfoDialog):
        BookInfoDialog.setObjectName("BookInfoDialog")
        BookInfoDialog.resize(562, 642)
        self.verticalLayout = QtGui.QVBoxLayout(BookInfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.authorsLayout = QtGui.QVBoxLayout()
        self.authorsLayout.setObjectName("authorsLayout")
        self.verticalLayout.addLayout(self.authorsLayout)
        self.titleLabel = QtGui.QLabel(BookInfoDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titleLabel.setFont(font)
        self.titleLabel.setText("Book Title")
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.genresLabel = QtGui.QLabel(BookInfoDialog)
        self.genresLabel.setObjectName("genresLabel")
        self.verticalLayout.addWidget(self.genresLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.coverpageLabel = QtGui.QLabel(BookInfoDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coverpageLabel.sizePolicy().hasHeightForWidth())
        self.coverpageLabel.setSizePolicy(sizePolicy)
        self.coverpageLabel.setText("Image")
        self.coverpageLabel.setObjectName("coverpageLabel")
        self.verticalLayout_2.addWidget(self.coverpageLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.annotationEdit = QtGui.QTextEdit(BookInfoDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annotationEdit.sizePolicy().hasHeightForWidth())
        self.annotationEdit.setSizePolicy(sizePolicy)
        self.annotationEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.annotationEdit.setPalette(palette)
        self.annotationEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.annotationEdit.setReadOnly(True)
        self.annotationEdit.setObjectName("annotationEdit")
        self.verticalLayout_3.addWidget(self.annotationEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fileinfoLayout = QtGui.QVBoxLayout()
        self.fileinfoLayout.setObjectName("fileinfoLayout")
        self.verticalLayout.addLayout(self.fileinfoLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.layout2 = QtGui.QGridLayout()
        self.layout2.setObjectName("layout2")
        self.gridLayout.addLayout(self.layout2, 1, 1, 1, 1)
        self.layout1 = QtGui.QGridLayout()
        self.layout1.setObjectName("layout1")
        self.gridLayout.addLayout(self.layout1, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(BookInfoDialog)
        QtCore.QMetaObject.connectSlotsByName(BookInfoDialog)

    def retranslateUi(self, BookInfoDialog):
        BookInfoDialog.setWindowTitle(QtGui.QApplication.translate("BookInfoDialog", "Book info", None, QtGui.QApplication.UnicodeUTF8))

