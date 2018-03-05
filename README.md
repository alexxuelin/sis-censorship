# SIR-Censorship
This project models the spread of information using the SIS model for epidemics

## SIS_stochastic.py 
Visualizes 4 simulations of the SIS model (without birth or death, using poisson process time interval) over a one month period

## SIS_stochastic_pdfs.py
Visualizes probability distributions of 5000 runs of the SIS model in SIS_stochastic.py over one month, stopping after every week

## SIS_stochastic_params.py
Sweep parameters like beta and gamma on the foundation of SIS_stochastic and SIS_stochastic_pdfs to investigate sensitivity

## SIS_stochastic_bd.py
Adding birth and death processes to the basic model
