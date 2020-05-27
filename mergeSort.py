from algorithm import Algorithm

class MergeSort(Algorithm):

	def __init__(self):
		super().__init__('O(n*Log(n))', 'O(n)', 'Merge Sort')

	def sort(self, array):
		# apply the merge sort recursive function
		sortedArray = self.sortR(array)
		return sortedArray

	def sortR(self, array):
		# End function if no array is passed
		if not array:
			return None 

		# if there is only one digit in the list then 
		# no need to call mergeSort again, return the element
		if len(array)==1:
			return array

		# split the array into two halves and apply mergeSort again
		# left and right array should not have overlapping elements 
		leftA = self.sortR(array[:int(len(array)/2)])
		rightA = self.sortR(array[int(len(array)/2):])

		leftLen = len(leftA)
		rightLen= len(rightA)

		res = []
		leftCursor = 0
		rightCursor= 0

		# combining the elements in the left and right arrays
		# elements are added from the two arrays in the sorted order
		count = 0
		while rightCursor < rightLen and leftCursor < leftLen:
			if leftA[leftCursor] < rightA[rightCursor]:
				res.append(leftA[leftCursor])
				leftCursor += 1
			else:
				res.append(rightA[rightCursor])
				rightCursor += 1

		# if right array is longer or has elements remaining while left array is empty 
		# then add the rest of right array to result
		while rightCursor < rightLen:
			res.append(rightA[rightCursor])
			rightCursor += 1

		# if left array is longer or has elements remaining while right array is empty 
		# then add the rest of left array to result
		while leftCursor < leftLen:
			res.append(leftA[leftCursor])
			leftCursor += 1

		# return the sorted subarray
		return res

sort = MergeSort()
print(sort.sort([2,34,23,1,2,3,4,566,78,34]))
