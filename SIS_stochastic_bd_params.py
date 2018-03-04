import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt

# Parameters and Initial Values

#Testing a range of betas and gammas
## Use this to adjust the gammas and betas tested - set it to anything
pstart = 0.0
pstop = 1
pstep = 9

###############################################################################
pi= np.linspace(pstart,pstop, pstep)

# Parameters and Initial Values
beta= 0.1
gamma= 1/20.0
Y0=3 #Naive agents
N0=100.0 #Total population
# X = N - Y is Informed Agents
ND=30 * 24; #Time (a month)
input = Y0

# params related to birth and death

def stochastic_equations(last_Y,ts, p):
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

def stochastic_iteration(input,p):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	naive=[0]
	while T[lop] < ND and input > 0:
		[res,ts] = stochastic_equations(input,ts,p)
		lop=lop+1
		T.append(T[lop-1]+ts)
		naive.append(input)
		lop=lop+1
		T.append(T[lop-1])
		naive.append(res)
		input=res
	return [np.array(naive), np.array(T)]


res_dict={}


for p in pi:
		res_dict[p]=stochastic_iteration(input,p)


plt.close('all')


fig, ax = plt.subplots()
ax.set_title('Susceptible Populations: sensitivity analysis to probability of being captured')


def plot_sense(ax, p,res_dict, x_coor, y_coor):

	#xx = [ (x/24 + x_coor) for x in res_dict[(g,b)][1]]
	xx = [ (x/720 + x_coor) for x in res_dict[p][1]]
	#print(len(xx))
	print(max(xx))
	#yy = [(y/100 + y_coor) for y in res_dict[(g,b)][0]]
	yy = [(y + (y_coor-1)*100) for y in res_dict[p][0]]

	ax.plot(xx,yy)

for x,p in enumerate(pi):
	y=1
	ax.text(x,-15, 'pi: '+ str(p), fontsize = 3)
	plot_sense(ax, p, res_dict, x, y)



plt.show()
