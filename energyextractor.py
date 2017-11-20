import matplotlib.pyplot as plt
import numpy as np
import itertools
import csv

z=[]

for i in range(500):
	name = 'partd'+ str(i+1) + '.txt'
	with open(name,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter='\t')
		for row in plots:
			x = row[0]
			y = x[20:30]
			print(y)
			z.append(float(y))

print(z)

thefile = open('expectationenergies.txt','w')

for item in z:
	thefile.write("%s\n" % item)
		

plt.hist(z,bins=100)
plt.title("Histogram of Energies")
plt.xlabel("Expectation Energy")
plt.ylabel("Count")
plt.show()
