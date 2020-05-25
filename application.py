
class Application(Object):

	def __init__(self):
		self._algorithm = Algorithm()
		self._array = []
		self._sorted = []

	def run(self):
		self.printAlgorithmInstructions()
		algorithmSelect = input()
		self._algorithm = Algorithm(algorithmSelect)

		self.printArrayInstructions()
		inputArray = input()
			
		self.sort()



	def printAlgorithmInstructions(self):
		print('Pick a sorting Algorithm:')
		print('[1] : Insertion Sort')

	def printArrayInstructions():
		print('Enter Array: ')
		print('[Example Format]:\n1,2,3,45,200')

	def algorithm(self):
		return self._algorithm

	def setAlgorithm(self, algorithm): 
		self._algorithm = algorithm
		 
	def array(self):
		return self._array

	def setArray(self, array):
		if array == None:
			return 
		self._array = array

runAlgorithms = Application()
runAlgorithms.run()