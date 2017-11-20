import matplotlib.pyplot as plt
import numpy as np
import itertools
import csv


for i in range(5):
	t=[]
	e=[]
	spec=[]
	mag=[]
	sus=[]
	abm=[]
	num = str((i+1)*20)

	name = 'parte'+num+'.txt'
	with open(name,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter='\t')
		for row in plots:
			x = row[0]
			t.append(float(x[6:14]))
			e.append(float(x[20:30]))
			spec.append(float(x[35:45]))
			mag.append(float(x[48:60]))
			sus.append(float(x[65:75]))
			abm.append(float(x[81:90]))
	if i == 0:
		plt.plot(t,e,label="L=20")
	if i == 1:
		plt.plot(t,e,'r',label="L=40")
	if i == 2:
		plt.plot(t,e,'g',label="L=60")
	if i == 3:
		plt.plot(t,e,'y',label="L=80")
	if i ==	4:
		plt.plot(t,e,'orange',label="L=100")
plt.title("Expectation Energy as a function of Temperature")
plt.xlabel('Temperature')
plt.ylabel('<E>')
plt.legend()
plt.show()


for i in range(5):
	t=[]
	e=[]
	spec=[]
	mag=[]
	sus=[]
	abm=[]
	num = str((i+1)*20)

	name = 'parte'+num+'.txt'
	with open(name,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter='\t')
		for row in plots:
			x = row[0]
			t.append(float(x[6:14]))
			e.append(float(x[20:30]))
			spec.append(float(x[35:45]))
			mag.append(float(x[48:60]))
			sus.append(float(x[65:75]))
			abm.append(float(x[81:90]))
	if i == 0:
		plt.plot(t,spec,label="L=20")
	if i == 1:
		plt.plot(t,spec,'r',label="L=40")
	if i == 2:
		plt.plot(t,spec,'g',label="L=60")
	if i == 3:
		plt.plot(t,spec,'y',label="L=80")
	if i ==	4:
		plt.plot(t,spec,'orange',label="L=100")
plt.title("Specific Heat as a function of Temperature")
plt.xlabel('Temperature')
plt.ylabel('Specific Heat')
plt.legend()
plt.show()

for i in range(5):
	t=[]
	e=[]
	spec=[]
	mag=[]
	sus=[]
	abm=[]
	num = str((i+1)*20)

	name = 'parte'+num+'.txt'
	with open(name,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter='\t')
		for row in plots:
			x = row[0]
			t.append(float(x[6:14]))
			e.append(float(x[20:30]))
			spec.append(float(x[35:45]))
			mag.append(float(x[48:60]))
			sus.append(float(x[65:75]))
			abm.append(float(x[81:90]))
	if i == 0:
		plt.plot(t,mag,label="L=20")
	if i == 1:
		plt.plot(t,mag,'r',label="L=40")
	if i == 2:
		plt.plot(t,mag,'g',label="L=60")
	if i == 3:
		plt.plot(t,mag,'y',label="L=80")
	if i ==	4:
		plt.plot(t,mag,'orange',label="L=100")
plt.title("Expectation Magnetization as a function of Temperature")
plt.xlabel('Temperature')
plt.ylabel('<M>')
plt.legend()
plt.show()

for i in range(5):
	t=[]
	e=[]
	spec=[]
	mag=[]
	sus=[]
	abm=[]
	num = str((i+1)*20)

	name = 'parte'+num+'.txt'
	with open(name,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter='\t')
		for row in plots:
			x = row[0]
			t.append(float(x[6:14]))
			e.append(float(x[20:30]))
			spec.append(float(x[35:45]))
			mag.append(float(x[48:60]))
			sus.append(float(x[65:75]))
			abm.append(float(x[81:90]))
	if i == 0:
		plt.plot(t,sus,label="L=20")
	if i == 1:
		plt.plot(t,sus,'r',label="L=40")
	if i == 2:
		plt.plot(t,sus,'g',label="L=60")
	if i == 3:
		plt.plot(t,sus,'y',label="L=80")
	if i ==	4:
		plt.plot(t,sus,'orange',label="L=100")
plt.title("Magnetic Susceptibility as a function of Temperature")
plt.xlabel('Temperature')
plt.ylabel('Magnetic Susceptibility')
plt.legend()
plt.show()

for i in range(5):
	t=[]
	e=[]
	spec=[]
	mag=[]
	sus=[]
	abm=[]
	num = str((i+1)*20)

	name = 'parte'+num+'.txt'
	with open(name,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter='\t')
		for row in plots:
			x = row[0]
			t.append(float(x[6:14]))
			e.append(float(x[20:30]))
			spec.append(float(x[35:45]))
			mag.append(float(x[48:60]))
			sus.append(float(x[65:75]))
			abm.append(float(x[81:90]))
	if i == 0:
		plt.plot(t,abm,label="L=20")
	if i == 1:
		plt.plot(t,abm,'r',label="L=40")
	if i == 2:
		plt.plot(t,abm,'g',label="L=60")
	if i == 3:
		plt.plot(t,abm,'y',label="L=80")
	if i ==	4:
		plt.plot(t,abm,'orange',label="L=100")
plt.title("Absolute Magnetization as a function of Temperature")
plt.xlabel('Temperature')
plt.ylabel('<|M|>')
plt.legend()
plt.show()
