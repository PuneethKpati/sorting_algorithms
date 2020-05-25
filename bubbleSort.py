
class BubbleSort:
	def __init__(self):
		self._name = 'Bubble Sort'
		self._space = 'O(1)'
		self._time  = 'O(n^2)'

	def sort(self, array):
		for sortedI in range(len(array)):

			for index in range(1, len(array)-sortedI):
				if array[index-1] > array[index]:
					array[index], array[index-1] = array[index-1], array[index]

		return array

	def __str__(self):
		res =  f'{self._name}:' + '\n'
		res += 'Time Complexity: ' + self._time + '\n'
		res += 'Space Complexity: ' + self._space

		return res

array = [4,3,2,1]
sorter = BubbleSort()
print(sorter)
print(sorter.sort(array))
