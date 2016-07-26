import numpy as np

class bagofdevouring(object):
	def __init__(self, values, weight):
		assert len(values)==len(weights)
		self.values = values
		self.weight = weight
		self.num_obj = len(values)
		
	def RemoveObject(self,idx=None):
		if idx is None:
			idx = np.random.randint(0,self.num_obj-1)
		self.values = self.values.delete(idx)
		self.weight = self.weight.delete(idx)
		return idx
	
	def CalcPDevour(self,idx):
		if idx<0 or idx>=len(self.weight):
			print "ERROR> Item isn't in the bag"
			return 0
		else:
			pDevour = self.weight[idx]/(self.weight.sum()+100.0)
	
	def expYield(self, ):
		pass		

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
		
if __name__ == '__main__':
	bag = bagofdevouring(np.array([100,200,300]), np.array([100,200,300]))
	print "Expected yield: ", bag.expectedYield()

