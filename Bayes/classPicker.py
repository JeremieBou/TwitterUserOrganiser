import json

trained_data_path = "trained_data.json"

def main():
    json_string = "  {  	\"header\": {    		\"classCount\": \"0\",    		\"totalOccurences\": \"0\"    	},    	\"classes\": [{    		\"name\": \"china\",    		\"occurences\": \"3\",    		\"terms\": [{    			\"term\": \"macao\",    			\"count\": \"1\"    		}, {    			\"term\": \"chinese\",   			\"count\": \"5\"    		}, {    			\"term\": \"beijing\",    			\"count\": \"1\"    		}, {    			\"term\": \"shanghai\",    			\"count\": \"1\"    		}]    	}, {    		\"name\": \"japan\",    		\"occurences\": \"1\",    		\"terms\": [{    			\"term\": \"chinese\",    			\"count\": \"1\"    		}, {    			\"term\": \"japan\",    			\"count\": \"1\"    		}, {    			\"term\": \"tokyo\",    			\"count\": \"1\"    		}]    	}]}        "
    print("hello")
    parsed_json = json.loads(json_string)

    print(parsed_json["header"])


class DataClass:
	classCount = 0
	totalOccurences = 0

    @staticmethod
    def the_static_method(x):
        print x


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
