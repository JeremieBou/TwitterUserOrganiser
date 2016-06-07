import json

data_path = 'training.json'


def main():
	data = parse_data(open(data_path, "r"))
	classes = count_terms(data)
		
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
		try:
			classes[class_name].addOccurence
		except:
			classes[class_name] = DataClass(class_name)

		split_message = class_message.split(" ")

		for word in split_message:
			classes[class_name].addTerm(word)
	return classes
	

class DataClass:
	classCount = 0
	
	def __init__(self, name):
		self.name = name
		self.occurences = 0
		self.terms = {}
		self.term_count = 0

	def addOccurence(self):
		self.occurences += 1

	def addTerm(self, term):
		try:
			self.terms[term] += 1
		except:
			self.terms[term] = 1

		self.term_count += 1
	
	def __str__(self):
     		return "" + self.name+"\n" + str(self.occurences) + "\n" + str(self.terms)

main()
