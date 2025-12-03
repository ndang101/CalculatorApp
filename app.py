import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)

from PyQt5.QtCore import Qt

class CalculatorApp(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Calculator App")

    #initialize variables
    self.button_0 = QPushButton("0", self)
    self.button_1 = QPushButton("1", self)
    self.button_2 = QPushButton("2", self)
    self.button_3 = QPushButton("3", self)
    self.button_4 = QPushButton("4", self)
    self.button_5 = QPushButton("5", self)
    self.button_6 = QPushButton("6", self)
    self.button_7 = QPushButton("7", self)
    self.button_8 = QPushButton("8", self)
    self.button_9 = QPushButton("9", self)


    self.display = QLineEdit()

    # operators
    self.add_button = QPushButton("+", self)
    self.subtract_button = QPushButton("-", self)
    self.multiply_button = QPushButton("x", self)
    self.divide_button = QPushButton("÷", self)
    self.calculate_button = QPushButton("=", self)
    self.clear_button = QPushButton("C", self)
    # self.delete_button = QPushButton("⌫", self)

    self.initUI()
    
  def initUI(self):
    # Sets window title
    self.setWindowTitle("Calculator App")
    self.setFixedSize(400, 500)

    # Changes display properties
    self.display.setReadOnly(False)
    self.display.setAlignment(Qt.AlignRight)
    self.display.setFixedSize(380, 50)


    for widget in self.findChildren(QPushButton):
      widget.setFixedSize(80, 80)

    # initialize 4 columns for each button
    vbox1 = QVBoxLayout()
    vbox2 = QVBoxLayout()
    vbox3 = QVBoxLayout()
    vbox4 = QVBoxLayout()

    vbox1.addWidget(self.button_7)
    vbox1.addWidget(self.button_4)
    vbox1.addWidget(self.button_1)
    vbox1.addWidget(self.clear_button)

    vbox2.addWidget(self.button_8)
    vbox2.addWidget(self.button_5)
    vbox2.addWidget(self.button_2)
    vbox2.addWidget(self.button_0)

    vbox3.addWidget(self.button_9)
    vbox3.addWidget(self.button_6)
    vbox3.addWidget(self.button_3)
    vbox3.addWidget(self.calculate_button)

    vbox4.addWidget(self.add_button)
    vbox4.addWidget(self.subtract_button)
    vbox4.addWidget(self.multiply_button)
    vbox4.addWidget(self.divide_button)

    # Puts the 4 columns into 4 rows
    hbox = QHBoxLayout()

    hbox.addLayout(vbox1)
    hbox.addLayout(vbox2)
    hbox.addLayout(vbox3)
    hbox.addLayout(vbox4)

    # Adds a VBox to allow for display to go on top
    main_layout = QVBoxLayout()
    main_layout.addWidget(self.display, alignment=Qt.AlignHCenter) # Display goes first, align it to the center
    main_layout.addLayout(hbox) # Button columns go under it
    

    self.setLayout(main_layout)

    self.display.setObjectName("display")
    

    self.setStyleSheet("""
      QPushButton{
        font-family: calibri
        font-size: 30px;
      }
                       
      QLineEdit#display{
        font-size: 45px;
                       }

    """)

    # Connect signals to each button click
    self.clear_button.clicked.connect(self.controls)
  
  # Allows for inputs 0-9
  def number_press(self):
     pass
  
  # handles + - * / operations and state transistions
  def operations(self):
     pass

  # handles = and C operations
  def controls(self):
     print("yes")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    CalculatorApp = CalculatorApp()
    CalculatorApp.show()
    sys.exit(app.exec_())