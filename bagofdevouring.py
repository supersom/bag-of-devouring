import numpy as np

class bagofdevouring(object):
	def __init__(self, values, weight):
		assert len(values)==len(weight)
		self.values = values
		self.weight = weight
		self.num_obj = len(values)
		
#	def RemoveObject(self,idx=None):
#		if idx is None:
#			idx = np.random.randint(0,self.num_obj-1)
#		self.values = self.values.delete(idx)
#		self.weight = self.weight.delete(idx)
#		return idx
	
	def CalcPSurvive(self,i,n):
		if n==self.num_obj:
			return [1.0 for idx in range(0,n)]
		else:
			weight = np.r_[self.weight[:i],self.weight[(i+1):(n-1)]]
			print '\nweight: ',weight, len(weight)
			pDevour = [weight[idx]/(sum(weight)+100.0) for idx in range(0,len(weight))]
			pDevour.append(sum(pDevour))
			print 'pDevour: ',pDevour
			return [(1.0-pDevour[idx]) for idx in range(0,len(pDevour))]
	
	def ExpYield(self,idx,n):
		if n>0:
			ps = self.CalcPSurvive(idx,n-1)
			print 'ps: ',ps
			one_dev = [ps[idx]*self.ExpYield(idx,n-1) for idx in range(0,len(ps)-1)]
			none_dev = ps[-1]*self.ExpYield(n-2,n-1)
			one_dev.append(none_dev)
			print 'one_dev: ',one_dev
			tbr = self.values[idx]+max(one_dev)
			print 'return: ',tbr
			return tbr 
		else:
			return 0.0

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
	bag = bagofdevouring(np.array([100.,200.,300.]), np.array([100.,200.,300.]))
#	print "Best expected yield: \n", max([bag.ExpYield(idx,bag.num_obj) for idx in range(0,bag.num_obj)])
	print "Best expected yield: \n", bag.ExpYield(bag.num_obj-1,bag.num_obj)

