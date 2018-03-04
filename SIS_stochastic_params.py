import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt

# Parameters and Initial Values

#Testing a range of betas and gammas
## Use this to adjust the gammas and betas tested - set it to anything
bstart = .1
bstop = 1
bstep = 9

gstart = .1
gstop = 1
gstep = 9

###############################################################################
beta= np.linspace(bstart,bstop, bstep) #The total number of people that gain access to the
#site per day
gamma= np.linspace(gstart,gstop,gstep)#The total length of the denial issued by the government
Y0=3 #Naive agents
N0=100.0 #Total population
# X = N - Y is Informed Agents
ND=30 * 24; #Time (a month)
input = Y0

def stochastic_equations(last_Y,ts, g, b):
	Y=last_Y

	denial_rate = b*(N0-Y)*Y/N0
	access_rate = g*Y

    #generate random numbers
	rand1=pl.rand()
	rand2=pl.rand()

    #time until either event occurs
	ts = -np.log(rand2)/(denial_rate+access_rate)
	if rand1 < (denial_rate/(denial_rate+access_rate)):

		Y += 1;
	else:

		Y -= 1;
	return [Y, ts]

def stochastic_iteration(input, g, b):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	naive=[0]
	while T[lop] < ND and input > 0:
		[res,ts] = stochastic_equations(input,ts,g,b)
		lop=lop+1
		T.append(T[lop-1]+ts)
		naive.append(input)
		lop=lop+1
		T.append(T[lop-1])
		naive.append(res)
		input=res
	return [np.array(naive), np.array(T)]




res_dict={}


for g in gamma:
	for b in beta:
		res_dict[(g,b)]=stochastic_iteration(input,g,b)


plt.close('all')

#fig, ax = plt.subplots( 9, 9, sharex='col', sharey='row');

fig, ax = plt.subplots()
ax.set_title('Susceptible Populations: sensitivity analysis on Beta and Gamma')

#plt.axis('off')


def plot_sense(ax, g, b, res_dict, x_coor, y_coor):

	#xx = [ (x/24 + x_coor) for x in res_dict[(g,b)][1]]
	xx = [ (x/720 + x_coor) for x in res_dict[(g,b)][1]]
	#print(len(xx))
	print(max(xx))
	#yy = [(y/100 + y_coor) for y in res_dict[(g,b)][0]]
	yy = [(y + (y_coor-1)*100) for y in res_dict[(g,b)][0]]

	ax.plot(xx,yy)

for x,g in enumerate(gamma):
	for y,b in enumerate(beta):
		#ax.text(x*24, y*100, 'Gamma: '+ str(g)+'Beta: '+str(b), fontsize = 3)
		ax.text(x,-120, 'Gamma: '+ str(g), fontsize = 3)
		ax.text(-1,(y*100)-120, 'Beta: '+ str(b), fontsize = 3)
		plot_sense(ax, g, b, res_dict, x, y)



plt.show()
