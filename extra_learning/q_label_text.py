from PyQt5.QtWidgets import QWidget,QVBoxLayout,QApplication, QGridLayout ,QLabel,QLineEdit,QPushButton

import sys

class FilesLocationWidget(QWidget):
  
    def __init__(self, parent=None):
        super(FilesLocationWidget,self).__init__(parent)

        self.yaml_file_location = None
        self.right_checker_board_location = None
        self.right_tube_location = None
        self.left_checker_board_location = None
        self.left_tube_location = None 

        self.set_total_data={}

        self.ui()
        self.show()
    def ui(self):

        grid_layout = QGridLayout()

        # Yaml file location
        self.yaml =QLabel("Set Yaml file location")
        self.yaml_text= QLineEdit()
        self.yaml_text.setPlaceholderText(" Set Yaml file location for parameters.")
        self.yaml_text.textChanged.connect(self.set_yaml_file_location)

        grid_layout.addWidget(self.yaml,0,0)
        grid_layout.addWidget(self.yaml_text,0,1)

        # checker board file location

        # @ left
        self.checker_left =QLabel("Set left file location of checker board")
        self.checker_left_text= QLineEdit()
        self.checker_left_text.setPlaceholderText(" Set Checker board location for saving  Left images.")
        self.checker_left_text.textChanged.connect(self.set_checker_board_left_file_location)

        grid_layout.addWidget(self.checker_left,1,0)
        grid_layout.addWidget(self.checker_left_text,1,1)

        # @ right
        self.checker_right =QLabel("Set right file location of checker board")
        self.checker_right_text= QLineEdit()
        self.checker_right_text.setPlaceholderText(" Set Checker board location for saving  right images.")

        grid_layout.addWidget(self.checker_right,2,0)
        grid_layout.addWidget(self.checker_right_text,2,1)

        # Set images of tube
        # @ tube right
        self.tube_right =QLabel("Set right file location of Tube")
        self.tube_right_text= QLineEdit()
        self.tube_right_text.setPlaceholderText(" Set location for saving the  right tube images.")

        grid_layout.addWidget(self.tube_right,3,0)
        grid_layout.addWidget(self.tube_right_text,3,1)


        # @ tube left 
        self.tube_left =QLabel("Set left file location of Tube")
        self.tube_left_text= QLineEdit()
        self.tube_left_text.setPlaceholderText(" Set location for saving the left tube images.")

        grid_layout.addWidget(self.tube_left,4,0)
        grid_layout.addWidget(self.tube_left_text,4,1)

        button = QPushButton("Ok")
        button.clicked.connect(self.send_file_locations_to_clients)

        v_box= QVBoxLayout()
        v_box.addLayout(grid_layout)
        v_box.addWidget(button)
        self.setLayout(v_box)
    
    def set_yaml_file_location(self):
        """ Set"""
        self.yaml_file_location = self.yaml_text

    def set_checker_board_left_file_location(self):
        """ Set"""
        self.left_checker_board_location=self.checker_left_text.text()
        
        self.left_tube_location = self.tube_left_text.txt()
        self.right_tube_location = self.tube_right_text.text()

    def set_checker_board_right_file_location(self):
        """ Set """
        self.right_checker_board_location = self.checker_right_text.text()
        


    def send_file_locations_to_clients(self):
        print(" out ")


app=QApplication(sys.argv)
a= FilesLocationWidget()
sys.exit(app.exec_())
