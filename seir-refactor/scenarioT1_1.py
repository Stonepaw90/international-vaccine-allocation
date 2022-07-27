# Scenario parameters for seir_opt script
# T1.1 T=1, T1.2 T = 2, T1.3 T = 180 and v = 2

r_I = 1 / 5     # rate out of exposed (E) state into infectious (I) state
r_0 = 1 / 3.5   # rate out of infectious state without testing
r_R =  1 / 15   # rate out of state hospitalized (H) into recovery or death
p_V_H = 0.02    # P(Hospitalized | Infected and Vaxxed)
p_H = 0.2       # P(Hospitalized | Infected)
p_D = 0.1       # P(Dead | Hospitalized)
a_0 = 0.6       # Initial infection rate (proportion/day)
delta_a = 0.6   # Change in infection rate for a new variant (proportion/day)
p_e = 0.6       # Transmission rate from a vaccinated person (proportion of unvaccinated rate)
p_r = 0.6       # Infection rate for a vaccinated person (proportion of unvaccinated rate)
L = 20          # Lag parameter in days for the time a variant takes to reach other area
T_D = 45        # Time for variant to dominate area
p = 0.01        # proportion of people in infected state that have new variant when introduced
T = 180         # Time horizon
B_0 = 1750      # Vaccine available day 1
b = [] #Vaccine availability as a proportion of day 0, by day = 0,...,T-1. Default = 1