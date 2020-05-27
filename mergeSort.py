from algorithm import Algorithm

class MergeSort(Algorithm):

	def __init__(self):
		super().__init__('O(n*Log(n))', 'O(n)', 'Merge Sort')

	def sort(self, array):
		sortedArray = self.sortR(array)
		return sortedArray

	def sortR(self, array):
		if array== None:
			return None


		if len(array)==1 or len(array)==0:
			return array

		leftA = self.sortR(array[:int(len(array)/2)])
		rightA = self.sortR(array[int(len(array)/2):])

		leftLen = len(leftA)
		rightLen= len(rightA)

		res = []
		leftCursor = 0
		rightCursor= 0

		count = 0
		while rightCursor < rightLen and leftCursor < leftLen:
			if leftA[leftCursor] < rightA[rightCursor]:
				res.append(leftA[leftCursor])
				leftCursor += 1
			else:
				res.append(rightA[rightCursor])
				rightCursor += 1

		while rightCursor < rightLen:
			res.append(rightA[rightCursor])
			rightCursor += 1

		while leftCursor < leftLen:
			res.append(leftA[leftCursor])
			leftCursor += 1

		return res
