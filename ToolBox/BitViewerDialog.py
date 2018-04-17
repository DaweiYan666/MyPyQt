from PyQt5.Qt import QGridLayout, QLineEdit, QPushButton, QDialog, QListWidget, QListWidgetItem
from BitFields import BitFields, BitField

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

        if (dataText.startswith('0x') or dataText.startswith('0X')):
            data = int(dataText[2:], 16)
        else:
            data = int(dataText)

        self.listWidget.clear()

        fields = BitFields(bitText)
        results = fields.results(data)

        for result in results:
            self.listWidget.addItem(QListWidgetItem(str(result)))

    def __init__(self, parent=None):
        super(QDialog, self).__init__()
        self.setupUi()