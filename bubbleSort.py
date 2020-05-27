
from algorithm import Algorithm

class BubbleSort(Algorithm):
	def __init__(self):
		super().__init__('O(n^2)', 'O(1)', 'Bubble Sort')

	def sort(self, array):
		# End function if no array is passed
		if not array:
			return None 

		# split array into subarrays that shrink after each iteration
		for sortedI in range(len(array)):
			# move the largest element in the subarray to the end of the subarray
			for index in range(1, len(array)-sortedI):
				# only move element to right if it is larger than next element
				if array[index-1] > array[index]:
					array[index], array[index-1] = array[index-1], array[index]

		return array




