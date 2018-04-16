import sys
from PyQt5.Qt import QApplication, QMainWindow, QLineEdit, QWidget, QPushButton, QGridLayout
from PyQt5.Qt import QMenuBar, QMenu, QAction, QDialog, QMdiArea, QListWidget, QListWidgetItem

class BitViewerDialog(QDialog):
    def setupUi(self):
        self.setWindowTitle('BIT Viewer')

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.dataEdit = QLineEdit(self)
        self.bitEdit  = QLineEdit(self)
        button = QPushButton('&Conv', self)
        self.listWidget = QListWidget(self)

        button.clicked.connect(self.onButtonClicked)

        layout.addWidget(self.dataEdit, 0, 0)
        layout.addWidget(self.bitEdit, 1, 0)
        layout.addWidget(button, 0, 1, 2, 1)
        layout.addWidget(self.listWidget, 2, 0, 2, 1)

    def onButtonClicked(self):
        dataText = self.dataEdit.text()
        bitText  = self.bitEdit.text()

        data = 0

        if (dataText.startswith('0x') or dataText.startswith('0X')):
            data = int(dataText[2:], 16)
        else:
            data = int(dataText)

        self.listWidget.addItem(QListWidgetItem(str(data)))


    def __init__(self, parent=None):
        super(QDialog, self).__init__()
        self.setupUi()

class DictionaryDialog(QDialog):
    def setupUi(self):
        self.setWindowTitle('Dictionary')

    def __init__(self, parent=None):
        super(QDialog, self).__init__()
        self.setupUi()

class MainWindow(QMainWindow):
    def onSubWindowCreate(self):
        action = self.sender()
        dialog = None

        if (action.text() == '&BIT Viewer'):
            dialog = BitViewerDialog(self)
        elif (action.text() == '&Dictionary'):
            dialog = DictionaryDialog(self)

        self.mdiArea.addSubWindow(dialog)
        dialog.show()

    def setupUi(self):
        self.setWindowTitle('hello')

        menu = QMenu('&Menu', self)
        self.menuBar().addMenu(menu)

        self.createAction(menu, '&BIT Viewer', self.onSubWindowCreate)
        self.createAction(menu, '&Dictionary', self.onSubWindowCreate)

        self.mdiArea = QMdiArea(self)
        self.setCentralWidget(self.mdiArea)
        
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi()
    def createAction(self, menu, text, signal):
        action = menu.addAction(text)
        action.triggered.connect(signal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
