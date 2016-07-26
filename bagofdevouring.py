import numpy as np

class bagofdevouring(object):
	def __init__(self, values, weight):
		self.values = values
		self.weight = weight
	def expectedYield(self):
		expectedweight = float(0)
		for i in range(0, len(self.values)):
			if i == 0:
				expectedweight = expectedweight + self.values[np.argmax(self.values)]
				self.values = np.delete(self.values, np.argmax(self.values))
			else:
				print self.values
				expectedweight = expectedweight + (self.values[np.argmax(self.values)] * float(self.values[np.argmax(self.values)]) / (np.sum(self.values) + 100))
				self.values = np.delete(self.values, np.argmax(self.values))
		print expectedweight
bag = bagofdevouring(np.array([100,200,300]), np.array([100,200,300]))
bag.expectedYield()

