from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QFileDialog,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QApplication
)


class Ui_TestQFileDialog(QWidget):
    def __init__(self, parent=None) -> None:
        super(Ui_TestQFileDialog, self).__init__(parent)

        self.data_location1 = None
        self.data_location2 = None
        self.data_location3 = None
        self.setupUi()
        self.show()

    def _open_file_dialog(self, lineeditr):
        directory = str(QFileDialog.getExistingDirectory())
        lineeditr.setText("{}".format(directory))


    def _set_text(self, text):
        return text

    def setupUi(self):

        self.setWindowTitle("File saving location")
        self.setMinimumSize(400, 240)

        # ------------------------- first set  ------------------------------------------------------
        TestQFileDialog = QDialog()

        self.toolButtonOpenDialog = QToolButton(TestQFileDialog)

        self.label1 = QLineEdit(TestQFileDialog)
        self.label1.setEnabled(False)
        self.label1.setPlaceholderText("file location")
        

        #  Function for storing yaml file location
        self.label1.textChanged.connect(self.file_location1)
        self.toolButtonOpenDialog.clicked.connect(lambda: (self._open_file_dialog(self.label1)))

        # ----------------------------- second set  --------------------------------------------------------
        TestQFileDialog1 = QDialog()

        self.toolButtonOpenDialog1 = QToolButton(TestQFileDialog1)

        self.label3 = QLineEdit(TestQFileDialog1)
        self.label3.setEnabled(False)
        self.label3.setPlaceholderText(" file location")
        self.label3.textChanged.connect(self.file_location2)

        
        self.toolButtonOpenDialog1.clicked.connect(lambda: (self._open_file_dialog(self.label3)))

        # -----------------------------------------  3rd set --------------------------------------------------------------

        TestQFileDialog2 = QDialog()
        

        self.toolButtonOpenDialog2 = QToolButton(TestQFileDialog2)
        

        self.label2 = QLineEdit(TestQFileDialog2)
        self.label2.setEnabled(False)
        self.label2.setPlaceholderText("location location")

        self.label2.textChanged.connect(self.file_location3)

   
        self.toolButtonOpenDialog2.clicked.connect(lambda: (self._open_file_dialog(self.label2)))

        self.retranslateUi(TestQFileDialog, self.toolButtonOpenDialog, "TestQFileDialog", "data")
        self.retranslateUi(TestQFileDialog1, self.toolButtonOpenDialog1, "TestQFileDialog1", "data1")
        self.retranslateUi(TestQFileDialog2, self.toolButtonOpenDialog2, "TestQFileDialog2", "data2")
        QtCore.QMetaObject.connectSlotsByName(TestQFileDialog)
        QtCore.QMetaObject.connectSlotsByName(TestQFileDialog1)
        QtCore.QMetaObject.connectSlotsByName(TestQFileDialog2)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label1, 0, 0)
        grid_layout.addWidget(self.toolButtonOpenDialog, 0, 1)

        grid_layout.addWidget(self.label3, 1, 0)
        grid_layout.addWidget(self.toolButtonOpenDialog1, 1, 1)

        grid_layout.addWidget(self.label2, 2, 0)
        grid_layout.addWidget(self.toolButtonOpenDialog2, 2, 1)

        button = QPushButton("ok")
        #button.clicked.connect(self.send_file_locations_to_client)

        ve_box = QVBoxLayout()
        ve_box.addLayout(grid_layout)
        ve_box.addWidget(button)
        self.setLayout(ve_box)

    def file_location1(self):
       
        self.data_location1 = self.label1.text()

    def file_location2(self):
        
        self.data_location2 = self.label3.text()

    def file_location3(self):
        
        self.data_location3 = self.label2.text()


    def retranslateUi(self, TestQFileDialog, tool, dialogue: str, d: str):
        _translate = QtCore.QCoreApplication.translate
        TestQFileDialog.setWindowTitle(_translate(dialogue, d))
        tool.setText(_translate(dialogue, "..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_TestQFileDialog()

    sys.exit(app.exec_())
