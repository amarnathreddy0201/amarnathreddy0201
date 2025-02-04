""" The Aim of this file is to show the reprojection error of checker board"""
# First party
import logging

# 3rd party
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QVBoxLayout, QWidget

logger = logging.getLogger(__name__)


class SomeWindow(QWidget):
    """The Aim of this class is to set the parameters of cameras from UI"""

    def __init__(self, parent=None):
        super(ReProjectionWindow, self).__init__(parent)
        self.show_projection_window()

    def show_projection_window(self):
        """Embedded parameters to UI"""
        try:
            grid_for_projection_error = QGridLayout()
            self.setWindowTitle("Reprojection ...")

            self.calibrating = QLabel("Calibrating .....")
            self.calibrating.setStyleSheet("QLabel {  font-size: %dpx; }" % 20)

            # GridLayout for single and final reprojection widgets.
            grid_for_projection_error.addWidget(self.calibrating, 0, 0)

            single_pro_text = QLabel("Single Reprojection Error :")
            single_pro_text.setStyleSheet("QLabel {  font-size: %dpx; }" % 20)

            self.single_projection_error = QLabel()
            self.single_projection_error.setStyleSheet("QLabel {  font-size: %dpx; }" % 20)
            grid_for_projection_error.addWidget(single_pro_text, 1, 0)
            grid_for_projection_error.addWidget(self.single_projection_error, 1, 1)

            final_pro_text = QLabel("Final Reprojection Error")
            final_pro_text.setStyleSheet("QLabel {  font-size: %dpx; }" % 20)
            self.final_projection_error = QLabel()
            self.final_projection_error.setStyleSheet("QLabel {  font-size: %dpx; }" % 20)
            grid_for_projection_error.addWidget(final_pro_text, 2, 0)
            grid_for_projection_error.addWidget(self.final_projection_error, 2, 1)

            label_for_text_ok_button = QGridLayout()
            self.success_or_failure_label = QLabel()
            self.success_or_failure_label.setStyleSheet("QLabel {  font-size: %dpx; }" % 20)

            self.success_button = QPushButton("OK")
            self.success_button.clicked.connect(self.close_window_and_goto_anotherprocess)
            self.success_button.setDisabled(True)

            label_for_text_ok_button.addWidget(self.success_or_failure_label)
            label_for_text_ok_button.addWidget(self.success_button)

            # This is for corner detection of checkerboard images.
            self.checker_board_corners = QVBoxLayout()
            self.checker_board_label = QLabel()
            # self.checker_board_label.setFixedSize(640,480)
            self.checker_board_corners.addWidget(self.checker_board_label)

            # This is main widget for embedding all widgets.
            ver_box = QVBoxLayout()
            ver_box.addLayout(grid_for_projection_error)

            verticle_widget = QVBoxLayout()
            verticle_widget.addLayout(ver_box)
            verticle_widget.addLayout(self.checker_board_corners)
            verticle_widget.addLayout(label_for_text_ok_button)

            self.setLayout(verticle_widget)
            self.show()

        except Exception as error:
            logger.info(" Error @ show_projection_window , error :%s", error)

    def close_window_and_goto_anotherprocess(self):
        """For closing the window"""
        self.close()
