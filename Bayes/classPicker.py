import json

trained_data_path = "trained_data.json"
test_data_path = "test.json"
def main():
    json_string = "  {  	\"header\": {    		\"classCount\": \"0\",    		\"totalOccurences\": \"0\"    	},    	\"classes\": [{    		\"name\": \"china\",    		\"occurences\": \"3\",    		\"terms\": [{    			\"term\": \"macao\",    			\"count\": \"1\"    		}, {    			\"term\": \"chinese\",   			\"count\": \"5\"    		}, {    			\"term\": \"beijing\",    			\"count\": \"1\"    		}, {    			\"term\": \"shanghai\",    			\"count\": \"1\"    		}]    	}, {    		\"name\": \"japan\",    		\"occurences\": \"1\",    		\"terms\": [{    			\"term\": \"chinese\",    			\"count\": \"1\"    		}, {    			\"term\": \"japan\",    			\"count\": \"1\"    		}, {    			\"term\": \"tokyo\",    			\"count\": \"1\"    		}]    	}]}        "
    
    parsed_json = json.loads(json_string)
    test_json = json.load(open(test_data_path, "r"))
    
    classes = parse_classes(parsed_json["classes"])
    guess_class(classes, test_json["message"])
   
def guess_class(classes, message):
	print("guessing class:")
	mostProbabable = classes[0]
	for data_class in classes:
		print(data_class)
		class_prob = data_class.getClassProbability(message)
		print("class probability for " + data_class.name + " : ")
		print(class_prob)
		
		if class_prob > mostProbabable.getClassProbability(message):
			mostProbabable = data_class
	print("\"" + message + "\" is probability in")
	print(mostProbabable.name)

def parse_classes(json_classes):
	classes = []
	
	print(json_classes[1])  
	print("\n")
	 
	for json_class in json_classes:
		data_class = JSONDataClass(json_class) 
		classes.append(data_class)
		
	print("classes parsed, Lenght: ")
	print(len(classes))
    
	return classes
	
	
def parse_class(json_class):
	name = json_class["name"]
	occurences = json_class["occurence"]
	terms = json_class["terms"]
	
	data_class = JSONDataClass("name")
	return data_class
		
	
	

class JSONDataClass:
	classCount = 0
	totalOccurences = 0
	vocabulary = {}
	vocabularySize = 0
	
	@staticmethod
	def the_static_method(x):
		print x
		
		
	@staticmethod
	def setClassCount(count):
		classCount = count
		
	@staticmethod
	def setTotalOccurences(total):
		totalOccurences = total


	def __init__(self, JSONString):
		JSONTerms = JSONString["terms"]
		
		self.name = JSONString["name"]
		self.occurences = int(JSONString["occurences"])
		self.terms = self.parseTerms(JSONTerms)
		self.term_count = len(self.terms)
		
		JSONDataClass.classCount += 1

	def parseTerms(self, JSONterms):
		terms = {}
		for term in JSONterms:
			inTerm = term["term"]
			
			terms[inTerm] = int(term["count"])
			
			print(term["term"])
			
			if inTerm not in JSONDataClass.vocabulary:
				JSONDataClass.vocabulary[inTerm] = term["count"]
				JSONDataClass.vocabularySize += 1
				print("Adding term: " + term["term"])
			else:
				JSONDataClass.vocabulary[inTerm] += term["count"]
				
		print("\nvocabulary size: ")
		print(JSONDataClass.vocabularySize)
				
		return terms
		
	def getTerms(self):
		return self.terms

	def getClassProbability(self, message):
		pClass = float(self.occurences)/float(JSONDataClass.classCount)
		splitMessage = message.split(" ")
		for term in splitMessage:
			termProb = self.getTermProbability(term)
			
			pClass = pClass * self.getTermProbability(term)
		
		return pClass
		
	def getTermProbability(self, term):
		if term in self.terms:
			return (float(self.terms[term]) + 1)/(float(self.occurences) + float(JSONDataClass.vocabularySize))
		else:
			return (1)/float((self.occurences + JSONDataClass.vocabularySize))
	
	def printSelf(self):
		print("Name: " + self.name+"\n Occurences:" + str(self.occurences) + "\n Terms: " + str(self.terms))

	def __str__(self):
    		return "Name: " + self.name+"\n Occurences:" + str(self.occurences) + "\n Terms: " + str(self.terms)


main()
