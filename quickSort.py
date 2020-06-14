from algorithm import Algorithm 

class QuickSort(Algorithm): 

	def __init__(self):
		super().__init__('O(n^2)', 'O(n)', 'Quick Sort')

	# recursive function that divides array and fixes pivot spot
	def sort(self, array):
		# Edge case handling
		if not array:
			return None
		if len(array) in [1, 0]:
			return array

		# Quick Sort algorithm begins
		# select the pivot and end points of the array to be sorted
		pivot = array[0]
		i = 1
		j = len(array)-1

		# these will be used as flags to signify when two elements can be swapped
		jFound = False
		iFound = False

		# loop till we've seen all elements
		while j >= i:
			# move i up if the element is in the right segment
			# else, wait for j to swap with the curr element 
			if array[i] < pivot:
				i += 1
			else:
				iFound = True

			# same as the i movement but instead down 
			if array[j] > pivot:
				j -= 1
			else:
				jFound = True

			# if we found two misplaced elements then swap them around and continue with the problem
			if iFound and jFound:
				array[i], array[j] = array[j], array[i]
				i += 1
				j -= 1
				# reset flags
				jFound, iFound = False, False

		# move pivot to its final fixed spot in the array
		array[0], array[j] = array[j], array[0]

		# now we split the array divided by the pivot in its fixed spot
		fixed = j
		# apply recursive function to each segment to sort them around our pivot
		array[:fixed] = self.sort(array[:fixed])
		array[fixed+1:] = self.sort(array[fixed+1:])
		
		return array
		


		