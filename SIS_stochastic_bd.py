import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt

# Parameters and Initial Values
beta= 0.1
gamma= 1/20.0
Y0=30 # informed agents
N0=100.0 #Total population
# X = N - Y is informed Agents
ND=30 * 24; #Time (a month)
input = Y0

# params related to birth and death
p = 0.05; # probability of an informed agent being arrested


def stochastic_equations(last_N, last_Y,ts):
	Y=last_Y
	N=last_N
	access_rate = beta*(N-Y)*Y/N
	denial_rate = gamma*Y
	death_rate = (p)/(1-p)*access_rate
	birth_rate = 0.1
	# print access_rate,denial_rate,death_rate

    #generate random numbers
	rand1=pl.rand()
	rand2=pl.rand()
	rand3=pl.rand()

    #time until either event occurs
	ts = -np.log(rand2)/(denial_rate+access_rate+birth_rate+death_rate)
	if rand1 < ((access_rate+birth_rate)/(birth_rate+denial_rate+access_rate+death_rate)):
		if (rand3 < access_rate/(birth_rate+access_rate)):
			# access, one more informed agent
			Y += 1
		else:
			# new birth turn up
			N += 1
	else:
        # denial, one fewer informed agent
		Y -= 1
		if(rand3 < death_rate/(death_rate+denial_rate)):
			# denial and jailing
			N-=1

	return [N, Y, ts]

def stochastic_iteration(input):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	informed=[input]
	total=[N0]
	tot=N0

	# starts with T[0] and input = Y0 = 30
	while T[lop] < ND and input > 0:

		[tot,res,ts] = stochastic_equations(tot,input,ts)
		T.append(T[lop] + ts)
		informed.append(res)
		total.append(tot)
		input=res
		lop=lop+1

	return [np.array(total), np.array(informed), np.array(T)]

# Visualize 4 simulations
[total1,informed1,t1]=stochastic_iteration(input)
[total2,informed2,t2]=stochastic_iteration(input)
[total3,informed3,t3]=stochastic_iteration(input)
[total4,informed4,t4]=stochastic_iteration(input)


f1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row');
ax1.plot(t1/24., informed1);
ax1.set_title('Simulation 1');
ax2.plot(t2/24., informed2);
ax2.set_title('Simulation 2');
ax3.plot(t3/24., informed3);
ax3.set_title('Simulation 3');
ax4.plot(t4/24., informed4);
ax4.set_title('Simulation 4');
plt.show();

f1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row');
ax1.plot(t1/24., total1);
ax1.set_title('Simulation 1');
ax2.plot(t2/24., total2);
ax2.set_title('Simulation 2');
ax3.plot(t3/24., total3);
ax3.set_title('Simulation 3');
ax4.plot(t4/24., total4);
ax4.set_title('Simulation 4');
plt.show();
