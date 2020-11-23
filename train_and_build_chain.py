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
        ind = (s[1:], s[:-1])  # Indices of elements for existing transitions
        arr[ind] += 1          # Add existing transitions
    # Normalize by columns and return as a DataFrame
    return pd.DataFrame(arr / arr.sum(axis=0)).rename_axis(index='Next', columns='Current')

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