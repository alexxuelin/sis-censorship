# SIR-Censorship
This project models the spread of information using models for epidemics

## SIS_stochastic.py (DONE)
Visualizes 4 simulations of the SIS model (without birth or death, poisson event time interval) over a one month period

## SIS_stochastic_pdfs.py (DONE)
Visualizes probability distributions of 1000 runs of the SIS model in SIS_stochastic.py over one month, stopping at 1, 5, 10, and 15 days

## SIS_stochastic_params.py (TODO 1)
Sweep parameters like beta and gamma on the foundation of SIS_stochastic and SIS_stochastic_pdfs to investigate sensitivity
Remember -  the significance of ratio between beta and gamma! Take a look at book chapter 2 for things like threshold, asymptote, etc.
threshold - what determines whether an epidemic will occur of fail to invade
Basic reproductive ratio - the avg number of secondary cases arising from an average primary case in an entirely susceptible population - BETA/GAMMA
Its inverse is the relative removal rate - GAMMA/BETA

## SIS_stochastic_bd.py
Adding birth and death processes to the original model.

## Compare with Real Data (TODO)
Not sure if this is feasible, but we can see if there's data on how information spread and see if our model is predictive

## For Reference Only Folder
Some other implementations. Some of those can't be run because we can't recreate others' environments, but we can look at what people tweaked, delete this before submission
