import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt

# Parameters and Initial Values

#Testing a range of betas and gammas
## Use this to adjust the gammas and betas tested - set it to anything
pstart = 0.0
pstop = 0.4
pstep = 9

bstart = 0.0
bstop = 0.4
bstep = 9

###############################################################################
pi= np.linspace(pstart,pstop, pstep)
bi= np.linspace(bstart,bstop, bstep)

# Parameters and Initial Values
beta= 0.1
gamma= 1/20.0
Y0=3 #Naive agents
N0=100.0 #Total population
# X = N - Y is Informed Agents
ND=30 * 24; #Time (a month)
input = Y0

# params related to birth and death

def stochastic_equations(last_N, last_Y,ts,p,b):
	Y=last_Y
	N=last_N
	access_rate = beta*(N-Y)*Y/N
	denial_rate = gamma*Y
	death_rate = (p)/(1-p)*access_rate
	birth_rate = b
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

def stochastic_iteration(input,p,b):
	lop=0
	ts=0
    # Initialize as lists
	T=[0]
	informed=[input]
	total=[N0]
	tot=N0

	# starts with T[0] and input = Y0 = 30
	while T[lop] < ND and input > 0:

		[tot,res,ts] = stochastic_equations(tot,input,ts,p,b)
		T.append(T[lop] + ts)
		informed.append(res)
		total.append(tot)
		input=res
		lop=lop+1

	return [np.array(total), np.array(informed), np.array(T)]


res_dict={}


for p in pi:
	for b in bi:
		res_dict[(p,b)]=stochastic_iteration(input,p,b)


plt.close('all')


fig, ax = plt.subplots()
ax.set_title('Informed Populations: sensitivity analysis on v and p')
plt.axis('off')

def plot_sense(ax, p,b, res_dict, x_coor, y_coor):

	#xx = [ (x/24 + x_coor) for x in res_dict[(g,b)][1]]
	xx = [ (x/720 + x_coor) for x in res_dict[(p,b)][2]]
	#print(len(xx))
	print(max(xx))
	#yy = [(y/100 + y_coor) for y in res_dict[(g,b)][0]]
	yy = [(y/3 + (y_coor-1)*100) for y in res_dict[(p,b)][1]]

	ax.plot(xx,yy)

for x,p in enumerate(pi):
	for y,b in enumerate(bi):
		ax.text(x,-120, 'P: '+ (str(p))[:4], fontsize = 5)
		ax.text(-1,(y*100)-120, 'V: '+ (str(b))[:4], fontsize = 5)
		plot_sense(ax, p, b, res_dict, x, y)

ax.text(5, -200, 'Time (1 Month)')
ax.text(-1.5, 500, 'Population of Informed Agents [0,1]', rotation='vertical')



plt.show()
