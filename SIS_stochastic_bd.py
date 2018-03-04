import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt

# Parameters and Initial Values
beta= 0.1
gamma= 1/20.0
Y0=3 #Naive agents
N0=100.0 #Total population
# X = N - Y is Informed Agents
ND=30 * 24; #Time (a month)
input = Y0

# params related to birth and death
v = 1;  
p =

def stochastic_equations(last_Y,ts):
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
		[res,ts] = stochastic_equations(input,ts)
		lop=lop+1
		T.append(T[lop-1]+ts)
		infected.append(input)
		lop=lop+1
		T.append(T[lop-1])
		infected.append(res)
		input=res
	return [np.array(infected), np.array(T)]

# Visualize 4 simulations
[infected1,t1]=stochastic_iteration(input)
[infected2,t2]=stochastic_iteration(input)
[infected3,t3]=stochastic_iteration(input)
[infected4,t4]=stochastic_iteration(input)

f1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row');
ax1.plot(t1/24., infected1);
ax1.set_title('Simulation 1');
ax2.plot(t2/24., infected2);
ax2.set_title('Simulation 2');
ax3.plot(t3/24., infected3);
ax3.set_title('Simulation 3');
ax4.plot(t4/24., infected4);
ax4.set_title('Simulation 4');
plt.show();
