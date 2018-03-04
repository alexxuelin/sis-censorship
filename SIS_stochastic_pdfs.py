import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt
# todo: import the file SIS_stochastic.py

# Parameters and Initial Values
beta= 0.1
gamma= 1/20.0
Y0=30 #informed agents
N0=100.0 #Total population
# X = N - Y is naive Agents
ND=30 * 24; #Time (a month)
input = Y0

def stochastic_equations(last_Y,ts):
	Y=last_Y

	access_rate  = beta*(N0-Y)*Y/N0
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

# def stochastic_iteration(input):
# 	lop=0
# 	ts=0
#     # Initialize as lists
# 	T=[0]
# 	naive=[0]
# 	while T[lop] < ND and input > 0:
# 		[res,ts] = stochastic_equations(input,ts)
# 		lop=lop+1
# 		T.append(T[lop-1]+ts)
# 		naive.append(input)
# 		lop=lop+1
# 		T.append(T[lop-1])
# 		naive.append(res)
# 		input=res
# 	return [np.array(naive), np.array(T)]

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

## set up to run more instances
# take snapshots on certain days, adjust to have insightful stopping points
stops = [1 * 24, 5 * 24, 10 * 24, 25*24];
# number of simulations (100 -> 3s, 1000 -> 15s)
instances = 100;

# store results (number of naive individuals) in S
S = [[0 for c in range(instances)] for r in range(len(stops))];

for instance in range(0, instances):
	[naive, timestamps]=stochastic_iteration(input)
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
				S[r][instance] = naive[c];  # todo - check if this was done right, go through loop

print S;



# plot 4 snapshots
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row');
ax1.hist(S[0], bins = 10, alpha=0.75);
ax1.set_title('1 Day');

ax2.hist(S[1], bins = 20, alpha=0.75);
ax2.set_title('5 Days');

ax3.hist(S[2], bins = 20, alpha=0.75);
ax3.set_title('10 Days');

ax4.hist(S[3], bins = 20, alpha=0.75);
ax4.set_title('25 Days');

fig = plt.gcf();
plt.show();
