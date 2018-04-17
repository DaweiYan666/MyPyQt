import sys

class Word:
	def __init__(self, line):
		words = line.split(',')
		self.short   = ''
		self.long    = ''
		self.explain = ''
		if (len(words) > 0):
			self.short = words[0]
		if (len(words) > 1):
			self.long = words[1]
		if (len(words) > 2):
			self.explain = words[2]

		# print(self.toString())

	def toString(self):
		return '%s,%s,%s' % (self.short, self.long, self.explain)

defaultPath = 'C:\\Users\\ezyanda\\OneDrive - Ericsson AB\\Attachments\\dict.csv'

class Dictionary:
	def __init__(self):
		self.words = []

	def load(self, filePath = defaultPath):
		f = open(filePath, 'r')
		while (True):
			line = f.readline()
			if (len(line) == 0):
				break;
			self.words.append(Word(line))
		f.close()

	def save(self, filePath = defaultPath):
		f = open(filePath, 'w')
		for word in self.words:
			f.write(word.toString())
		f.close()

	def append(self, word):
		self.words.append(word)

	def compare(self, short):
		results = []
		short = short.upper()
		for word in self.words:
			if (word.short.startswith(short)):
				results.append(word)
		return results