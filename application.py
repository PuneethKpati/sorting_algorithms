from algorithm import Algorithm 
from insertionSort import InsertionSort
from selectionSort import SelectionSort
from bubbleSort import BubbleSort
from mergeSort import MergeSort


class Application:

	def __init__(self):
		self._algorithm = None
		self._array = []
		self._sorted = []
		self._algos = {
		'1':InsertionSort(),
		'2':SelectionSort(),
		'3':BubbleSort(),
		'4':MergeSort(),
		'5':'QuickSort',
		}

	def run(self):
		while True:
			self.printAlgorithmInstructions()
			algoNum = input()
			self._algorithm = self._algos[algoNum]

			self.printSelected()
			

			self.printArrayInstructions()
			self._array = self.strToArr(input())

			self._sorted = self.sort(self._array)
			print('sorted: ', self._sorted)

	def sort(self, array):
		return self._algorithm.sort(array)


	def strToArr(self, inputStr):
		res = []
		digits = inputStr.split(',')
		for digit in digits:
			res.append(int(digit))

		return res


	def printAlgorithmInstructions(self):
		print('\nPick a sorting Algorithm & Enter the num:')
		print('[1] : Insertion Sort')
		print('[2] : Selection Sort')
		print('[3] : Bubble Sort')
		print('[4] : Merge Sort')
		print('[5] : Quick Sort')
		print('\nEnter Number: ', end='')

	def printSelected(self):
		print(f'{self._algorithm}\n')

	def printArrayInstructions(self):
		print('Enter Array (elements separated by commas): ')
		print('[Example Format]:1,2,3,45,200\n')
		print('Enter Array: ', end='')

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