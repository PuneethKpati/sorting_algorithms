
from algorithm import Algorithm

class BubbleSort(Algorithm):
	def __init__(self):
		super().__init__('O(n^2)', 'O(1)', 'Bubble Sort')

	def sort(self, array):
		for sortedI in range(len(array)):

			for index in range(1, len(array)-sortedI):
				if array[index-1] > array[index]:
					array[index], array[index-1] = array[index-1], array[index]

		return array


array = [1,1,2,4,65,4,23,321,2]
sorter = BubbleSort()
print(sorter)
print(sorter.sort(array))


