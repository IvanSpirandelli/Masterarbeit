import random

import PySide2
import gudhi

from PySide2.QtWidgets import (QVBoxLayout, QWidget, QPushButton, QGroupBox, QGridLayout, QLineEdit)
from PySide2.QtCore import Slot
from CustomQWidgets.point_cloud_generation_widget import PointCloudGenerationWidget


class SetupTabWidget(QWidget):
    def __init__(self, main_ui):
        super().__init__()
        self.layout = QGridLayout(self)
        self.main_ui = main_ui

        point_set_generation_box = QGroupBox("Point Set Generation")
        point_set_generation_layout = QVBoxLayout(point_set_generation_box)
        point_cloud_generator = PointCloudGenerationWidget(self, self.main_ui.computation_handler)
        point_set_generation_layout.addWidget(point_cloud_generator)
        point_set_generation_box.setMaximumWidth(200)
        point_set_generation_box.setMaximumHeight(250)
        self.layout.addWidget(point_set_generation_box)

        point_set_pass_box = QGroupBox("Point Set Pass")
        point_set_pass_layout = QVBoxLayout(point_set_pass_box)
        point_set_pass_box.setMaximumWidth(200)
        point_set_pass_box.setMaximumHeight(250)
        self.in_field = QLineEdit()
        point_set_pass_layout.addWidget(self.in_field)
        pass_button = QPushButton("Set Point Set")

        pass_button.clicked.connect(self.pass_points)
        point_set_pass_layout.addWidget(pass_button)

        self.layout.addWidget(point_set_pass_box)

        generate_filtration_vis = QPushButton("Generate Filtration Visuals")
        generate_filtration_vis.clicked.connect(self.generate_filtration_vis_clicked)
        self.layout.addWidget(generate_filtration_vis)




    @Slot()
    def generate_filtration_vis_clicked(self):
        self.main_ui.generate_filtration_tab()

    @Slot()
    def pass_points(self):
        points = eval(self.in_field.text())
        print(points)
        self.main_ui.computation_handler.set_points(points)