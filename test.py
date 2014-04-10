class Test:
	def __init__(self, testName, version, questions):
		self.testName = testName
		self.version = version 
		self.questions = questions
		
	def __dir__(self):
		return ['testName', 'version']

	def randomizeTest():
		# randomize questions 
		for q in self.questions:
			 #randeomize answers in questions 
			 print (q)
	''' 
		Json Structure 
		{
			TestName: "",
			version: 1.0,
			Questions: [{
				Question: "",
				Answer: "",
				MultipleChoice: ["","","",""]
			}]
		}
	'''
class Question:
	def __init__(self, question, answer, multipleChoice):
		self.question = question
		self.answer = answer
		self.multipleChoice = multipleChoice


class Term:
	def __init__(self, term, definition):
		self.term = term
		self.definition = definition