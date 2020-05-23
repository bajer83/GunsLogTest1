from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure


class MplLineWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure()) # creates main Figure object

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        # self.canvas.axes_guns_shots_bar_plot = self.canvas.figure.add_subplot(141) # creates an array of sub
        # self.canvas.axes_airline_shots_plot = self.canvas.figure.add_subplot(142) # creates an array of sub
        # self.canvas.axes_tbs_plot = self.canvas.figure.add_subplot(143) # creates an array of sub
        # self.canvas.axes_solenoids_bar_plot = self.canvas.figure.add_subplot(144) # creates an array of sub

        self.canvas.axes_guns_shots_bar_plot = self.canvas.figure.add_subplot(221)  # creates an array of sub
        self.canvas.axes_airline_shots_plot = self.canvas.figure.add_subplot(222)  # creates an array of sub
        self.canvas.axes_tbs_plot = self.canvas.figure.add_subplot(223)  # creates an array of sub
        self.canvas.axes_solenoids_bar_plot = self.canvas.figure.add_subplot(224)  # creates an array of sub

        self.canvas.figure.subplots_adjust(wspace=0.3, hspace=0.4)

        self.setLayout(vertical_layout)