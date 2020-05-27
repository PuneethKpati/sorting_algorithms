from algorithm import Algorithm 

class InsertionSort(Algorithm): 

	def __init__(self):
		super().__init__('O(n^2)', 'O(1)', 'Insertion Sort')

	def sort(self, array):
		# End function if no array is passed
		if not array:
			return None 

		# only consider first 'index' number of elements and sort them	
		for index in range(len(array)):
			# within the first 'index' elements sort the array
			# by inserting the last element from subarray into appropriate place within. 
			for shift in range(index, 0, -1):
				if array[shift] < array[shift-1]:
					array[shift], array[shift-1] = array[shift-1], array[shift]


		return array

