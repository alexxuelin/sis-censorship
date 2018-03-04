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
p = 0.05; # probability of an informed agent being arrested

def stochastic_equations(last_Y,ts):
	Y=last_Y
	denial_rate = beta*(N0-Y)*Y/(N0 * (1-p))
	access_rate = gamma*Y

    #generate random numbers
	rand1=pl.rand()
	rand2=pl.rand()

    #time until either event occurs
	ts = -np.log(rand2)/(denial_rate+access_rate)
	if rand1 < (denial_rate/(denial_rate+access_rate)):
        # denial, one more naive agent
		Y += 1;
	else:
        # access, one fewer naive agent
		Y -= 1;
	return [Y, ts]

def stochastic_iteration(input):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	naive=[0]
	while T[lop] < ND and input > 0:
		[res,ts] = stochastic_equations(input,ts)
		lop=lop+1
		T.append(T[lop-1]+ts)
		naive.append(input)
		lop=lop+1
		T.append(T[lop-1])
		naive.append(res)
		input=res
	return [np.array(naive), np.array(T)]

# Visualize 4 simulations
[naive1,t1]=stochastic_iteration(input)
[naive2,t2]=stochastic_iteration(input)
[naive3,t3]=stochastic_iteration(input)
[naive4,t4]=stochastic_iteration(input)


f1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row');
ax1.plot(t1/24., naive1);
ax1.set_title('Simulation 1');
ax2.plot(t2/24., naive2);
ax2.set_title('Simulation 2');
ax3.plot(t3/24., naive3);
ax3.set_title('Simulation 3');
ax4.plot(t4/24., naive4);
ax4.set_title('Simulation 4');
plt.show();
