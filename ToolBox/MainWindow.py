from PyQt5.Qt import QMenuBar, QMenu, QAction, QDialog, QMdiArea, QListWidget, QListWidgetItem, QMainWindow
from BitViewerDialog import BitViewerDialog
from DictionaryDialog import DictionaryDialog

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