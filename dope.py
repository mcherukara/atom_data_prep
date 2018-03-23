import numpy as np
import random

#Calculate sum of weights, generate random number. See which slice it falls into
def weighted_choice(weights):
  weights=np.asarray(weights)
  wtsum=np.sum(weights) #Sum weights in case not 1
  lend=weights.shape[0]
  cumsum=np.zeros(lend,float)
  cum=0
  
  for i in range(lend): #Make array of cumulative sums
    cum+=weights[i]
    cumsum[i]=cum
  rnd=random.random()*wtsum
  
  for i, wt in enumerate(np.nditer(cumsum)): #Find which slice it falls in
    if rnd< wt: return i+1

data=np.loadtxt('coats.dump', skiprows=9)
ofile=open('co10al10ni.ats', 'w')
dims=data.shape
print "Read file"

ntypes=np.zeros(3, int)
for i in range(dims[0]):
  typ=weighted_choice([0.8,0.1,0.1])
  ntypes[typ-1]+=1
  ofile.write('%d %d %.4f %.4f %.4f\n' %(data[i,0], typ, data[i,2], data[i,3], data[i,4]))

ofile.close()
print ntypes
print "Fractions:", ntypes/float(ntypes.sum())
