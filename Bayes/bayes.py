import json

data_path = 'training.json'


def main():
	data = parse_data(open(data_path, "r"))
	classes = count_terms(data)
	for c in classes:
		print(classes[c])



def parse_data(data_file):
	data = []
	for line in data_file:
		try:
			entry = json.loads(line)
			data.append(entry)
		except:
			continue


	return data

def count_terms(data):
	classes = {}

	for entry in data:
		class_name = entry['class']
		class_message = entry['message']

		if class_name not in classes:
			classes[class_name] = DataClass(class_name)

		classes[class_name].addOccurence()


		split_message = class_message.split(" ")

		for word in split_message:
			classes[class_name].addTerm(word)

	return classes


class DataClass:
	classCount = 0
	totalOccurences = 0

	def __init__(self, name):
		self.name = name
		self.occurences = 0
		self.terms = {}
		self.term_count = 0
		DataClass.classCount += 1

	def addOccurence(self):
		self.occurences += 1
		DataClass.totalOccurences += 1

	def addTerm(self, term):
		try:
			self.terms[term] += 1
		except:
			self.terms[term] = 1

		self.term_count += 1

	def getTerms():
		return self.terms

	def printSelf():
		print("Name: " + self.name+"\n Occurences:" + str(self.occurences) + "\n Terms: " + str(self.terms))

	def __str__(self):
     		return "Name: " + self.name+"\n Occurences:" + str(self.occurences) + "\n Terms: " + str(self.terms)

main()
