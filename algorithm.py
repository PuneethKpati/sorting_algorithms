
class Algorithm:
	def __init__(self, time, space, name):
		self._name = name
		self._space = space
		self._time  = time
		

	def sort(self, array):
		return array

	def __str__(self):
		res =   '-----------------------------------------------' + '\n'
		res +=  f'{self._name}:' + '\n'
		res += 'Time Complexity: ' + self._time + '\n'
		res += 'Space Complexity: ' + self._space + '\n'
		res +=   '-----------------------------------------------'
		return res
