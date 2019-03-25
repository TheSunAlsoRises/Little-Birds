import sys
from sys import exit
from PyQt4 import QtGui
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
import ManagerUIsController, Graph_UI

class GraphUI (QtGui.QDialog):

    window = None
    tweetsSum = None
    scriptsSum = None
    prediction = None
    prediction_size = None

    def __init__(self, parent=None):
        super(GraphUI, self).__init__(parent)

        #self.ui = Graph_UI.Ui_Form()
        #self.ui.setupUi(self)

        # a figure instance to plot on
        #self.figure = Figure()S
        self.figure = plt.figure()
        self.setWindowTitle("Analysis Result")
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # O u r  - C o d e :
        userSymbol = "@"

        # If there are no analysis results
        if GraphUI.scriptsSum is None:
            GraphUI.scriptsSum = list()
            for i in range(0, 4):
                GraphUI.scriptsSum.insert(i, "")
            GraphUI.scriptsSum.insert(3, 0)
            GraphUI.scriptsSum[0] = list()
            for i in range(0, 8):
                GraphUI.scriptsSum[0].insert(i, 0)

        if GraphUI.prediction is None:
            GraphUI.prediction = list()
            for i in range(0, 8):
                GraphUI.prediction.insert(i, 0)

        if GraphUI.tweetsSum is None:
            GraphUI.tweetsSum = list()
            for i in range(0, 6):
                GraphUI.tweetsSum.insert(i, "")
            GraphUI.tweetsSum.insert(5, 0)
            GraphUI.tweetsSum[0] = list()
            for i in range(0, 8):
                GraphUI.tweetsSum[0].insert(i, 0)
            userSymbol = ""

        # Set the window
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.window.setGeometry(self.window.x(), self.window.y() , 1000, 200)

        # Set the headline
        labelText = ""
        if self.window.character_text is not None:
            labelText = str(self.window.character_text)
        elif self.window.location_text is not None:
            labelText = str(self.window.location_text)
        elif self.window.house is not None:
            labelText = "House " + str(self.window.house)
        # Capitalize the name
        labelText = labelText[0].upper() + labelText[1:]
        lastNameIndex = labelText.find(" ") + 1
        labelText = labelText[:lastNameIndex] + labelText[lastNameIndex].upper() + labelText[lastNameIndex + 1:]
        q = '"'
        labelText += " in episode " + str(self.window.episode) + " - " + str(self.window.episode_text)

        self.label = QtGui.QLabel(labelText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);"
                                 "color: rgb(0, 0, 0);"
                                 "margin-top: 0px; margin-bottom: 10px; margin-right: 15px; margin-left: 15px;"
                                 "padding: 0px;"
                                 "font-size: 35px;")

        # Set secondary headline
        self.second_label = QtGui.QLabel("Produced from " + str(GraphUI.tweetsSum[5]) + " tweets, "
                                         + str(GraphUI.scriptsSum[3]) + " script lines, " +
                                         str(round(0.8*GraphUI.prediction_size)) + " for training set and " +
                                         str(round(0.2*GraphUI.prediction_size)) + " for testing set")
        self.second_label.setAlignment(QtCore.Qt.AlignCenter)
        self.second_label.setStyleSheet("background-color: rgb(255, 255, 255);"
                                        "color: rgb(0, 0, 0);"
                                        "margin-top: 0px; margin-bottom: 10px; margin-right: 15px; margin-left: 15px;"
                                        "padding: 0px;"
                                        "font-size: 18px;")

        # Set the graph's size
        self.canvas.setFixedSize(QtCore.QSize(500, 500))
        #self.canvas.setMaximumWidth(1200)

        # Set the representative tweets

        self.tweet1 = QtGui.QLabel(str(GraphUI.tweetsSum[1]) + "\n\n" + userSymbol + str(GraphUI.tweetsSum[2]))
        self.tweet1.setWordWrap(True)
        self.tweet1.setMaximumWidth(350)
        self.tweet1.setStyleSheet("background-color: rgb(29, 202, 255);"
                                  "color: rgb(0, 0, 0);"
                                  "margin-top: 5px; margin-bottom: 15px; margin-right: 15px; margin-left: 15px;"
                                  "padding: 15px;"
                                  "font-size: 18px;")

        self.tweet2 = QtGui.QLabel(str(GraphUI.tweetsSum[3]) + "\n\n" + userSymbol + str(GraphUI.tweetsSum[4]))
        self.tweet2.setWordWrap(True)
        self.tweet2.setMaximumWidth(350)
        self.tweet2.setStyleSheet("background-color: rgb(29, 202, 255);"
                                  "color: rgb(0, 0, 0);"
                                  "margin-top: 15px; margin-bottom: 5px; margin-right: 15px; margin-left: 15px;"
                                  "padding: 15px;"
                                  "font-size: 18px;")

        # abort if there are no analysis results
        if userSymbol == "":
            self.tweet1.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.tweet2.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Set the restart and quit buttons

        #self.restart_button = QtGui.QPushButton('Restart')
        self.restart_button = QtGui.QPushButton()
        self.restart_button.clicked.connect(GraphUI.window.startMainPageUI)
        #self.restart_button.setMaximumWidth(91)
        #self.restart_button.setMaximumHeight(91)
        self.restart_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reboot-filled-100.png')))
        self.restart_button.setFixedSize(QtCore.QSize(90, 90))
        self.restart_button.setIconSize(QtCore.QSize(80, 80))

        #self.restart_button.setGeometry(self.restart_button.x(), self.restart_button.y(), 91, 91)
        #self.restart_button.setStyleSheet("background-color: #000000; color: black; border: 4.5px solid #111111; margin: 4px; border-radius: 40px;")


        #self.quit_button = QtGui.QPushButton('Quit')
        self.quit_button = QtGui.QPushButton()
        self.quit_button.clicked.connect(exit)
        self.quit_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-shutdown-100.png')))
        self.quit_button.setFixedSize(QtCore.QSize(90, 90))
        self.quit_button.setIconSize(QtCore.QSize(80, 80))

        # set the layout

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.second_label)

        # Set an inner layout for the graph and the tweets
        middle_layout = QtGui.QHBoxLayout()

        # Set an inner-inner layout for the quit button
        leftbtn_layout = QtGui.QVBoxLayout()
        leftbtn_layout.addStretch()
        leftbtn_layout.addWidget(self.quit_button)
        middle_layout.addLayout(leftbtn_layout)

        middle_layout.addStretch()

        # Set an inner-inner layout for the graph and its toolbar
        graph_layout = QtGui.QVBoxLayout()
        graph_layout.addWidget(self.toolbar)
        graph_layout.addWidget(self.canvas)
        middle_layout.addLayout(graph_layout)

        # Set an inner-inner layout for the tweets
        tweets_layout = QtGui.QVBoxLayout()
        tweets_layout.addWidget(self.tweet1)
        tweets_layout.addWidget(self.tweet2)
        middle_layout.addLayout(tweets_layout)

        middle_layout.addStretch()

        # Set an inner-inner layout for the restart button
        rightbtn_layout = QtGui.QVBoxLayout()
        rightbtn_layout.addStretch()
        rightbtn_layout.addWidget(self.restart_button)
        middle_layout.addLayout(rightbtn_layout)

        layout.addLayout(middle_layout)

        # Set an inner layout for the buttons
        #down_layout = QtGui.QHBoxLayout()
        #down_layout.addWidget(self.quit_button)
        #down_layout.addStretch()
        #down_layout.addWidget(self.restart_button)
        #layout.addLayout(down_layout)

        self.setLayout(layout)

        # Clean the chosen parameters for the next round
        self.window.parameters = None
        self.window.episode = None
        self.window.episode_text = None
        self.window.category = None
        self.window.character = None
        self.window.character_text = None
        self.window.location = None
        self.window.location_text = None
        self.window.house = None

        # Show graph
        self.plot()

    def plot(self):
        # Set data
        df = pd.DataFrame({
            'group': ['Tweets', 'Scripts','Prediction'],
            'Joy': [GraphUI.tweetsSum[0][5], GraphUI.scriptsSum[0][5], GraphUI.prediction[5]],
            'Trust': [GraphUI.tweetsSum[0][7], GraphUI.scriptsSum[0][7], GraphUI.prediction[7]],
            'Fear': [GraphUI.tweetsSum[0][2], GraphUI.scriptsSum[0][2], GraphUI.prediction[2]],
            'Surprise': [GraphUI.tweetsSum[0][4], GraphUI.scriptsSum[0][4], GraphUI.prediction[4]],
            'Sadness': [GraphUI.tweetsSum[0][3], GraphUI.scriptsSum[0][3], GraphUI.prediction[3]],
            'Disgust': [GraphUI.tweetsSum[0][1], GraphUI.scriptsSum[0][1], GraphUI.prediction[1]],
            'Anger': [GraphUI.tweetsSum[0][0], GraphUI.scriptsSum[0][0], GraphUI.prediction[0]],
            'Anticipation': [GraphUI.tweetsSum[0][6], GraphUI.scriptsSum[0][6], GraphUI.prediction[6]]
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

        # Ind3
        values = df.loc[2].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Prediction")
        ax.fill(angles, values, 'g', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.15, 0.05))

        # create an axis
        #ax = self.figure.add_subplot(111)

        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = GraphUI()
    main.show()

    sys.exit(app.exec_())
