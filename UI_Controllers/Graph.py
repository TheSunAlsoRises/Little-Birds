import sys
from PyQt4 import QtGui
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random


class GraphUI (QtGui.QDialog):
    def __init__(self, parent=None):
        super(GraphUI, self).__init__(parent)

        # a figure instance to plot on
        #self.figure = Figure()
        self.figure = plt.figure()
        self.setWindowTitle("Analysis Result")
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        #self.button = QtGui.QPushButton('Plot')
        #self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        # Add headline lable here instead of the button
        #layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.plot()

    def plot(self):
        # Set data
        df = pd.DataFrame({
            'group': ['A', 'B'],
            'Joy': [38, 40],
            'Trust': [29, 17],
            'Fear': [100, 90],
            'Surprise': [90, 31],
            'Sadness': [50, 78],
            'Disgust': [95, 88],
            'Anger': [25, 40],
            'Anticipation': [50, 17]
        })

        #initialize the figure
        #my_dpi = 96
        #plt.figure(figsize=(1000 / my_dpi, 1000 / my_dpi), dpi=my_dpi)

        # ------- PART 1: Create background

        # number of variable
        categories = list(df)[1:]
        N = len(categories)

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]


        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)

        # discards the old graph
        #ax.clear()

        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, size=9)
        # Set the distance of x-axe labels from the graph
        ax.tick_params(axis='x', which='major', pad=14)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ["", "20", "","40","","60","","80","","100"], color="grey", size=7)
        plt.ylim(0, 100)

        # ------- PART 2: Add plots

        # Plot each individual = each line of the data
        # I don't do a loop, because plotting more than 3 groups makes the chart unreadable

        # Ind1
        values = df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Tweets")
        ax.fill(angles, values, 'b', alpha=0.1)

        # Ind2
        values = df.loc[1].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Scripts")
        ax.fill(angles, values, 'r', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(-0.1, 0.1))

        # create an axis
        #ax = self.figure.add_subplot(111)

        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = GraphUI()
    main.show()

    sys.exit(app.exec_())
