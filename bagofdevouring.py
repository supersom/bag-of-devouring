import numpy as np

class bagofdevouring(object):
	def __init__(self, values, weight):
		assert len(values)==len(weight)
		self.values = values
		self.weight = weight
		self.num_obj = len(values)
		
	def CalcPSurvive(self,i,n):
		weight = np.r_[self.weight[:i],self.weight[(i+1):(n-1)]]
		print '\nweight: ',weight, len(weight)
		pDevour = [weight[idx]/(sum(weight)+100.0) for idx in range(0,len(weight))]
		pDevour.append(1-sum(pDevour))
		return [(1.0-pDevour[idx]) for idx in range(0,len(pDevour))]
	
	def ExpYield(self,idx,n):
		if n>0:
			print '\nIn ExpYield: idx:',idx,', n: ',n
			ps = self.CalcPSurvive(idx,n-1)
			print 'ps: ',ps
#			one_dev = [ps[idx]*self.ExpYield(idx,n-1) for idx in range(0,len(ps)-1)]
			[self.ExpYield(idx,n-1) for idx in range(0,len(ps)-1)]
			tbr = self.values[idx]+max([ps[idx]*self.ExpYield(idx,n-1) for idx in range(0,len(ps))])
			print 'return: ',tbr
			return tbr 
		else:
			print 'Returning 0, because n = ',n
			return 0.0
		
if __name__ == '__main__':
	bag = bagofdevouring(np.array([100.,200.,300.]), np.array([100.,200.,300.]))
#	print "Best expected yield: \n", max([bag.ExpYield(idx,bag.num_obj) for idx in range(0,bag.num_obj)])
	print "Best expected yield: \n", bag.ExpYield(bag.num_obj-1,bag.num_obj)

