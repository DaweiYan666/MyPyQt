from PyQt5.Qt import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def OnButtonClicked(self):
        self.lineEdit.setText("hello")

    def setupUi(self):
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        
        self.lineEdit = QLineEdit(self)
        self.layout.addWidget(self.lineEdit, 1, 1);
        
        self.button = QPushButton(self)
        self.layout.addWidget(self.button, 2, 1);
        
        def __init__(self):
            super(QMainWindow,self).__init__()
            self.setupUi()