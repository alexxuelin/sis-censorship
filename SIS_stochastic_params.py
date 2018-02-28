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

    #transmission rate = beta * XY/N
	transmit_rate = b*(N0-Y)*Y/N0
    #recovery rate = gamma * Y
	recover_rate = g*Y

    #generate random numbers
	rand1=pl.rand()
	rand2=pl.rand()

    #time until either event occurs
	ts = -np.log(rand2)/(transmit_rate+recover_rate)
	if rand1 < (transmit_rate/(transmit_rate+recover_rate)):
        # infection
		Y += 1;
	else:
        # recovery
		Y -= 1;
	return [Y, ts]

def stochastic_iteration(input, g, b):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	infected=[0]
	while T[lop] < ND and input > 0:
		[res,ts] = stochastic_equations(input,ts,g,b)
		lop=lop+1
		T.append(T[lop-1]+ts)
		infected.append(input)
		lop=lop+1
		T.append(T[lop-1])
		infected.append(res)
		input=res
	return [np.array(infected), np.array(T)]




res_dict={}


for g in gamma:
	for b in beta:
		res_dict[(g,b)]=stochastic_iteration(input,g,b)


fig, ax = plt.subplots( 9, 9, sharex='col', sharey='row');

counter1=0
for b in beta:
	counter2 =0
	for g in gamma:

		ax[counter1,counter2].plot(res_dict[(g,b)][1]/24., res_dict[(g,b)][0]);
		#ax[counter1,counter2].set_title('Gamma: '+ str(g)+'Beta: '+str(b), size = 2);
		#ax[counter1,counter2].set_axis_off
		ax[counter1,counter2].grid

		counter2+=1


	counter1+=1
	counter2=0
plt.show()
