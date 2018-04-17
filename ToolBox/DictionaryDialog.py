from PyQt5.Qt import QGridLayout, QLineEdit, QPushButton, QDialog, QListWidget, QListWidgetItem, QTableWidget, QCompleter, QTableWidgetItem, QLabel, QMessageBox
from Dictionary import Dictionary, Word

class DictionaryDialog(QDialog):
    def setupUi(self):
        self.setWindowTitle('Dictionary')

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.edit = QLineEdit(self)        
        self.edit.textChanged.connect(self.onTextChanged)
        self.edit.returnPressed.connect(self.onReturnPressed)

        searchButton = QPushButton('&Search', self)
        searchButton.clicked.connect(self.onSearchButtonClicked)

        addButton = QPushButton('Add', self)
        addButton.clicked.connect(self.onAddButtonClicked)
        
        header = ('Short', 'Long', "Translate")
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(header)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 200)

        self.edit.setCompleter(QCompleter(self.updateTable(self.dictionary.words)))

       	layout.addWidget(self.edit, 0, 0)
       	layout.addWidget(searchButton, 0, 1)
       	layout.addWidget(addButton, 0, 2)
       	layout.addWidget(self.table, 1, 0, 1, 3)

    def onSearchButtonClicked(self):
    	pass

    def onAddButtonClicked(self):
    	pass

    def onTextChanged(self, arg):
    	self.updateTable(self.dictionary.compare(arg))

    def onReturnPressed(self):
    	if (self.table.rowCount() == 0):
    		if (QMessageBox.question(self, "Add", "Not Found\nAdd new one?") == QMessageBox.Yes):
    			self.createWordDialog(Word('%s,,' % self.edit.text()))

    def createWordDialog(self, word = Word('')):
    	dialog = QDialog(self)
    	layout = QGridLayout(self)

    	dialog.setLayout(layout)
    	shortEdit = QLineEdit(word.short)
    	longEdit  = QLineEdit(word.long)
    	explainEdit = QLineEdit(word.explain)
    	okButton = QPushButton('OK')
    	okButton.clicked.connect(dialog.accept)
    	cancelButton = QPushButton('Cancel')
    	cancelButton.clicked.connect(dialog.reject)

    	layout.addWidget(QLabel('Short'), 0, 0)
    	layout.addWidget(shortEdit, 0, 1)
    	layout.addWidget(QLabel('Long'), 1, 0)
    	layout.addWidget(longEdit, 1, 1)
    	layout.addWidget(QLabel('Translate'), 2, 0)
    	layout.addWidget(explainEdit, 2, 1)
    	layout.addWidget(okButton, 3, 0)
    	layout.addWidget(cancelButton, 3, 1)

    	dialog.exec()
    	if (dialog.result() == QDialog.Accepted):
    		word = Word('%s,%s,%s' % (shortEdit.text(), longEdit.text(), explainEdit.text()))
    		self.dictionary.append(word)
    		self.dictionary.save()
    		self.updateTable(self.dictionary.words)

    def updateTable(self, words):
    	results = []
    	self.table.setRowCount(len(words))
    	i = 0
    	for word in words:
    		self.table.setItem(i, 0, QTableWidgetItem(word.short))
    		self.table.setItem(i, 1, QTableWidgetItem(word.long))
    		self.table.setItem(i, 2, QTableWidgetItem(word.explain))
    		i += 1
    		results.append(word.short)
    	return results
        
    def __init__(self, parent=None):
        super(QDialog, self).__init__()
        self.dictionary = Dictionary()
        self.dictionary.load()
        self.setupUi()