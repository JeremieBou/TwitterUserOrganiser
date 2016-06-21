import json

trained_data_path = "trained_data.json"
test_data_path = "test.json"
def main():
    json_string = "  {  	\"header\": {    		\"classCount\": \"0\",    		\"totalOccurences\": \"0\"    	},    	\"classes\": [{    		\"name\": \"china\",    		\"occurences\": \"3\",    		\"terms\": [{    			\"term\": \"macao\",    			\"count\": \"1\"    		}, {    			\"term\": \"chinese\",   			\"count\": \"5\"    		}, {    			\"term\": \"beijing\",    			\"count\": \"1\"    		}, {    			\"term\": \"shanghai\",    			\"count\": \"1\"    		}]    	}, {    		\"name\": \"japan\",    		\"occurences\": \"1\",    		\"terms\": [{    			\"term\": \"chinese\",    			\"count\": \"1\"    		}, {    			\"term\": \"japan\",    			\"count\": \"1\"    		}, {    			\"term\": \"tokyo\",    			\"count\": \"1\"    		}]    	}]}        "
    
    parsed_json = json.loads(json_string)
    test_json = json.load(open(test_data_path, "r")))
    
    classes = parse_classes(parsed_json["classes"])
   
   
def guess_class(JSONDocument):
	username = JSONDocument["username"]
	message = JSONDocument["message"]
	
	splitMessage = message.split(" ")
	
	for term in splitMessage:

def parse_classes(json_classes):
	classes = {}
	
	 
	for json_class in json_classes:
    	print(json_class)
    	print("\n")
    	
    	data_class = JSONDataClass(json_class) 
    	
	return classes
	
	
def parse_class(json_class):
	name = json_class["name"]
	occurences = json_class["occurence"]
	terms = json_class["terms"]
	
	data_class = DataClass("name")
	
	return data_class
	
	
	

class JSONDataClass:
	classCount = 0
	totalOccurences = 0
	
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
		name = JSONString["name"]
		occurences = JSONString["occurences"]
		terms = JSONString["terms"]
		
		
		self.name = name
		self.occurences = occurences
		parseTerms(terms)
		self.term_count = 0

	def parseTerms(self, JSONterms):
		for term in JSONterms:
			self.terms[term["term"]] = term["count"]
			self.term_count += 1

	def getTerms(self):
		return self.terms

	def getClassProbability(self, message):
		pClass = self.occurences/totalOccurences
		
		
	def getProbabilityWithTerms(self, termArray)
		

	def printSelf(self):
		print("Name: " + self.name+"\n Occurences:" + str(self.occurences) + "\n Terms: " + str(self.terms))

	def __str__(self):
    		return "Name: " + self.name+"\n Occurences:" + str(self.occurences) + "\n Terms: " + str(self.terms)


main()
