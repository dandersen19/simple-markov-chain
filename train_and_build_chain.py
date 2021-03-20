# Create transition table from any number of sequences
# Use transition table to build Markov chain

import numpy as np
import pandas as pd
import random

# Sequences
# integer lists that represent sequence of discrete states
sequence1 = [0, 1, 1, 2, 3, 4, 3, 2, 1, 0]
sequence2 = [1, 1, 1, 2, 1, 1, 2, 4, 1, 0]

# Function to generate transition table
def make_table(allSeq):
    # Size of the transition array
    n = max([ max(s) for s in allSeq ]) + 1
    # Transition array, initially empty
    arr = np.zeros((n,n), dtype=int)
    for s in allSeq:
        for i,j in zip(seq[1:],seq[:-1]): # now counts multiples of same succession of elemennts
            ind = (i,j)
            arr[ind] += 1
    # Return as a DataFrame (normalizing not necessary for input to random.choices)
    return pd.DataFrame(arr).rename_axis(index='Next', columns='Current')

# Call function to generate transition table from any number of sequences
transitions = make_table([sequence1, sequence2])

# Function for generating Markov chain
def make_chain(t_m, start_term, n): # trans_table, start_state, num_steps
    chain = [start_term]
    for i in range(n-1):
        chain.append(get_next_term(t_m[chain[-1]]))
    return chain

# Nested function for each step
def get_next_term(t_s):
    return random.choices(t_s.index, t_s)[0]

# Call function (transition table, starting value, number of steps)
make_chain(transitions, 0, 10)
