import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt

# Parameters and Initial Values
beta= 0.1
gamma= 1/20.0
Y0=30 #informed agents
N0=100.0 #Total population
# X = N - Y is informed Agents
ND=30 * 24; #Time (a month)
input = Y0

def stochastic_equations(last_Y,ts):
	Y=last_Y

	access_rate = beta*(N0-Y)*Y/N0
	denial_rate = gamma*Y

    #generate random numbers
	rand1=pl.rand()
	rand2=pl.rand()

    #time until either event occurs
	ts = -np.log(rand2)/(denial_rate+access_rate)
	if rand1 < (access_rate/(denial_rate+access_rate)):
        # access, one more informed agent
		Y += 1;
	else:
        # denial, one fewer informed agent
		Y -= 1;
	return [Y, ts]

# redundancy fixed
def stochastic_iteration(input):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	informed=[input]

	# starts with T[0] and input = Y0 = 30
	while T[lop] < ND and input > 0:

		[res,ts] = stochastic_equations(input,ts)
		T.append(T[lop] + ts)
		informed.append(res)
		input=res
		lop=lop+1

	return [np.array(informed), np.array(T)]

# Visualize 4 simulations
[informed1,t1]=stochastic_iteration(input)
[informed2,t2]=stochastic_iteration(input)
[informed3,t3]=stochastic_iteration(input)
[informed4,t4]=stochastic_iteration(input)

print t1[:8], informed1[:8];

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
