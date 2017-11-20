import matplotlib.pyplot as plt
import numpy as np
import itertools
import csv

x=[]

with open('partd2.4_20_1100000.txt','r') as csvfile:
	plots = csv.reader(csvfile)
	for row in itertools.islice(plots,2,100001):
		x.append(float(row[0])*400.)

plt.hist(x,bins=100,normed='True',color='goldenrod')
plt.title("Histogram of Energies")
plt.xlabel("Energy of the System")
plt.ylabel("Percentage")
plt.show()
