import matplotlib.pyplot as plt
import numpy as np
import itertools
import csv

z=[]

for i in range(10):
	name = 'funstuff'+ str(i+1) + '_20_500000.txt'
	with open(name,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter='\t')
		for row in itertools.islice(plots,1,2):
			x = row[0]
			y = x[20:30]
			print(y)
			z.append(float(y))

print(z)	
		

#plt.semilogx(x,y)
#plt.xlabel('MC cycles')
#plt.ylabel('Expectation Energy')
#plt.title('Expectation Energy by MC Cycles!')
#plt.show()
