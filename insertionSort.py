from algorithm import Algorithm 

class InsertionSort(Algorithm): 

	def __init__(self):
		super().__init__('O(n^2)', 'O(1)', 'Insertion Sort')

	def sort(self, array):
		for index in range(len(array)):
			
			for shift in range(index, 0, -1):
				if array[shift] < array[shift-1]:
					array[shift], array[shift-1] = array[shift-1], array[shift]


		return array

