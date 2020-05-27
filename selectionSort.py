from algorithm import Algorithm 

class SelectionSort(Algorithm): 

	def __init__(self):
		super().__init__('O(n^2)', 'O(1)', 'Selection Sort')

	def sort(self, array):
		# Traverse the subarray with unsorted elements
		for sortDone in range(len(array)):
			# find the max element in subarray
			maxIndex = 0
			for index in range(len(array)-sortDone):
				if array[index] > array[maxIndex]:
					maxIndex = index

			# swap the biggest element in subarray with
			# last element in the subarray
			array[len(array)-sortDone], array[maxIndex] =  array[maxIndex], array[len(array)-sortDone]

		return array

