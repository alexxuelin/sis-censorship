import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt
# todo: import the file SIS_stochastic.py

# Parameters and Initial Values
beta= 0.1
gamma= 1/20.0
Y0=3 #Naive agents
N0=100.0 #Total population
# X = N - Y is Informed Agents
ND=30 * 24; #Time (a month)
input = Y0

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

## set up to run more instances
# take snapshots on certain days, adjust to have insightful stopping points
stops = [1 * 24, 5 * 24, 10 * 24, 15*24];
# number of simulations (100 -> 3s, 1000 -> 15s)
instances = 100;

# store results (number of infected individuals) in S
S = [[0 for c in range(instances)] for r in range(len(stops))];

for instance in range(0, instances):
	[infected, timestamps]=stochastic_iteration(input)
	#prefill with ND is greater than any possible diff
	diff0 = [[ND for c in range(len(timestamps))] for s in range(len(stops))];
	for r in range(0, len(stops)):
		for c in range(0, len(timestamps)):
			# calculate difference between each event time and the stop time
			d = timestamps[c] - stops[r];
			if d > 0:
	 			diff0[r][c] = d;

	# todo - find index to work more efficiently (not urgent)
	# get S of closest value to T
	for r in range(0, len(stops)):
		min_diff = min(diff0[r]);
		for c in range(0, len(timestamps)):
			# get index of smallest entry in row
			if diff0[r][c] == min_diff:
				# S[row = stops][column = instances]
				S[r][instance] = infected[c];  # todo - check if this was done right, go through loop

print S;

# todo - plot histograms/PDFs (won't take long!)
# print np.histogram(S[0])[0],np.histogram(S[0])[1];
# f2, ((s1, s2), (s3, s4)) = plt.subplots(2, 2, sharex='col', sharey='row');
# s1.plot(set(S[0]),S[0]);
# s1.set_title('1 Day');
# s2.plot(np.histogram(S[1])[0],np.histogram(S[1])[1]);
# s2.set_title('5 Days')
# s3.plot(np.histogram(S[2])[0],np.histogram(S[2])[1]);
# s3.set_title('10 Days')
# s4.plot(np.histogram(S[3])[0],np.histogram(S[3])[1]);
# s4.set_title('15 Days')
# plt.show()
