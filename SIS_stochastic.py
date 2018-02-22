# SIS model without birth or death
# stochastic, using poisson event time interval
# 6.3.1.1


import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

beta=0.03
gamma=1/100.0

Y0=20.0 #Infected
N0=1000.0 #Total
# X = N - Y is Susceptibles
ND=10*365.0; #Time

input = Y0

def stoc_eqs(last_Y,ts):
	Y=last_Y

    #transmission rate = beta * XY/N
	transmit_rate = beta*(N0-Y)*Y/N0
    #recovery rate = gamma * Y
	recover_rate = gamma*Y

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

def stochastic_iteration(input):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	infected=[0]
	while T[lop] < ND and input > 0:
		[res,ts] = stoc_eqs(input,ts)
		lop=lop+1
		T.append(T[lop-1]+ts)
		infected.append(input)
		lop=lop+1
		T.append(T[lop-1])
		infected.append(res)
		input=res
	return [np.array(infected), np.array(T)]

[infected1,t1]=stochastic_iteration(input)
[infected2,t2]=stochastic_iteration(input)
[infected3,t3]=stochastic_iteration(input)
[infected4,t4]=stochastic_iteration(input)

# print len(infected), len(t)
# issue : each realization creates a different number of events, how to plot all?
# # loop over realizations
# row, col= 4, 1;
# times = [[0 for r in range(row)] for c in range(col)]
# Y_results = [[0 for r in range(row)] for c in range(col)]
#
# for i in range(0,row):
#     [infected, t] = stochastic_iteration(input)
#     results[:, i] =
#     t=np.array(t)
#     infected=np.array(infected)


# ### plot
# pl.plot(t/365., infected, 'r')
# pl.show()

# visualize several runs
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
ax1.plot(t1/365., infected1)
ax1.set_title('Simulation 1')
ax2.plot(t2/365., infected2)
ax1.set_title('Simulation 2')
ax3.plot(t3/365., infected3)
ax1.set_title('Simulation 3')
ax4.plot(t4/365., infected4)
ax1.set_title('Simulation 4')
plt.show()
